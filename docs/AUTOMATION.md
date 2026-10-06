# Documentation Automation

This document explains how to set up automated updates for the HPC documentation site based on changes to `$VSC_DATA_VO`.

## Overview

The automation system:

1. **Scans** `$VSC_DATA_VO/shared` for `metadata.yaml` files
2. **Validates** metadata against the JSON schema
3. **Detects** added, moved, or deleted datasets
4. **Rebuilds** the dataset catalog documentation
5. **Regenerates** the MkDocs static site
6. **Commits** changes to git (optional)
7. **Notifies** dataset contacts on validation errors (optional)

## Quick Start

### Test the automation (dry-run)

```bash
cd /path/to/HPC-docs
python scripts/update_site.py --dry-run
```

### Set up automated updates via cron

```bash
# Test first
bash scripts/setup_cron.sh --test

# Install cron job (runs every 6 hours)
bash scripts/setup_cron.sh --install

# Check status
bash scripts/setup_cron.sh --check

# View logs
tail -f logs/cron-update.log
```

### Alternative: Real-time file watching

```bash
# Install watchdog
pip install watchdog

# Start the watcher (runs indefinitely)
python scripts/watch_and_update.py
```

## Components

### 1. `scripts/update_site.py`

Main orchestration script that handles the complete update pipeline.

**Usage:**

```bash
# Dry run (no git operations)
python scripts/update_site.py --dry-run

# Full update with git commit
python scripts/update_site.py --commit

# Email notifications on validation errors
python scripts/update_site.py --notify-on-error

# Override shared directory
python scripts/update_site.py --shared-dir /custom/path
```

**What it does:**

- Finds all `metadata.yaml` files under `$VSC_DATA_VO/shared`
- Validates each file against `schema/dataset-schema.json`
- Tracks changes since last run (stored in `.automation-state.json`)
- Logs all changes: added, removed, and moved datasets
- Regenerates dataset documentation pages
- Rebuilds the MkDocs site
- Commits changes to git (if `--commit` flag is used)

**Exit codes:**

- `0` - Success, no validation errors
- `1` - Validation errors found (site still built from valid metadata)
- `2` - Fatal error (cannot continue)

### 2. `scripts/setup_cron.sh`

Helper script to install/manage cron jobs for automated updates.

**Usage:**

```bash
# Install cron job (default: every 6 hours)
bash scripts/setup_cron.sh --install

# Custom schedule (daily at 2 AM)
CRON_SCHEDULE="0 2 * * *" bash scripts/setup_cron.sh --install

# Remove cron job
bash scripts/setup_cron.sh --uninstall

# Check current configuration
bash scripts/setup_cron.sh --check

# Test the update script
bash scripts/setup_cron.sh --test
```

**Cron schedule examples:**

| Schedule | Cron expression |
|----------|----------------|
| Every 6 hours | `0 */6 * * *` |
| Daily at midnight | `0 0 * * *` |
| Daily at 2 AM | `0 2 * * *` |
| Every 30 minutes | `*/30 * * * *` |
| Twice daily (6 AM, 6 PM) | `0 6,18 * * *` |

### 3. `scripts/watch_and_update.py`

Real-time file watcher that triggers updates on changes (alternative to cron).

**Usage:**

```bash
# Install dependency
pip install watchdog

# Watch with default settings (30s debounce)
python scripts/watch_and_update.py

# Custom debounce interval (wait 60s before rebuilding)
python scripts/watch_and_update.py --debounce 60

# Verbose logging
python scripts/watch_and_update.py --verbose
```

**What it watches:**

- `metadata.yaml` files
- `README.md` files (future enhancement)

**How it works:**

- Uses `inotify` (Linux) to monitor file system events
- Debounces rapid changes to avoid excessive rebuilds
- Automatically triggers `update_site.py --commit` on changes

### 4. `scripts/validate_metadata.py`

Standalone validation script (used by `update_site.py`).

**Usage:**

```bash
# Validate all metadata in default location
python scripts/validate_metadata.py

# Validate metadata in custom directory
python scripts/validate_metadata.py /custom/shared/dir
```

### 5. `scripts/build_catalog.py`

Standalone catalog builder (used by `update_site.py`).

**Usage:**

```bash
# Rebuild the dataset catalog
python scripts/build_catalog.py
```

## Dependencies

### Python packages

```bash
pip install pyyaml jsonschema mkdocs mkdocs-material
```

For file watching:

```bash
pip install watchdog
```

### System requirements

- Python 3.7+
- Git
- Cron (for scheduled updates)
- Linux with inotify support (for file watching)

## Deployment Scenarios

### Scenario 1: Scheduled updates (Recommended for HPC)

Best for stable, predictable updates without overhead.

```bash
# Install cron job to run every 6 hours
bash scripts/setup_cron.sh --install

# Monitor logs
tail -f logs/cron-update.log
```

**Pros:**
- Low resource usage
- Predictable execution times
- Easy to manage

**Cons:**
- Updates not immediate (max 6 hour delay)

### Scenario 2: Real-time watching

Best for development or when immediate updates are needed.

