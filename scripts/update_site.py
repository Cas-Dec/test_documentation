#!/usr/bin/env python3
"""Orchestrate the full documentation site update pipeline.

This script is designed to run from a cron job on the HPC. It:
1. Scans $VSC_DATA_VO/shared for metadata.yaml files
2. Validates all metadata against the JSON schema
3. Detects added/moved/deleted datasets
4. Rebuilds the dataset catalog
5. Rebuilds the MkDocs site
6. Optionally commits changes and creates a PR

Usage:
    # Dry run (no git operations)
    python scripts/update_site.py --dry-run

    # Full update with git commit
    python scripts/update_site.py --commit

    # Email notifications on validation errors
    python scripts/update_site.py --notify-on-error

Exit codes:
    0 - Success
    1 - Validation errors (site still built if possible)
    2 - Fatal error (cannot continue)
"""
import argparse
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple

import yaml
from jsonschema import Draft7Validator

# Configure paths
REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schema" / "dataset-schema.json"
SHARED_DIR = REPO_ROOT / "VSC_DATA_VO" / "shared"
CATALOG_DIR = REPO_ROOT / "docs-site" / "docs" / "datasets"
STATE_FILE = REPO_ROOT / ".automation-state.json"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class DatasetTracker:
    """Track dataset changes between runs."""

    def __init__(self, state_file: Path):
        self.state_file = state_file
        self.previous_state = self._load_state()

    def _load_state(self) -> Dict[str, str]:
        """Load previous state from file."""
        if not self.state_file.exists():
            return {}
        try:
            return json.loads(self.state_file.read_text(encoding="utf-8"))
        except Exception as e:
            logger.warning(f"Could not load previous state: {e}")
            return {}

    def save_state(self, current_datasets: Dict[str, str]):
        """Save current state to file."""
        self.state_file.write_text(
            json.dumps(current_datasets, indent=2),
            encoding="utf-8"
        )

    def detect_changes(
        self, current_datasets: Dict[str, str]
    ) -> Tuple[Set[str], Set[str], Set[str]]:
        """Detect added, removed, and modified datasets.

        Returns:
            (added, removed, modified) dataset names
        """
        prev_names = set(self.previous_state.keys())
        curr_names = set(current_datasets.keys())

        added = curr_names - prev_names
        removed = prev_names - curr_names

        # Modified = same name but different path
        modified = {
            name for name in (prev_names & curr_names)
            if self.previous_state[name] != current_datasets[name]
        }

        return added, removed, modified


class MetadataValidator:
    """Validate metadata.yaml files against JSON schema."""

    def __init__(self, schema_path: Path):
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self.validator = Draft7Validator(schema)

    def validate_file(self, path: Path) -> Tuple[bool, List[str]]:
        """Validate a single metadata.yaml file.

        Returns:
            (is_valid, error_messages)
        """
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            return False, [f"YAML parsing error: {e}"]

        errors = sorted(self.validator.iter_errors(data), key=lambda e: e.path)
        if errors:
            messages = []
            for err in errors:
                loc = ".".join(str(p) for p in err.path) or "<root>"
                messages.append(f"{loc}: {err.message}")
            return False, messages

        return True, []

    def validate_all(self, metadata_files: List[Path]) -> Tuple[Dict[Path, List[str]], int]:
        """Validate all metadata files.

        Returns:
            (errors_by_file, valid_count)
        """
        errors_by_file = {}
        valid_count = 0

        for path in metadata_files:
            is_valid, errors = self.validate_file(path)
            rel = path.relative_to(REPO_ROOT)

            if is_valid:
                logger.info(f"✓ {rel}")
                valid_count += 1
            else:
                logger.error(f"✗ {rel}")
                for err in errors:
                    logger.error(f"    {err}")
                errors_by_file[path] = errors

        return errors_by_file, valid_count


def find_metadata_files(shared_dir: Path) -> List[Path]:
    """Find all metadata.yaml files under shared_dir."""
    return sorted(shared_dir.rglob("metadata.yaml"))


