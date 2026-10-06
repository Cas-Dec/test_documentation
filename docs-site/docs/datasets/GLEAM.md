# GLEAM

*Global Land Evaporation Amsterdam Model output*

Daily terrestrial evaporation estimates produced in-house by running the GLEAM model, forced with a mix of reanalysis and satellite observations. Used across multiple projects, so it lives in shared/generated rather than a single project folder.

## Details

| | |
|---|---|
| **Category** | `generated` |
| **Version** | 4.2a |
| **Provider** | h-cel (internally generated, based on the GLEAM model) |
| **License** | internal use — ask contact before external sharing |
| **Source URL** | https://www.gleam.eu/ |
| **DOI** | - |
| **Spatial domain** | global |
| **Spatial resolution** | 0.25° |
| **Temporal coverage** | 1980-01-01 to 2023-12-31 |
| **Frequency** | daily |
| **Contact** | Alex Janssens (alex.janssens@ugent.be, vsc46250) |
| **Path** | `VSC_DATA_VO/shared/generated/GLEAM` |

## Variables

| short_name | standard_name | units |
|---|---|---|
| `E` | water_evaporation_flux | mm d-1 |

## Processing history

- **2026-06-10** — Model run v4.2a over 1980-2023, forced with ERA5-Land and MSWEP ([source](https://github.com/h-cel/gleam-runs/blob/4f0a9c2/run_gleam_v4.2a.py))
