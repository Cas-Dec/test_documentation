# Quick Start: Documentation Automation

## Download the HTML site to your local machine

From your **local machine**, run:

```bash
rsync -avz --progress vsc46240@login.hpc.ugent.be:/kyukon/scratch/gent/vo/000/gvo00090/vsc46240/PhD/HPC-docs/docs-site/site/ ./hpc-docs-site/
```

Then open `./hpc-docs-site/index.html` in your browser.

## Set up automated updates (Recommended)

### Option 1: Cron-based updates (Recommended for HPC)

```bash
# 1. Test the automation
bash scripts/setup_cron.sh --test

# 2. Install cron job (runs every 6 hours)
bash scripts/setup_cron.sh --install

# 3. Check it's running
bash scripts/setup_cron.sh --check

# 4. Monitor logs
tail -f logs/cron-update.log
```

**Customize the schedule:**

```bash
# Run daily at 2 AM instead
CRON_SCHEDULE="0 2 * * *" bash scripts/setup_cron.sh --install
```

### Option 2: Real-time file watching

For immediate updates when metadata changes:

```bash
# 1. Install watchdog
pip install watchdog

# 2. Start the watcher
python scripts/watch_and_update.py

# Or run in background
nohup python scripts/watch_and_update.py &> logs/watcher.log &
```

## Manual updates

```bash
# Dry run (preview what would happen)
python scripts/update_site.py --dry-run

# Full update with git commit
python scripts/update_site.py --commit
```

## What the automation does

1. ✓ Scans `$VSC_DATA_VO/shared/**/metadata.yaml`
2. ✓ Validates all metadata against JSON schema
3. ✓ Detects added/moved/deleted datasets
4. ✓ Rebuilds dataset catalog documentation
5. ✓ Regenerates MkDocs site
6. ✓ Commits changes to git (optional)
7. ✓ Notifies dataset contacts on errors (optional)

## Files created

| File | Purpose |
|------|---------|
| `scripts/update_site.py` | Main orchestration script |
| `scripts/setup_cron.sh` | Cron job installer/manager |
| `scripts/watch_and_update.py` | Real-time file watcher |
| `AUTOMATION.md` | Complete documentation |
| `scripts/README.md` | Scripts quick reference |

## Troubleshooting

**Cron not running?**
```bash
bash scripts/setup_cron.sh --check
```

**Validation errors?**
```bash
python scripts/validate_metadata.py
```

**View logs:**
```bash
tail -f logs/cron-update.log
```

## Next steps

1. ✓ Test the automation: `bash scripts/setup_cron.sh --test`
2. ✓ Fix any validation errors in your metadata files
3. ✓ Install cron job: `bash scripts/setup_cron.sh --install`
4. ✓ Monitor logs to ensure it's working

For complete documentation, see [AUTOMATION.md](AUTOMATION.md).
