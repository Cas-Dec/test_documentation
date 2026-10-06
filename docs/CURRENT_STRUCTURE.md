# Current VSC_DATA_VO Structure Survey

**Date:** 2026-09-30
**Path:** `/data/gent/vo/000/gvo00090`

## Summary Statistics

- **Project/Dataset folders:** 18
- **User directories (vsc*):** 73
- **Special directories:** 3 (tools, restores, GUESTSHARED)

## Directory Inventory

### Projects & Datasets

| Directory | Owner | Group | Last Modified | Subdirs | Proposed Category |
|-----------|-------|-------|---------------|---------|-------------------|
| BUCCS | vsc45925 | 2542247 | 2023-03-04 | ec2caf, nccd, scripts | `projects/BUCCS/internal/` |
| CSNOW | vsc42513 | gvo00090 | 2023-02-08 | matlab | `projects/CSNOW/internal/` |
| D2D | vsc45925 | 2640220 | 2023-06-23 | archive, data, log, scripts, software | `projects/D2D/internal/` |
| ERA-5Land | vsc48989 | vsc48989 | 2025-10-13 | South America | `shared/external/ERA5-Land/` |
| EXT | vsc45925 | gvo00090 | 2024-08-16 | archive, data, scripts, software | **Migrate contents to `shared/external/`** |
| FLEXPART | vsc45925 | 2640367 | 2023-09-14 | forcing, hamster, observations, simulations, tools, versions | `shared/generated/FLEXPART/` |
| Forcings | vsc45264 | vsc45264 | 2025-09-05 | job_logs | `shared/generated/Forcings/` or `projects/Forcings/internal/` |
| GLEAM | vsc45925 | ggleam | 2026-04-21 | data, ET-SENSE, GLANCE, GLEAM4_outputs, gleam-hr, GLEAM-Hybrid, GLEAM-PIE, HERMES, scripts | `shared/generated/GLEAM/` + `projects/GLEAM/shared` symlink |
| GLEAM_Europe | vsc45925 | 2541461 | 2019-11-20 | agg, frac | `shared/generated/GLEAM_Europe/` |
| GUESTSHARED | vsc42145 | vsc42145 | 2026-09-22 | PROBEX | **Keep as-is at VO level** |
| HEAT | vsc45925 | gvo00090 | 2026-09-24 | Data, download_scripts, Preds, stats | `projects/HEAT/internal/` |
| LCZEU | vsc45925 | gvo00090 | 2023-01-10 | software | `projects/LCZEU/internal/` |
| MODIS_BA | vsc48989 | vsc48989 | 2025-10-03 | Global | `shared/external/MODIS_BA/` |
| SNOWSHOP | vsc40471 | gvo00090 | 2026-07-24 | AlphaEarth, auxdata, Forcings, Lidar, measurements, PMW_SWE, pythonenv, Sentinel1, .snap, Snowclim, Snowclim_FMI, snowcover, wavetrax, WetSnow | `projects/SNOWSHOP/internal/` |
| SUBLIME | vsc45925 | gsublime | 2017-10-25 | archive, data, scripts, software | `projects/SUBLIME/internal/` |
| WAVETRAX | vsc42654 | vsc42654 | 2024-12-07 | Test_Example_SubDailyGLEAM_hpc, Test_Example_SubDailyGLEAM_local, Thesis_Emma | `projects/WAVETRAX/internal/` |
| restores | vsc45925 | gvo00090 | 2024-02-21 | — | **Keep as-is at VO level** |
| tools | vsc45925 | 2640367 | 2021-12-23 | — | **Keep as-is at VO level** |

### User Directories (vsc*)

**Total count:** 73 user directories
**Sample:** vsc10524, vsc40149, vsc40471, vsc40846, vsc40866, vsc41461, vsc41839, vsc41843, vsc41917, vsc42145, vsc42244, vsc42247, vsc42248, vsc42294, vsc42295, vsc42296, vsc42383, vsc42444, vsc42513, vsc42561, vsc42563, vsc42634, vsc42654, vsc42663, vsc42724, vsc42736, vsc42776, vsc43087, vsc43092, vsc43205, vsc43350, vsc43482, vsc43600, vsc43614, vsc43632, vsc43765, vsc43863, vsc44191, vsc44251, vsc44255, vsc44412, vsc44798, vsc44801, vsc44942, vsc44965, vsc45264, vsc45400, vsc45406, vsc45429, vsc45925, vsc46060, vsc46187, vsc46240, vsc46263, vsc46271, vsc46292, vsc46941, vsc47870, vsc47903, vsc47934, vsc47942, vsc48498, vsc48989, vsc49513, vsc49672, vsc49764, vsc49964, vsc50314, vsc50377, vsc50750, vsc50813, vsc52101, vsc52121

**Proposed migration:** `personal/<vsc_username>/`

## Classification Logic

### `shared/external/`
**Raw datasets from external providers, unchanged**
- ERA-5Land (already started)
- MODIS_BA (already started)
- Contents of EXT/ (to be migrated)

### `shared/processed/`
**Derived from external data, useful across teams**
- (TBD - needs lab input on which datasets qualify)

### `shared/generated/`
**In-house products used by multiple teams**
- GLEAM (main output)
- GLEAM_Europe (regional variant)
- FLEXPART (model output)
- Forcings (if cross-team; otherwise project-specific)

### `projects/<name>/internal/`
**Project-specific data, no metadata required**
- BUCCS
- CSNOW
- D2D
- HEAT
- LCZEU
- SNOWSHOP
- SUBLIME
- WAVETRAX
- Forcings (if single-team only)

### Keep at VO top level
**Special-purpose, not subject to reform**
- tools (shared scripts/binaries)
- restores (backup/restore area)
- GUESTSHARED (external collaboration space)

### `personal/<vsc_username>/`
**All 73 existing vsc* directories**

## Questions Requiring Lab Input

1. **EXT contents**: What datasets are in EXT/data/? Need to inventory and migrate each to appropriate `shared/external/<dataset>/` folder
2. **Forcings**: Single-team or cross-team? Determines `shared/generated/` vs `projects/<name>/internal/`
3. **GLEAM structure**: Confirm which subdirs (GLEAM4_outputs, GLEAM-Hybrid, GLEAM-PIE, HERMES, etc.) should be:
   - Part of canonical `shared/generated/GLEAM/`
   - Kept in `projects/GLEAM/internal/`
4. **Active vs archived projects**: Are D2D, BUCCS, LCZEU, SUBLIME still active? If archived, different handling?
5. **WAVETRAX**: Recent (2024), but appears to be thesis-specific - confirm project vs personal classification
6. **Group ownership**: Several folders have custom groups (ggleam, gsublime, 2640220, etc.) - maintain these post-reform?

## Next Steps

1. **Deep dive on EXT/**: Survey its contents to create migration plan
2. **GLEAM inventory**: Document current structure and decide canonical vs internal split
3. **Contact project leads**: Verify classification for each project folder
4. **Draft migration timeline**: Prioritize by activity level and dependencies
