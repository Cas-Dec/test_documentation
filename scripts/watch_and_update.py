#!/usr/bin/env python3
"""Watch $VSC_DATA_VO for changes and trigger documentation updates.

This is an alternative to cron-based updates. It uses inotify (Linux) to
watch for file system changes and triggers rebuilds automatically.

Usage:
    # Watch and auto-rebuild on changes
    python scripts/watch_and_update.py

    # Watch with custom debounce interval (seconds)
    python scripts/watch_and_update.py --debounce 60

    # Watch with verbose logging
    python scripts/watch_and_update.py --verbose

Requirements:
    pip install watchdog

Note: This script should run as a long-lived process, potentially managed
by systemd or supervisor on the HPC.
"""
import argparse
import logging
import subprocess
import sys
import time
from pathlib import Path
from typing import Set

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler, FileSystemEvent
except ImportError:
    print("ERROR: watchdog package not found")
    print("Install with: pip install watchdog")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
SHARED_DIR = REPO_ROOT / "VSC_DATA_VO" / "shared"
UPDATE_SCRIPT = REPO_ROOT / "scripts" / "update_site.py"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class DebounceHandler:
    """Debounce rapid file changes to avoid excessive rebuilds."""

    def __init__(self, callback, debounce_seconds: int = 30):
        self.callback = callback
        self.debounce_seconds = debounce_seconds
        self.pending_paths: Set[Path] = set()
        self.last_trigger_time = 0

    def add_change(self, path: Path):
        """Add a changed path and potentially trigger callback."""
        self.pending_paths.add(path)
        current_time = time.time()

        # Only trigger if enough time has passed since last trigger
        if current_time - self.last_trigger_time >= self.debounce_seconds:
            self.trigger()

    def trigger(self):
        """Execute the callback with accumulated changes."""
        if not self.pending_paths:
            return

        logger.info(f"Triggering update for {len(self.pending_paths)} changed paths")
        self.callback(list(self.pending_paths))
        self.pending_paths.clear()
        self.last_trigger_time = time.time()


class MetadataChangeHandler(FileSystemEventHandler):
    """Watch for changes to metadata.yaml and README files."""

    def __init__(self, debouncer: DebounceHandler):
        self.debouncer = debouncer
        super().__init__()

    def _is_relevant_file(self, path: str) -> bool:
        """Check if file is relevant for documentation."""
        path_obj = Path(path)
        name = path_obj.name.lower()

        # Watch metadata.yaml and README files
        if name == "metadata.yaml":
            return True
        if name.startswith("readme") and name.endswith(".md"):
            return True

        return False

    def on_created(self, event: FileSystemEvent):
        if not event.is_directory and self._is_relevant_file(event.src_path):
            logger.info(f"Created: {event.src_path}")
            self.debouncer.add_change(Path(event.src_path))

    def on_modified(self, event: FileSystemEvent):
        if not event.is_directory and self._is_relevant_file(event.src_path):
            logger.info(f"Modified: {event.src_path}")
            self.debouncer.add_change(Path(event.src_path))

    def on_deleted(self, event: FileSystemEvent):
        if not event.is_directory and self._is_relevant_file(event.src_path):
            logger.info(f"Deleted: {event.src_path}")
            self.debouncer.add_change(Path(event.src_path))

    def on_moved(self, event: FileSystemEvent):
        if not event.is_directory:
            if self._is_relevant_file(event.src_path):
                logger.info(f"Moved: {event.src_path} -> {event.dest_path}")
                self.debouncer.add_change(Path(event.src_path))
            if self._is_relevant_file(event.dest_path):
                self.debouncer.add_change(Path(event.dest_path))


def run_update(changed_paths: list):
    """Run the update script."""
    logger.info("=" * 60)
    logger.info("Running documentation update...")
    logger.info("=" * 60)

    try:
        result = subprocess.run(
            [sys.executable, str(UPDATE_SCRIPT), "--commit"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True
        )

        # Log output
        if result.stdout:
            for line in result.stdout.splitlines():
                logger.info(line)

        if result.returncode != 0:
            logger.error("Update failed!")
            if result.stderr:
                logger.error(result.stderr)
        else:
            logger.info("✓ Update completed successfully")

    except Exception as e:
        logger.error(f"Failed to run update script: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Watch for changes and auto-update documentation"
    )
    parser.add_argument(
        "--debounce",
        type=int,
        default=30,
        help="Debounce interval in seconds (default: 30)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    parser.add_argument(
        "--watch-dir",
        type=Path,
        help="Override directory to watch"
    )
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    watch_dir = args.watch_dir or SHARED_DIR

    if not watch_dir.exists():
        logger.error(f"Watch directory does not exist: {watch_dir}")
        return 1

    logger.info("=" * 60)
    logger.info("HPC Documentation Watcher")
    logger.info("=" * 60)
    logger.info(f"Watching: {watch_dir}")
    logger.info(f"Debounce: {args.debounce}s")
    logger.info(f"Update script: {UPDATE_SCRIPT}")
    logger.info("")
    logger.info("Monitoring for changes to metadata.yaml and README.md files...")
    logger.info("Press Ctrl+C to stop")
    logger.info("=" * 60)

    # Set up file watcher
    debouncer = DebounceHandler(run_update, args.debounce)
    event_handler = MetadataChangeHandler(debouncer)
    observer = Observer()
    observer.schedule(event_handler, str(watch_dir), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("\nStopping watcher...")
        observer.stop()

    observer.join()
    logger.info("Watcher stopped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