```bash
# Run watcher as a background process
nohup python scripts/watch_and_update.py &> logs/watcher.log &

# Or use screen/tmux
screen -S doc-watcher
python scripts/watch_and_update.py
# Ctrl+A, D to detach
```

**Pros:**
- Immediate updates on changes
- Great for development

**Cons:**
- Requires long-running process
- Higher resource usage

### Scenario 3: Manual updates

Best for testing or one-off updates.

```bash
# Run update manually
python scripts/update_site.py --commit
```

## Workflow

### When a dataset is added

1. Researcher creates new dataset under `$VSC_DATA_VO/shared/<category>/<dataset>/`
2. Researcher adds `metadata.yaml` following the schema
3. Automation detects new metadata file
4. Validates metadata against schema
5. If valid: generates documentation page
6. Rebuilds site
7. Commits changes to git

### When a dataset is moved

1. Dataset folder is moved to new location
2. Automation detects path change
3. Updates documentation with new path
4. Rebuilds site
5. Commits changes

### When a dataset is deleted

1. Dataset folder is removed
2. Automation detects missing metadata
3. Removes corresponding documentation page
4. Rebuilds site
5. Commits changes

### When metadata is invalid

1. Validation fails with schema errors
2. Error is logged with details
3. Dataset contact is notified via email (if `--notify-on-error`)
4. Site is built from remaining valid metadata
5. No commit is made for invalid metadata

## State Tracking

The automation maintains state in `.automation-state.json`:

```json
{
  "ERA5": "VSC_DATA_VO/shared/external/ERA5",
  "CHIRPS": "VSC_DATA_VO/shared/external/CHIRPS",
  "SNOWSHOP-Sentinel1": "VSC_DATA_VO/shared/generated/SNOWSHOP"
}
```

This enables detection of:
- **New datasets**: names not in previous state
- **Deleted datasets**: names in previous state but not current
- **Moved datasets**: same name but different path

## Logs

All automation logs are stored in `logs/`:

```bash
# Cron execution logs
tail -f logs/cron-update.log

# Watch script logs (if using watcher)
tail -f logs/watcher.log
```

## Troubleshooting

### Cron job not running

```bash
# Check if cron job is installed
bash scripts/setup_cron.sh --check

# Check cron daemon is running
systemctl status cron  # or crond on some systems

# Check logs for errors
tail -f logs/cron-update.log
```

### Validation errors

```bash
# Run validation standalone
python scripts/validate_metadata.py

# Check specific metadata file
python -c "
import yaml
from pathlib import Path
print(yaml.safe_load(Path('path/to/metadata.yaml').read_text()))
"
```

### MkDocs build fails

```bash
# Test MkDocs build manually
cd docs-site
mkdocs build --verbose
```

### File watcher not detecting changes

```bash
# Check inotify limits (Linux)
cat /proc/sys/fs/inotify/max_user_watches

# Increase if needed (temporary)
sudo sysctl fs.inotify.max_user_watches=524288

# Test with verbose logging
python scripts/watch_and_update.py --verbose
```

## Notification System

Currently, the `--notify-on-error` flag logs which contacts should be notified but doesn't send actual emails.

To implement email notifications:

1. Configure HPC mail system access
2. Edit `update_site.py` function `send_notification()`
3. Use `sendmail`, `mail`, or SMTP library

Example implementation:

```python
def send_notification(errors_by_file: Dict[Path, List[str]]):
    import smtplib
    from email.message import EmailMessage

    for path, errors in errors_by_file.items():
        meta = yaml.safe_load(path.read_text())
        contact = meta.get("contact", {})

        msg = EmailMessage()
        msg["Subject"] = f"Validation error in {meta['dataset']['name']}"
        msg["From"] = "hpc-docs@example.com"
        msg["To"] = contact.get("email")
        msg.set_content(f"Errors:\n" + "\n".join(errors))

        # Send via SMTP
        with smtplib.SMTP("localhost") as smtp:
            smtp.send_message(msg)
```

## Best Practices

1. **Always test first**: Use `--dry-run` before enabling commits
2. **Monitor logs**: Regularly check `logs/cron-update.log`
3. **Validate locally**: Run `validate_metadata.py` before committing metadata
4. **Use appropriate schedule**: Don't run cron too frequently (every 6 hours is reasonable)
5. **Keep state file**: Don't delete `.automation-state.json` (it tracks changes)
6. **Git hygiene**: Regularly review auto-commits for accuracy

## Future Enhancements

Potential improvements:

- [ ] Integrate with GitHub Actions for PR creation
- [ ] Slack/email notifications
- [ ] Dashboard for validation status
- [ ] Auto-deployment to web server
- [ ] Metadata health checks (e.g., check if dataset paths actually exist)
- [ ] Integration with HPC job scheduler for resource-heavy rebuilds
- [ ] Support for `README.md` documentation in addition to metadata.yaml

## Support

For issues or questions:

1. Check logs: `logs/cron-update.log`
2. Run with `--dry-run` to test
3. Validate metadata: `python scripts/validate_metadata.py`
4. Review this documentation
5. Contact HPC team or repository maintainers
