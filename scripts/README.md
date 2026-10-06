# Automation Scripts

This directory contains scripts for automated documentation updates.

## Quick Reference

### Test the automation

```bash
python update_site.py --dry-run
```

### Set up cron (recommended)

```bash
# Test
bash setup_cron.sh --test

# Install (runs every 6 hours)
bash setup_cron.sh --install

# Check status
bash setup_cron.sh --check
```

### Use real-time file watching

```bash
pip install watchdog
python watch_and_update.py
```

## Scripts

| Script | Purpose |
|--------|---------|
| `update_site.py` | Main orchestration script - validates, builds, commits |
| `setup_cron.sh` | Install/manage cron jobs for scheduled updates |
| `watch_and_update.py` | Real-time file watcher (alternative to cron) |
| `validate_metadata.py` | Standalone metadata validation |
| `build_catalog.py` | Standalone catalog builder |

## Documentation

See [AUTOMATION.md](../AUTOMATION.md) for complete documentation.
