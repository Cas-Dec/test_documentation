# MODIS_BA

*MODIS MCD64A1 Burned Area*

Monthly, global gridded burned-area product derived from combined Terra and Aqua MODIS reflectance imagery.

## Details

| | |
|---|---|
| **Category** | `external` |
| **Version** | 6.1 |
| **Provider** | NASA LP DAAC |
| **License** | NASA EOSDIS Data Use Policy |
| **Source URL** | https://lpdaac.usgs.gov/products/mcd64a1v061/ |
| **DOI** | 10.5067/MODIS/MCD64A1.061 |
| **Spatial domain** | global |
| **Spatial resolution** | 500 m |
| **Temporal coverage** | 2000-03-01 to 2024-12-31 |
| **Frequency** | monthly |
| **Contact** | John Smith (john.smith@ugent.be, vsc46240) |
| **Path** | `VSC_DATA_VO/shared/external/MODIS_BA` |

## Variables

| short_name | standard_name | units |
|---|---|---|
| `ba` | burned_area_fraction | 1 |

## Processing history

- **2026-07-02** — Download, reprojection to regular lat/lon grid, and conversion to CF-compliant NetCDF ([source](https://github.com/h-cel/data-pipelines/blob/6b7e2d1/modis_ba/process_modis_ba.py))
