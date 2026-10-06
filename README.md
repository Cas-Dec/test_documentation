# test_documentation
Repo to test MkDocs for internal documentation 

<<<<<<< HEAD
To create this site, following guides were used:

- https://squidfunk.github.io/mkdocs-material/getting-started/
- https://squidfunk.github.io/mkdocs-material/creating-your-site/
- https://squidfunk.github.io/mkdocs-material/publishing-your-site/ 

## For developpers

With conda, install the computational environment:
```
conda env create -f environment.yml
conda activate test_documentation
```

You can now test if mkdocs is installed by e.g. running:
```
mkdocs --version
```

=======
**Goal:** Create a well-organized, self-documenting data infrastructure for the H-CEL lab on the VSC HPC cluster.

This repository implements a new structure for `$VSC_DATA_VO` (`/data/gent/vo/000/gvo00090`) with:
- **Standardized metadata** for all datasets (validated against JSON schema)
- **Automated documentation** that stays in sync with the actual data
- **Clear folder structure** separating external data, processed data, projects, and personal files

## Quick Links

- **[QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md)** - One-page cheat sheet 📋
- **[STRUCTURE_DIAGRAM.md](docs/STRUCTURE_DIAGRAM.md)** - Visual overview of the proposed structure ⭐ Start here!
- **[CONTRIBUTING.md](docs/CONTRIBUTING.md)** - How to add/update datasets
- **[QUICKSTART_AUTOMATION.md](docs/QUICKSTART_AUTOMATION.md)** - Set up automated docs
- **[AUTOMATION.md](docs/AUTOMATION.md)** - Complete automation documentation
- **[REFORM.md](docs/REFORM.md)** - Full proposal and rationale
- **[CURRENT_STRUCTURE.md](docs/CURRENT_STRUCTURE.md)** - Current VSC_DATA_VO inventory

## Why This Reform?

### Current Problems
- Hard to discover what datasets exist on `$VSC_DATA_VO`
- No standardized metadata or documentation
- Unclear ownership and contact info
- Inconsistent naming conventions
- User data mixed with shared datasets

### Our Solution
1. **Organized structure**: `shared/`, `projects/`, `personal/` top-level folders
2. **Metadata files**: Every dataset has a `metadata.yaml` with schema validation
3. **Auto-generated docs**: Documentation site updates automatically when data changes
4. **Clear conventions**: CF-compliant variable names, standardized file naming

## Repository Contents

### Core Directories

- **`VSC_DATA_VO/`** - Example of the proposed structure
  - `shared/external/` - Downloaded datasets (ERA5, CHIRPS, MODIS, etc.)
  - `shared/processed/` - Datasets that have been processed/modified
  - `shared/generated/` - Model outputs and lab-generated data
  - `shared/observations/` - Observational data
  - `projects/` - Project-specific workspaces
  - `personal/` - Individual user scratch spaces

