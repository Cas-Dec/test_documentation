#!/usr/bin/env python
"""Validate every dataset's metadata.yaml under $VSC_DATA_VO/shared against
schema/dataset-schema.json.

Usage: python scripts/validate_metadata.py [shared_dir]
"""
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft7Validator

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schema" / "dataset-schema.json"
DEFAULT_SHARED_DIR = REPO_ROOT / "VSC_DATA_VO" / "shared"


def find_metadata_files(shared_dir: Path):
    return sorted(shared_dir.rglob("metadata.yaml"))


def main():
    shared_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SHARED_DIR

    # For CI: if default shared_dir doesn't exist, exit successfully
    if not shared_dir.exists():
        print(f"Directory {shared_dir} does not exist - skipping validation")
        return 0

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft7Validator(schema)

    metadata_files = find_metadata_files(shared_dir)
    if not metadata_files:
        print(f"no metadata.yaml files found under {shared_dir}")
        return 0  # Not an error for CI

    had_errors = False
    for path in metadata_files:
        rel = path.relative_to(REPO_ROOT)
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
        if errors:
            had_errors = True
            print(f"FAIL  {rel}")
            for err in errors:
                loc = ".".join(str(p) for p in err.path) or "<root>"
                print(f"        {loc}: {err.message}")
        else:
            print(f"OK    {rel}")

    print()
    print(f"{len(metadata_files)} dataset(s) checked")
    return 1 if had_errors else 0


if __name__ == "__main__":
    sys.exit(main())