def category_of(metadata_path: Path, shared_dir: Path) -> str:
    """Extract category from metadata path."""
    return metadata_path.relative_to(shared_dir).parts[0]


def render_dataset_page(meta: dict, category: str, rel_data_path: str) -> str:
    """Render a dataset documentation page."""
    d = meta["dataset"]
    src = meta["source"]
    cov = meta["coverage"]
    contact = meta["contact"]

    lines = [
        f"# {d['name']}",
        "",
        f"*{d['long_name']}*",
        "",
        d["description"].strip(),
        "",
        "## Details",
        "",
        "| | |",
        "|---|---|",
        f"| **Category** | `{category}` |",
        f"| **Version** | {d.get('version', '-')} |",
        f"| **Provider** | {src['provider']} |",
        f"| **License** | {src['license']} |",
        f"| **Source URL** | {src['url'] or '-'} |",
        f"| **DOI** | {src.get('doi') or '-'} |",
        f"| **Spatial domain** | {cov['spatial']['domain']} |",
        f"| **Spatial resolution** | {cov['spatial']['resolution']} |",
        f"| **Temporal coverage** | {cov['temporal']['start']} to {cov['temporal']['end']} |",
        f"| **Frequency** | {cov['temporal']['frequency']} |",
        f"| **Contact** | {contact['name']} ({contact['email']}, {contact['vsc_username']}) |",
        f"| **Path** | `{rel_data_path}` |",
        "",
        "## Variables",
        "",
        "| short_name | standard_name | units |",
        "|---|---|---|",
    ]
    for v in meta["variables"]:
        lines.append(f"| `{v['short_name']}` | {v['standard_name']} | {v['units']} |")

    lines += ["", "## Processing history", ""]
    for h in meta["history"]:
        lines.append(f"- **{h['date']}** — {h['description']} ([source]({h['source']}))")

    lines.append("")
    return "\n".join(lines)


def build_catalog(metadata_files: List[Path], out_dir: Path, shared_dir: Path):
    """Build the dataset catalog documentation."""
    logger.info(f"Building catalog from {len(metadata_files)} metadata files...")

    # Clean up old dataset pages (but keep index.md)
    for old in out_dir.glob("*.md"):
        if old.name != "index.md":
            old.unlink()
            logger.debug(f"Removed old page: {old.name}")

    by_category = {}
    for path in metadata_files:
        meta = yaml.safe_load(path.read_text(encoding="utf-8"))
        category = category_of(path, shared_dir)
        name = meta["dataset"]["name"]
        rel_data_path = str(path.parent.relative_to(REPO_ROOT)).replace("\\", "/")

        page = render_dataset_page(meta, category, rel_data_path)
        (out_dir / f"{name}.md").write_text(page, encoding="utf-8")
        logger.info(f"  Generated datasets/{name}.md")

        by_category.setdefault(category, []).append((name, meta["dataset"]["long_name"]))

    # Build index page
    index_lines = [
        "# Data catalog",
        "",
        f"Auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} from",
        "`metadata.yaml` files under `VSC_DATA_VO/shared/`. Do not edit by hand.",
        ""
    ]
    for category in sorted(by_category):
        index_lines.append(f"## {category}")
        index_lines.append("")
        for name, long_name in sorted(by_category[category]):
            index_lines.append(f"- [{name}]({name}.md) — {long_name}")
        index_lines.append("")

    (out_dir / "index.md").write_text("\n".join(index_lines), encoding="utf-8")
    logger.info("  Generated datasets/index.md")


