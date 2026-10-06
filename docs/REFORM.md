# Data & Documentation Reform

Notes and proposal for reforming how we document datasets and shared data on the HPC (VSC), based on the current example site: https://h-cel.github.io/test_documentation/

## 1. Metadata per dataset

### Conventions options

- Try to adhere to **CF conventions** where possible, e.g. see this intro: https://how-to-create-publishable-netcdf-data-6d8371.pages.rwth-aachen.de/PART2_Introduction_CF_Conventions.html
- Most full-fledged option: a **STAC catalog** (https://stacspec.org/en/tutorials/2-create-stac-catalog-python/) — a lot of work though, likely overkill for now.
- **Important:** the `history` field should *always* contain a link to the file/script where the data download or processing happens — preferably a permalink to a specific git commit, not just a branch.

### Practical approach

- A standard **YAML file** to fill in per dataset.
  - Could include a fixed field for the **contact person**: who to reach out to if something is unclear about the data.
- **Validation** of the YAML against a schema, e.g. using [`jsonschema`](https://github.com/python-jsonschema/jsonschema/).

### Example: `external/` folder layout

Each dataset gets its own folder with a `README.md` and a `metadata.yaml`, sitting next to the data itself. NetCDF files follow the CF/CMOR-style naming convention `<variable>_<dataset>_<frequency>_<start>-<end>.nc`, where `<variable>` is a CF short name (`tas`, `pr`, `huss`, `sfcWind`, ...) rather than a provider-specific label.

```text
$VSC_DATA_VO/shared/external/
├── ERA5/
│   ├── README.md
│   ├── metadata.yaml
│   └── hourly/
│       ├── tas/                  # air_temperature
│       │   ├── tas_ERA5_1hr_197901-197912.nc
│       │   └── tas_ERA5_1hr_198001-198012.nc
│       ├── pr/                   # precipitation_flux
│       │   └── pr_ERA5_1hr_197901-197912.nc
│       ├── huss/                 # specific_humidity
│       │   └── huss_ERA5_1hr_197901-197912.nc
│       └── sfcWind/               # wind_speed
│           └── sfcWind_ERA5_1hr_197901-197912.nc
├── MSWEP/
│   ├── README.md
│   ├── metadata.yaml
│   └── daily/
│       └── pr/                   # precipitation_flux
│           └── pr_MSWEP_day_197901-202312.nc
└── MODIS_LST/
    ├── README.md
    ├── metadata.yaml
    └── daily/
        └── ts/                    # surface_temperature
            └── ts_MODIS_day_200003-202412.nc
```

### Example: standard `metadata.yaml`

Every dataset folder gets one of these, validated against a shared JSON schema. This is the field-by-field template:

```yaml
# metadata.yaml — one per dataset, lives in $VSC_DATA_VO/shared/external/<dataset>/
dataset:
  name: ""                # short identifier, matches folder name
  long_name: ""            # human-readable full name
  version: ""              # dataset release version, if applicable
  description: ""          # 1-3 sentences on what this data is

source:
  provider: ""             # e.g. ECMWF, NASA, KU Leuven
  url: ""                  # link to the original data source / portal
  doi: ""                  # if available
  license: ""              # usage license / restrictions

coverage:
  spatial:
    domain: ""             # e.g. "global", "Europe", bounding box
    resolution: ""         # e.g. "0.25°", "9 km"
  temporal:
    start: ""              # YYYY-MM-DD
    end: ""                # YYYY-MM-DD or "ongoing"
    frequency: ""          # e.g. "hourly", "daily", "monthly"

variables:                  # one entry per CF variable, matches subfolder names
  - short_name: ""          # CF/CMOR short name, e.g. "tas"
    standard_name: ""       # CF standard_name, e.g. "air_temperature"
    units: ""                # CF/UDUNITS-compliant units, e.g. "K"

contact:
  name: ""                  # person responsible for this dataset
  email: ""                 # institutional email
  vsc_username: ""

history:                    # append-only log of processing steps
  - date: ""                # YYYY-MM-DD
    description: ""         # what was done (download, regrid, bias-correction, ...)
    source: ""               # permalink to the exact script/commit that produced this
```

### Example: filled-in `metadata.yaml` (ERA5)

```yaml
dataset:
  name: ERA5
  long_name: ERA5 hourly reanalysis on single levels
  version: "1"
  description: >
    ECMWF's fifth-generation atmospheric reanalysis, providing hourly
    estimates of a large number of atmospheric, land, and oceanic variables.

source:
  provider: ECMWF / Copernicus Climate Change Service (C3S)
  url: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels
  doi: 10.24381/cds.adbb2d47
  license: Copernicus License

coverage:
  spatial:
    domain: global
    resolution: "0.25°"
  temporal:
    start: "1940-01-01"
    end: ongoing
    frequency: hourly

variables:
  - short_name: tas
    standard_name: air_temperature
    units: K
  - short_name: pr
    standard_name: precipitation_flux
    units: kg m-2 s-1
  - short_name: huss
    standard_name: specific_humidity
    units: "1"
  - short_name: sfcWind
    standard_name: wind_speed
    units: m s-1

contact:
  name: Jane Doe
  email: jane.doe@ugent.be
  vsc_username: vsc12345

history:
  - date: "2026-08-15"
    description: Initial download and conversion to CF-compliant NetCDF
    source: https://github.com/h-cel/data-pipelines/blob/3f2a1c9/era5/download_era5.py
```

### Example: companion `README.md`

A short, human-facing summary of the same information, for anyone browsing the folder directly:

```markdown
# ERA5

ECMWF's fifth-generation atmospheric reanalysis (hourly, global, 0.25°),
covering 1940-present.

- **Source:** Copernicus Climate Change Service (C3S) — [CDS portal](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels)
- **License:** Copernicus License
- **Variables:** `tas` (air temperature), `pr` (precipitation flux),
  `huss` (specific humidity), `sfcWind` (wind speed)
- **Contact:** Jane Doe (jane.doe@ugent.be, vsc12345)

See `metadata.yaml` in this folder for full CF-compliant metadata and
processing history.
```

### Automation

- Schedule a scan of all data folders (e.g. every 24 hours):
  1. **Task 1** — update the list of available data on the documentation website.
  2. **Task 2** — if a dataset does not follow the correct structure, contact the person who created the file/folder.
     - Requires a maintained list linking VSC usernames to email addresses.
- **Problem:** GitHub Actions won't work here — no access to the HPC from GitHub-hosted runners.
- **Alternative:** a cron job on the HPC that opens a pull request on the repo (which then needs to be reviewed).
  - Tried `scrontab`, but it's disabled on this cluster (`scrontab: fatal: scrontab is disabled on this cluster`).
  - Standard `crontab` does seem to be available — use that instead.

## 2. Location

### GitHub (h-cel)

- Allows for automation and control over who can write what.
- Pure `.md` files.
- **Static site generator options:**
  - [`mkdocs-material`](https://github.com/squidfunk/mkdocs-material) — used in the current example docs, but will no longer be maintained.
  - Consider switching to [Zensical](https://github.com/zensical/zensical).
  - Other options: Quarto, Sphinx.
- **Hosting:** GitHub Pages.
  - Free if the documentation is public — done by several other teams already:
    - https://github.com/KUL-RSDA/documentation/tree/master
    - https://github.com/qforestlab
  - Private repos require paying for GitHub Pages hosting.

### SharePoint

- Main disadvantage: hard to automate a data catalog here.

## 3. Folder structure

Keep it simple — inspiration from the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/#directory-structure) layout.

Shared data lives under `$VSC_DATA_VO/shared`, alongside a `personal/` space for team-member-specific work:

- **`external/`** — the current `EXT` data; only raw datasets, without any processing.
- **`processed/`** — output of processing steps applied to external data, but still deemed useful for everyone.
- **`generated/`** — data generated internally that is used across teams (GLEAM, FLEXPART, ...). Note: these can just be symlinks into team-specific folders.

```text
$VSC_DATA_VO/
├── shared/
│   ├── external/        # raw datasets, no processing (current EXT data)
│   ├── processed/        # processed from external data, useful for everyone
│   └── generated/        # internally generated, used across teams
│       ├── GLEAM/
│       ├── FLEXPART/
│       └── ...
├── projects/
│   ├── GLEAM/
|   |   ├── internal/
|   |   └── shared/ -> /path/to/team/gleam/folder      (symlink)
│   ├── FLEXPART/
|   └── ...
└── personal/
    ├── <vsc_username_1>/
    ├── <vsc_username_2>/
    └── ...
```

## 4. Other documentation

Useful categories to cover on the site beyond dataset metadata:

- HPC (general usage, VSC-specific tips)
- Model guides: GLEAM, WRF, FLEXPART, ...
- ...
