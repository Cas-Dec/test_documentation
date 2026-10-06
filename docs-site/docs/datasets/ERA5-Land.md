# ERA5-Land

*ERA5-Land hourly reanalysis*

ECMWF's land-surface reanalysis, replaying the land component of ERA5 at higher spatial resolution, providing hourly estimates of land-surface variables from 1950 to present.

## Details

| | |
|---|---|
| **Category** | `external` |
| **Version** | 1 |
| **Provider** | ECMWF / Copernicus Climate Change Service (C3S) |
| **License** | Copernicus License |
| **Source URL** | https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land |
| **DOI** | 10.24381/cds.e2161bac |
| **Spatial domain** | global (land only) |
| **Spatial resolution** | 0.1° |
| **Temporal coverage** | 1950-01-01 to ongoing |
| **Frequency** | hourly |
| **Contact** | Jane Doe (jane.doe@ugent.be, vsc10520) |
| **Path** | `VSC_DATA_VO/shared/external/ERA5-Land` |

## Variables

| short_name | standard_name | units |
|---|---|---|
| `tas` | air_temperature | K |
| `pr` | precipitation_flux | kg m-2 s-1 |

## Processing history

- **2026-08-20** — Initial download and conversion to CF-compliant NetCDF, split per variable ([source](https://github.com/h-cel/data-pipelines/blob/9a1c3f0/era5-land/download_era5land.py))
