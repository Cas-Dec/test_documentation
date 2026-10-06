# Dataset metadata spec

Every dataset folder under `shared/` needs two files sitting next to the
data itself:

- **`metadata.yaml`** — machine-readable, validated against
  [`schema/dataset-schema.json`](https://github.com/h-cel/hpc-docs/blob/main/schema/dataset-schema.json)
  by `scripts/validate_metadata.py`. This is what the [data catalog](../datasets/index.md)
  is generated from.
- **`README.md`** — the same information, written for a human browsing
  the folder directly on disk.

## `metadata.yaml` fields

```yaml
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

!!! warning "The `history.source` field is not optional"
    It should always be a permalink to the exact script/commit that
    produced the data — a link to a branch will go stale. On GitHub,
    open the file at the commit you want and copy the URL; it'll contain
    the commit SHA instead of a branch name.

## Naming convention

Data files themselves follow the CF/CMOR-style pattern
`<variable>_<dataset>_<frequency>_<start>-<end>.nc`, with one subfolder
per variable, where `<variable>` is a CF short name (`tas`, `pr`,
`huss`, `sfcWind`, ...) rather than a provider-specific label. See any
dataset in the [catalog](../datasets/index.md) for a worked example.

## Validation

```bash
pip install -r docs-site/requirements.txt
python scripts/validate_metadata.py
```

This walks every `metadata.yaml` under `$VSC_DATA_VO/shared/` and checks
it against the schema, printing per-field errors for anything that
doesn't pass. On the real HPC this runs from a cron job on a schedule;
locally, run it before committing a new dataset.