def build_site():
    """Build the MkDocs site."""
    import subprocess

    logger.info("Building MkDocs site...")
    result = subprocess.run(
        ["mkdocs", "build"],
        cwd=REPO_ROOT / "docs-site",
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        logger.error("MkDocs build failed!")
        logger.error(result.stderr)
        return False

    logger.info("✓ MkDocs site built successfully")
    return True


def commit_changes(message: str) -> bool:
    """Commit changes to git."""
    import subprocess

    logger.info("Committing changes to git...")

    # Check if there are changes
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True
    )

    if not result.stdout.strip():
        logger.info("No changes to commit")
        return True

    # Add changes
    subprocess.run(["git", "add", "docs-site/docs/datasets/"], cwd=REPO_ROOT)
    subprocess.run(["git", "add", "docs-site/site/"], cwd=REPO_ROOT)
    subprocess.run(["git", "add", ".automation-state.json"], cwd=REPO_ROOT)

    # Commit
    result = subprocess.run(
        ["git", "commit", "-m", message],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        logger.error(f"Git commit failed: {result.stderr}")
        return False

    logger.info("✓ Changes committed")
    return True


def send_notification(errors_by_file: Dict[Path, List[str]]):
    """Send email notifications for validation errors."""
    logger.info("Sending email notifications...")

    # Extract contact emails from invalid metadata files
    for path, errors in errors_by_file.items():
        try:
            meta = yaml.safe_load(path.read_text(encoding="utf-8"))
            contact_email = meta.get("contact", {}).get("email")
            if contact_email:
                logger.info(f"  Would notify {contact_email} about {path.name}")
                # TODO: Implement actual email sending via HPC mail system
        except Exception as e:
            logger.warning(f"Could not extract contact from {path}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Update HPC documentation site")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run without committing changes")
    parser.add_argument("--commit", action="store_true",
                        help="Commit changes to git")
    parser.add_argument("--notify-on-error", action="store_true",
                        help="Send email notifications on validation errors")
    parser.add_argument("--shared-dir", type=Path,
                        help="Override shared directory path")
    args = parser.parse_args()

    shared_dir = args.shared_dir or SHARED_DIR

    logger.info("=" * 60)
    logger.info("HPC Documentation Site Update")
    logger.info("=" * 60)

    # Find all metadata files
    metadata_files = find_metadata_files(shared_dir)
    logger.info(f"Found {len(metadata_files)} metadata.yaml files")

    if not metadata_files:
        logger.error(f"No metadata.yaml files found under {shared_dir}")
        return 2

    # Track dataset changes
    tracker = DatasetTracker(STATE_FILE)
    current_datasets = {
        yaml.safe_load(p.read_text(encoding="utf-8"))["dataset"]["name"]: str(p.relative_to(REPO_ROOT))
        for p in metadata_files
    }
    added, removed, modified = tracker.detect_changes(current_datasets)

    if added or removed or modified:
        logger.info("\nDataset changes detected:")
        for name in sorted(added):
            logger.info(f"  + Added: {name}")
        for name in sorted(removed):
            logger.info(f"  - Removed: {name}")
        for name in sorted(modified):
            logger.info(f"  ~ Moved: {name}")
        logger.info("")
    else:
        logger.info("No dataset changes detected\n")

    # Validate all metadata
    validator = MetadataValidator(SCHEMA_PATH)
    errors_by_file, valid_count = validator.validate_all(metadata_files)

    logger.info(f"\nValidation: {valid_count}/{len(metadata_files)} passed")

    if errors_by_file and args.notify_on_error:
        send_notification(errors_by_file)

    # Build catalog from valid metadata only
    valid_files = [f for f in metadata_files if f not in errors_by_file]

    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    build_catalog(valid_files, CATALOG_DIR, shared_dir)

    # Build site
    if not build_site():
        return 2

    # Save state
    tracker.save_state(current_datasets)

    # Commit if requested
    if args.commit and not args.dry_run:
        commit_msg = f"Auto-update documentation ({datetime.now().strftime('%Y-%m-%d %H:%M')})"
        if added or removed or modified:
            changes = []
            if added:
                changes.append(f"{len(added)} added")
            if removed:
                changes.append(f"{len(removed)} removed")
            if modified:
                changes.append(f"{len(modified)} moved")
            commit_msg += f"\n\n{', '.join(changes)}"

        if not commit_changes(commit_msg):
            return 2

    logger.info("\n✓ Update complete!")

    # Return error code if there were validation errors
    return 1 if errors_by_file else 0


if __name__ == "__main__":
    sys.exit(main())