- **`docs-site/`** - Documentation website (MkDocs)
  - `docs/datasets/` - Auto-generated dataset catalog (don't edit manually!)
  - `docs/data/` - Data infrastructure documentation
  - `docs/hpc/` - HPC usage guides

- **`scripts/`** - Automation tools
  - `update_site.py` - Main automation orchestrator
  - `validate_metadata.py` - Schema validation
  - `build_catalog.py` - Generate dataset catalog
  - `setup_cron.sh` - Install/manage cron jobs
  - `watch_and_update.py` - Real-time file watcher

- **`schema/`** - JSON schema for metadata.yaml validation

### Documentation Files

- **`REFORM.md`** - Complete proposal with rationale and examples
- **`CURRENT_STRUCTURE.md`** - Inventory of current VSC_DATA_VO (as of 2026-09-30)
- **`AUTOMATION.md`** - How automated documentation works
- **`QUICKSTART_AUTOMATION.md`** - Quick setup guide
- **Inventory files** (`*_INVENTORY.md`) - Detailed surveys of specific datasets

## Getting Started

### For Lab Members: Using the Documentation

1. **Browse datasets**: Visit the documentation site (link TBD when deployed)
2. **Find what you need**: Search by category, variable, or dataset name
3. **Check metadata**: Each dataset page shows contact, coverage, variables, and path
4. **Contact the owner**: Metadata includes who to reach for questions

### For Data Stewards: Adding a New Dataset

1. **Organize your data** following the proposed structure:
   ```
   $VSC_DATA_VO/shared/<category>/<dataset_name>/
   ```

2. **Create metadata.yaml** (see [schema/dataset-schema.json](schema/dataset-schema.json)):
   ```bash
   # Copy template
   cp schema/metadata-template.yaml $VSC_DATA_VO/shared/<category>/<dataset>/metadata.yaml

   # Edit to fill in your dataset info
   vim $VSC_DATA_VO/shared/<category>/<dataset>/metadata.yaml
   ```

3. **Validate metadata**:
   ```bash
   python scripts/validate_metadata.py
   ```

4. **Documentation updates automatically** (if cron is set up)
   - Or trigger manually: `python scripts/update_site.py --commit`

### For Admins: Setting Up Automation

**Quick setup:**
```bash
# Test the automation
bash scripts/setup_cron.sh --test

# Install cron job (updates every 6 hours)
bash scripts/setup_cron.sh --install

# Check it's running
bash scripts/setup_cron.sh --check
```

See [QUICKSTART_AUTOMATION.md](docs/QUICKSTART_AUTOMATION.md) for details.

## How It Works

### The Metadata System

Every dataset under `$VSC_DATA_VO/shared/` has a `metadata.yaml` file describing:
- **Dataset info**: name, description, version
- **Source**: provider, license, DOI
- **Coverage**: spatial/temporal extent, resolution
- **Variables**: CF-compliant variable names and units
- **Contact**: who manages this dataset
- **History**: provenance tracking with script links

Example:
```yaml
dataset:
  name: ERA5
  long_name: ERA5 hourly reanalysis on single levels
  description: Global atmospheric reanalysis from ECMWF...

source:
  provider: ECMWF
  url: https://cds.climate.copernicus.eu/...
  license: Copernicus License

coverage:
  spatial:
    domain: global
    resolution: 0.25°
  temporal:
    start: 1979-01-01
    end: ongoing
    frequency: hourly

contact:
  name: Your Name
  email: your.name@ugent.be
  vsc_username: vsc12345
```

### The Automation Pipeline

1. **Scan**: Finds all `metadata.yaml` files under `$VSC_DATA_VO/shared/`
2. **Validate**: Checks against JSON schema using `jsonschema`
3. **Detect changes**: Tracks added/moved/deleted datasets
4. **Generate docs**: Creates dataset catalog pages from valid metadata
5. **Build site**: Regenerates MkDocs static site
6. **Commit**: Pushes changes to git (optional)
7. **Notify**: Emails contacts on validation errors (optional)

Runs automatically via cron (default: every 6 hours) or in real-time via file watcher.

## Example Workflows

### Viewing the Documentation Locally

```bash
# Install dependencies
pip install -r requirements-automation.txt

# Build and serve
cd docs-site
mkdocs serve
# Open http://127.0.0.1:8000
```

### Manually Updating the Documentation

```bash
# Validate all metadata
python scripts/validate_metadata.py

# Rebuild catalog
python scripts/build_catalog.py

# Build site
cd docs-site && mkdocs build
```

### Testing Before Migration

See `VSC_SCRATCH_USER/example_project/` for code migration examples:
```bash
cd VSC_SCRATCH_USER/example_project
./setup_symlinks.sh          # creates symlinks to new structure
python after/read_gleam_symlink.py
```

Most code changes are absorbed by symlinks; some require path updates.

## Current vs. Proposed Structure

**Current structure** ([CURRENT_STRUCTURE.md](docs/CURRENT_STRUCTURE.md)):
- 18 project/dataset folders at various locations
- 73 user directories mixed with shared data
- Inconsistent naming and organization

**Proposed structure** (this repo):
```
$VSC_DATA_VO/
├── shared/
│   ├── external/       # Downloaded datasets (ERA5, CHIRPS, etc.)
│   ├── processed/      # Modified versions of external data
│   ├── generated/      # Model outputs, lab-generated data
│   └── observations/   # Observational datasets
├── projects/           # Project-specific workspaces
└── personal/           # Individual user scratch (replaces scattered vsc* dirs)
```

Each dataset in `shared/` has:
- `metadata.yaml` (required, validated)
- `README.md` (optional, detailed notes)
- Data organized by variable and temporal frequency

## Status & Next Steps

**✅ Completed:**
- Metadata schema definition
- Validation scripts with `jsonschema`
- Automated catalog generation
- Cron-based automation
- Real-time file watching option
- Documentation site framework

**🚧 In Progress:**
- Current structure inventory and migration mapping
- Testing with lab members
- Documentation site deployment

**📋 To Do:**
- Migrate existing datasets to new structure
- Set up production cron job
- Deploy documentation site
- Email notification system
- Training session for lab members

## FAQ

**Q: Do I need to reorganize my existing data immediately?**
A: No. This is a proposed structure. Migration will be coordinated and gradual.

**Q: What if my dataset doesn't fit the categories?**
A: Contact the admin team. We can discuss adding new categories or special cases.

**Q: Can I still use my personal `vsc*` directory?**
A: Yes, but it will eventually move to `$VSC_DATA_VO/personal/vsc*/` for better organization.

**Q: What happens if my metadata.yaml has errors?**
A: The validation script will tell you exactly what's wrong. The site builds from valid metadata only; invalid datasets are logged and you'll be notified.

**Q: How do I update my dataset's metadata?**
A: Edit the `metadata.yaml` file. If automation is enabled, docs update automatically within 6 hours (or immediately with the file watcher).

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed instructions on:
- Adding new datasets
- Updating metadata
- Improving automation
- Contributing documentation

Quick links:
- **Report issues**: Open an issue in this repository
- **Suggest improvements**: Edit REFORM.md or open a discussion
- **Add documentation**: Submit PRs with improvements
- **Help migrate data**: Contact the data stewardship team

## Support

- **Technical issues**: Check logs in `logs/cron-update.log`
- **Metadata questions**: See [schema/dataset-schema.json](schema/dataset-schema.json)
- **Migration help**: See [REFORM.md](docs/REFORM.md) or ask in lab meetings
- **Automation setup**: See [AUTOMATION.md](docs/AUTOMATION.md)
>>>>>>> 582d8bc (Add complete documentation automation system)
