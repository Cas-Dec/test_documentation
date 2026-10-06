# Quick Reference Card

## New User? Start Here

1. **Read the overview**: [STRUCTURE_DIAGRAM.md](STRUCTURE_DIAGRAM.md)
2. **Understand why**: [README.md](README.md#why-this-reform)
3. **Browse datasets**: Documentation site (link TBD)

## Adding a Dataset

```bash
# 1. Create directory
mkdir -p $VSC_DATA_VO/shared/<category>/<dataset_name>

# 2. Copy template
cp schema/metadata-template.yaml $VSC_DATA_VO/shared/<category>/<dataset_name>/metadata.yaml

# 3. Edit metadata
vim $VSC_DATA_VO/shared/<category>/<dataset_name>/metadata.yaml

# 4. Validate
python scripts/validate_metadata.py

# 5. Done! (automation handles the rest)
```

## Common Commands

### Validate metadata
```bash
python scripts/validate_metadata.py
```

### Build documentation locally
```bash
python scripts/build_catalog.py
cd docs-site && mkdocs serve
```

### Set up automation
```bash
bash scripts/setup_cron.sh --install
```

### Check automation status
```bash
bash scripts/setup_cron.sh --check
tail -f logs/cron-update.log
```

### Download site to local machine
```bash
# From your local machine:
rsync -avz --progress vsc46240@login.hpc.ugent.be:/path/to/HPC-docs/docs-site/site/ ./hpc-docs-site/
```

## Directory Structure

```
$VSC_DATA_VO/
├── shared/
│   ├── external/     # Downloaded datasets
│   ├── processed/    # Modified data
│   ├── generated/    # Lab outputs
│   └── observations/ # Observational data
├── projects/         # Project workspaces
└── personal/         # User scratch
```

## Categories Explained

| Category | For | Examples |
|----------|-----|----------|
| `external` | Downloaded from external sources | ERA5, CHIRPS, MODIS |
| `processed` | Modified external data | Bias-corrected, regridded |
| `generated` | Lab-produced outputs | Model runs, derived products |
| `observations` | Observational datasets | Weather stations, radiosonde |

## Metadata Template

Every dataset needs a `metadata.yaml`:

```yaml
dataset: {name, long_name, version, description}
source: {provider, url, doi, license}
coverage:
  spatial: {domain, resolution}
  temporal: {start, end, frequency}
variables: [{short_name, standard_name, units}, ...]
contact: {name, email, vsc_username}
history: [{date, description, source}, ...]
```

## File Naming Convention

Format: `{variable}_{dataset}_{frequency}_{period}.nc`

Examples:
- `tas_ERA5_1hr_197901-197912.nc`
- `pr_CHIRPS_day_2020-2020.nc`

## CF Variable Names

Use CF standard names, not provider-specific labels:

| CF Name | Standard Name | Instead of |
|---------|---------------|------------|
| `tas` | air_temperature | t2m, temp |
| `pr` | precipitation_flux | tp, precip |
| `huss` | specific_humidity | q, QV |

See: http://cfconventions.org/standard-names.html

## Troubleshooting

**Validation errors?**
```bash
python scripts/validate_metadata.py
# Fix the errors it reports
```

**Site won't build?**
```bash
cd docs-site
mkdocs build --verbose
```

**Cron not running?**
```bash
bash scripts/setup_cron.sh --check
tail -f logs/cron-update.log
```

## Getting Help

- **Schema questions**: `schema/metadata-template.yaml`
- **Automation**: [AUTOMATION.md](AUTOMATION.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Full docs**: [README.md](../README.md)

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Main documentation |
| `STRUCTURE_DIAGRAM.md` | Visual overview |
| `QUICKSTART_AUTOMATION.md` | Automation setup |
| `CONTRIBUTING.md` | How to contribute |
| `REFORM.md` | Full proposal |

## Automation Schedule

Default: Every 6 hours

Customize:
```bash
CRON_SCHEDULE="0 2 * * *" bash scripts/setup_cron.sh --install
```

## Production Checklist

- [ ] Metadata validated
- [ ] Documentation builds locally
- [ ] Automation tested (dry-run)
- [ ] Cron job installed
- [ ] Logs monitored
- [ ] Team notified

---

**Next steps:** Read [README.md](../README.md) or [STRUCTURE_DIAGRAM.md](STRUCTURE_DIAGRAM.md)
