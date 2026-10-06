# Proposed VSC_DATA_VO Structure

## Visual Overview

```
$VSC_DATA_VO/  (/data/gent/vo/000/gvo00090/)
│
├── shared/                           # Lab-wide shared datasets
│   │
│   ├── external/                     # Downloaded from external sources
│   │   ├── ERA5/
│   │   │   ├── metadata.yaml        ← Required: validated metadata
│   │   │   ├── README.md            ← Optional: detailed notes
│   │   │   └── hourly/
│   │   │       ├── tas/             ← CF variable names
│   │   │       │   ├── tas_ERA5_1hr_197901-197912.nc
│   │   │       │   └── tas_ERA5_1hr_198001-198012.nc
│   │   │       ├── pr/
│   │   │       └── huss/
│   │   │
│   │   ├── CHIRPS/
│   │   │   ├── metadata.yaml
│   │   │   └── daily/
│   │   │
│   │   └── MODIS_BA/
│   │       ├── metadata.yaml
│   │       └── monthly/
│   │
│   ├── processed/                    # Processed versions of external data
│   │   └── ERA5-Land_biascorrected/
│   │       ├── metadata.yaml
│   │       └── daily/
│   │
│   ├── generated/                    # Lab-generated outputs
│   │   ├── GLEAM/
│   │   │   ├── metadata.yaml
│   │   │   └── v3.8a/
│   │   │
│   │   └── SNOWSHOP/
│   │       └── Sentinel1/
│   │           ├── metadata.yaml
│   │           └── products/
│   │
│   └── observations/                 # Observational datasets
│       └── atmospheric/
│           └── IGRA/
│               ├── metadata.yaml
│               └── stations/
│
├── projects/                         # Project-specific workspaces
│   ├── GLEAM/                        # One directory per project
│   │   ├── data/                     # Project-specific data
│   │   ├── scripts/
│   │   └── results/
│   │
│   ├── HEAT/
│   │   ├── simulations/
│   │   └── analysis/
│   │
│   └── BUCCS/
│       └── ...
│
└── personal/                         # Individual user workspaces
    ├── vsc12345/                     # Replaces scattered user dirs
    │   └── scratch/
    ├── vsc67890/
    └── ...
```

## Key Principles

### 1. Metadata-Driven Documentation

Every dataset in `shared/` requires a `metadata.yaml`:

```yaml
dataset:
  name: ERA5
  long_name: ERA5 hourly reanalysis
  description: Global atmospheric reanalysis...

source:
  provider: ECMWF
  url: https://cds.climate.copernicus.eu/...
  license: Copernicus License

coverage:
  spatial: {domain: global, resolution: 0.25°}
  temporal: {start: 1979-01-01, end: ongoing, frequency: hourly}

variables:
  - {short_name: tas, standard_name: air_temperature, units: K}

contact:
  name: Your Name
  email: your.name@ugent.be
  vsc_username: vsc12345

history:
  - date: 2024-01-15
    description: Initial download
    source: https://github.com/lab/scripts/blob/abc123/download_era5.py
```

### 2. Automated Documentation

```
metadata.yaml files
        ↓
    Validation (jsonschema)
        ↓
    Catalog Generation
        ↓
    MkDocs Site Build
        ↓
  Documentation Website
```

Triggered automatically:
- Via **cron** (every 6 hours)
- Or **file watcher** (immediate on changes)

### 3. Clear Categories

| Category | Purpose | Examples |
|----------|---------|----------|
| `external/` | Downloaded from external sources | ERA5, CHIRPS, MODIS |
| `processed/` | Modified external data | Bias-corrected, regridded |
| `generated/` | Lab-produced outputs | Model runs, derived products |
| `observations/` | Observational datasets | Weather stations, radiosonde |
| `projects/` | Project-specific work | Per-project data and code |
| `personal/` | Individual workspaces | User scratch areas |

### 4. CF-Compliant Variable Names

Use CF standard names instead of provider-specific labels:

| CF Name | Standard Name | Units | Instead of |
|---------|---------------|-------|------------|
| `tas` | air_temperature | K | t2m, temp, T2 |
| `pr` | precipitation_flux | kg m-2 s-1 | tp, precip, RAIN |
| `huss` | specific_humidity | 1 | q, QV, humidity |
| `sfcWind` | wind_speed | m s-1 | ws, WIND |

See: http://cfconventions.org/standard-names.html

### 5. Consistent File Naming

Format: `{variable}_{dataset}_{frequency}_{period}.nc`

Examples:
- `tas_ERA5_1hr_197901-197912.nc`
- `pr_CHIRPS_day_2020-2020.nc`
- `sm_GLEAM_mon_198001-202012.nc`

## Comparison: Current vs. Proposed

### Current Structure (Problems)

```
$VSC_DATA_VO/
├── CHELSA/              ← What is this? Who owns it?
├── CHIRPSv2/            ← No metadata, no docs
├── ERA5/                ← Mixed with user data below
├── flexpart_test/       ← User project? Production data?
├── vsc40023/            ← User data mixed in
├── vsc41234/
├── vsc42567/
├── SNOWSHOP/
├── DATA_TO_DELETE/      ← Unclear status
└── ...                  ← 73+ directories, no organization
```

**Issues:**
- Hard to discover datasets
- No standardized metadata
- Unclear ownership
- User data mixed with shared data
- Inconsistent naming

### Proposed Structure (Solutions)

```
$VSC_DATA_VO/
├── shared/
│   ├── external/ERA5/
│   │   └── metadata.yaml     ← Contact: vsc12345
│   ├── external/CHIRPS/
│   │   └── metadata.yaml     ← Contact: vsc67890
│   └── ...
├── projects/
│   └── flexpart_test/        ← Clearly a project
└── personal/
    ├── vsc40023/             ← User workspaces
    ├── vsc41234/
    └── ...
```

**Benefits:**
✅ Clear organization by purpose
✅ Every dataset has validated metadata
✅ Auto-generated, searchable documentation
✅ Contact info for every dataset
✅ Separation of shared vs. personal data

## Migration Strategy

1. **Symlinks preserve old paths** → minimal code changes
2. **Metadata added gradually** → dataset-by-dataset
3. **Documentation auto-updates** → always in sync
4. **Personal data moves last** → users have time to adjust

See [REFORM.md](REFORM.md) for full migration plan.
