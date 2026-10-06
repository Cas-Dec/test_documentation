# ERA5-Land_biascorrected

*ERA5-Land daily temperature, bias-corrected against station observations*

Daily-aggregated ERA5-Land air temperature, bias-corrected with a quantile-mapping approach against RMI station observations. Produced from shared/external/ERA5-Land — kept here because the correction is generic and useful beyond the project that first needed it.

## Details

| | |
|---|---|
| **Category** | `processed` |
| **Version** | 1 |
| **Provider** | h-cel (derived product) |
| **License** | Copernicus License (inherited from ERA5-Land) |
| **Source URL** | https://github.com/h-cel/data-pipelines/tree/main/era5-land |
| **DOI** | - |
| **Spatial domain** | Belgium |
| **Spatial resolution** | 0.1° |
| **Temporal coverage** | 1979-01-01 to 2023-12-31 |
| **Frequency** | daily |
| **Contact** | Jane Doe (jane.doe@ugent.be, vsc10520) |
| **Path** | `VSC_DATA_VO/shared/processed/ERA5-Land_biascorrected` |

## Variables

| short_name | standard_name | units |
|---|---|---|
| `tas` | air_temperature | K |

## Processing history

- **2026-08-20** — Source data ingested (see shared/external/ERA5-Land/metadata.yaml) ([source](https://github.com/h-cel/data-pipelines/blob/9a1c3f0/era5-land/download_era5land.py))
- **2026-08-28** — Daily aggregation and quantile-mapping bias correction against RMI stations ([source](https://github.com/h-cel/data-pipelines/blob/2d4f8ab/era5-land/biascorrect_era5land.py))
