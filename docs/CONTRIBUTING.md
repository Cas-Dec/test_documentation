# Contributing to HPC Data Documentation

Thank you for helping improve our data infrastructure! This guide explains how to contribute.

## For Dataset Owners

### Adding a New Dataset

1. **Create your dataset directory** following the structure:
   ```bash
   mkdir -p $VSC_DATA_VO/shared/<category>/<dataset_name>
   ```

   Choose the appropriate category:
   - `external/` - Downloaded from external sources
   - `processed/` - Modified versions of external data
   - `generated/` - Lab-generated outputs
   - `observations/` - Observational datasets

2. **Copy the metadata template**:
   ```bash
   cp schema/metadata-template.yaml $VSC_DATA_VO/shared/<category>/<dataset_name>/metadata.yaml
   ```

3. **Fill in the metadata**:
   - Use your favorite editor: `vim`, `nano`, `code`, etc.
   - Follow the inline comments
   - Use CF standard names for variables (see http://cfconventions.org/standard-names.html)
   - Include a permalink to your download/processing script in `history.source`

4. **Validate your metadata**:
   ```bash
   python scripts/validate_metadata.py
   ```

   Fix any errors reported. Common issues:
   - Missing required fields
   - Incorrect date format (must be YYYY-MM-DD)
   - Invalid email format
   - Additional properties not in the schema

5. **Test the documentation build**:
   ```bash
   python scripts/build_catalog.py
   cd docs-site && mkdocs serve
   ```

   Check that your dataset appears correctly at http://127.0.0.1:8000

6. **Submit your changes** (if using git):
   ```bash
   git add $VSC_DATA_VO/shared/<category>/<dataset_name>/metadata.yaml
   git commit -m "Add metadata for <dataset_name>"
   git push
   ```

### Updating Existing Metadata

Simply edit the `metadata.yaml` file and validate:

```bash
vim $VSC_DATA_VO/shared/<category>/<dataset_name>/metadata.yaml
python scripts/validate_metadata.py
```

If automation is enabled, the documentation will update automatically within 6 hours.

### Adding Processing History

When you process a dataset, **always** append to the `history` section:

```yaml
history:
  - date: 2024-01-15
    description: Initial download from CDS
    source: https://github.com/h-cel/scripts/blob/abc123/download_era5.py

  - date: 2024-02-10
    description: Regridded to 0.1° using bilinear interpolation
    source: https://github.com/h-cel/scripts/blob/def456/regrid.py
```

**Important:** Use permalinks (commit SHAs), not branch names:
- ✅ `https://github.com/org/repo/blob/abc123/script.py`
- ❌ `https://github.com/org/repo/blob/main/script.py`

## For Developers

### Improving the Automation

The automation system consists of:
- `scripts/update_site.py` - Main orchestrator
- `scripts/validate_metadata.py` - Schema validation
- `scripts/build_catalog.py` - Catalog generation
- `scripts/watch_and_update.py` - File watcher

To modify:

1. **Test your changes**:
   ```bash
   python scripts/update_site.py --dry-run
   ```

2. **Run validation tests**:
   ```bash
   python scripts/validate_metadata.py
   python scripts/build_catalog.py
   ```

3. **Check the docs build**:
   ```bash
   cd docs-site && mkdocs build --strict
   ```

### Modifying the Schema

The metadata schema is in `schema/dataset-schema.json`.

1. **Edit the schema** carefully (it's JSON Schema Draft 7)

2. **Update the template** if you add/remove fields:
   ```bash
   vim schema/metadata-template.yaml
   ```

3. **Test with existing metadata**:
   ```bash
   python scripts/validate_metadata.py
   ```

4. **Document your changes** in REFORM.md

5. **Notify dataset owners** of required changes

### Adding Documentation

Documentation lives in `docs-site/docs/`:

- `data/` - Data infrastructure docs
- `hpc/` - HPC usage guides
- `datasets/` - **Auto-generated, do not edit!**

To add new pages:

1. **Create markdown file**:
   ```bash
   vim docs-site/docs/<section>/<page>.md
   ```

2. **Add to navigation** in `docs-site/mkdocs.yml`:
   ```yaml
   nav:
     - Section:
       - Page Title: section/page.md
   ```

3. **Test locally**:
   ```bash
   cd docs-site && mkdocs serve
   ```

4. **Submit PR** with your changes

## Best Practices

### Metadata Quality

- ✅ Use **CF standard names** for variables
- ✅ Include **complete temporal coverage** (start and end dates)
- ✅ Provide **permalinks** in history.source
- ✅ Use **institutional email** for contact
- ✅ Write **descriptive** descriptions (not just the dataset name)

### File Organization

- ✅ Organize by **variable** first, then time
- ✅ Use **CF-compliant** file naming: `{variable}_{dataset}_{freq}_{period}.nc`
- ✅ Keep **metadata.yaml** at the dataset root
- ✅ Add **README.md** for complex datasets

### Version Control

- ✅ Commit **metadata changes** immediately
- ✅ Use **descriptive commit messages**
- ✅ Test **before pushing** to main
- ✅ Use **branches** for experimental changes

## Common Tasks

### Fix a validation error

```bash
# Run validation to see errors
python scripts/validate_metadata.py

# Example error:
# ✗ VSC_DATA_VO/shared/external/ERA5/metadata.yaml
#     source: 'url' is a required property

# Fix the metadata
vim VSC_DATA_VO/shared/external/ERA5/metadata.yaml

# Validate again
python scripts/validate_metadata.py
```

### Preview documentation changes

```bash
# Rebuild catalog from metadata
python scripts/build_catalog.py

# Serve locally
cd docs-site && mkdocs serve

# Open http://127.0.0.1:8000
```

### Update automation schedule

```bash
# Change cron schedule (e.g., daily at 2 AM)
CRON_SCHEDULE="0 2 * * *" bash scripts/setup_cron.sh --install
```

### Check automation logs

```bash
# View recent logs
tail -f logs/cron-update.log

# Search for errors
grep ERROR logs/cron-update.log
```

## Getting Help

- **Schema questions**: See `schema/dataset-schema.json` or `schema/metadata-template.yaml`
- **Validation errors**: Run `python scripts/validate_metadata.py` for detailed messages
- **Automation issues**: Check `logs/cron-update.log`
- **General questions**: Ask in lab meetings or open an issue

## Code of Conduct

- Be respectful of others' data and contributions
- Document your changes clearly
- Test before deploying
- Ask for help when unsure
- Share knowledge with the team

## Questions?

- See [REFORM.md](REFORM.md) for the full proposal
- Check [AUTOMATION.md](AUTOMATION.md) for automation details
- Review [STRUCTURE_DIAGRAM.md](STRUCTURE_DIAGRAM.md) for the overall structure
- Ask in lab meetings or contact the data stewardship team
