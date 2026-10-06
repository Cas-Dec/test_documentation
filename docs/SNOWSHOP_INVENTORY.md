# SNOWSHOP/ Structure Inventory

**Path:** `/data/gent/vo/000/gvo00090/SNOWSHOP/`
**Owner:** vsc40471 (primary), Group: gvo00090
**Purpose:** Snow monitoring and analysis using satellite data (Sentinel-1, Lidar, passive microwave)
**Last Modified:** 2026-07-24

## Directory Structure

| Subdirectory | Owner | Last Modified | Size/Files | Type | Proposed Location |
|--------------|-------|---------------|------------|------|-------------------|
| **Sentinel1/** | vsc40471 | 2025-11-12 | 4949 subdirs + 256K tarballs | SAR snow data | `shared/generated/SNOWSHOP/Sentinel1/` or `projects/SNOWSHOP/Sentinel1/` |
| **Forcings/** | vsc45264 | 2025-11-18 | Alps, Andes, NoSeFi | Meteorological forcing | `projects/SNOWSHOP/forcings/` |
| **Snowclim/** | vsc45264 | 2025-11-18 | 6 subdirs | Snow climatology | `shared/generated/SNOWSHOP/Snowclim/` |
| **Snowclim_FMI/** | vsc40471 | 2026-04-28 | 5 subdirs | FMI snow climate data | `shared/external/FMI/snowclim/` |
| **Lidar/** | vsc40471 | 2025-04-18 | 6 subdirs | Lidar snow measurements | `shared/observations/lidar/snow/` |
| **PMW_SWE/** | vsc40471 | 2025-03-20 | 4 subdirs | Passive microwave snow water equivalent | `shared/generated/SNOWSHOP/PMW_SWE/` |
| **WetSnow/** | vsc44965 | 2026-02-27 | 2 subdirs | Wet snow detection | `projects/SNOWSHOP/WetSnow/` |
| **AlphaEarth/** | vsc44965 | 2025-07-24 | 4 subdirs | ML embeddings | `projects/SNOWSHOP/AlphaEarth/` |
| **measurements/** | vsc40471 | 2026-01-09 | 7 subdirs | In-situ measurements | `shared/observations/ground/snow/` |
| **auxdata/** | vsc40471 | 2025-09-17 | 7 subdirs | Auxiliary data | `projects/SNOWSHOP/auxdata/` |
| **snowcover/** | vsc40471 | 2026-01-09 | 7 subdirs | Snow cover products | `shared/generated/SNOWSHOP/snowcover/` |
| **wavetrax/** | vsc40471 | 2025-04-30 | 4 subdirs | Related project | Link to separate `WAVETRAX/`? |
| **pythonenv/** | vsc40471 | 2024-07-15 | - | Python environment | `projects/SNOWSHOP/env/` (or remove) |
| **.snap/** | vsc40471 | 2024-07-17 | - | SNAP toolbox cache | Can be removed |

## Detailed Analysis

### 1. **Sentinel1/** → Large-scale SAR Processing Hub
- **Type:** Sentinel-1 SAR data processing for snow applications
- **Structure:**
  - `SNAPPY/` - 13 subdirs - ESA SNAP Python interface results
  - `SNAPPY_asfsearch/` - 5 subdirs - Alaska Satellite Facility data
  - `g0_100m/` - **4949 subdirs** - Massive processed dataset at 100m resolution
  - `g0_100m_tar/` - 256K directory - Compressed archives
  - `g0_100m_tmp/`, `g0_100m_untar/` - Processing temp directories
  - `S1_ASF_dwnld/` - 4M directory - Downloaded raw Sentinel-1 scenes
  - `SD_RETRIEVAL/` - Snow depth retrieval algorithms (Apr 2025)
- **Status:** Very active - continuous processing through 2025-2026
- **Size:** Extremely large (4949 processed tiles suggests continental scale)
- **Classification:** Major data product, likely multi-user resource
- **Migration:**
  - If cross-team → `shared/generated/SNOWSHOP/Sentinel1/`
  - Consider archiving `g0_100m_tar/` and temp directories
  - Keep active processing (`g0_100m/`) and retrieval algorithms

### 2. **Forcings/** → Regional Meteorological Data
- **Type:** Meteorological forcing data for snow models
- **Structure:**
  - `Alps/` - 5 subdirs (Aug 2025)
  - `Andes/` - (Aug 2025)
  - `NoSeFi/` - Nordic/Scandinavia/Finland? (Aug 2025)
- **Status:** Recently updated (Aug 2025), active
- **Users:** vsc45264
- **Migration:** `projects/SNOWSHOP/forcings/` - project-specific extracts

### 3. **Snowclim/** → Snow Climatology Product
- **Type:** Derived snow climatology (6 subdirs)
- **Last modified:** Nov 2025
- **Users:** vsc45264
- **Migration:**
  - If published/shared product → `shared/generated/SNOWSHOP/Snowclim/`
  - If internal → `projects/SNOWSHOP/Snowclim/`

### 4. **Snowclim_FMI/** → External FMI Data
- **Type:** Finnish Meteorological Institute snow climate data
- **Last modified:** Apr 2026 - very recent!
- **Migration:** `shared/external/FMI/snowclim/` - external dataset
- **Note:** Should have metadata.yaml with source info

### 5. **Lidar/** → Lidar Snow Measurements
- **Type:** Airborne/satellite lidar observations (6 subdirs)
- **Last modified:** Apr 2025
- **Migration:** `shared/observations/lidar/snow/`
- **Classification:** Observational data, likely valuable for multiple projects

### 6. **PMW_SWE/** → Passive Microwave Snow Water Equivalent
- **Type:** SWE retrievals from passive microwave (4 subdirs)
- **Last modified:** Mar 2025
- **Migration:**
  - If original product → `shared/generated/SNOWSHOP/PMW_SWE/`
  - If downloaded → `shared/external/PMW/SWE/`

### 7. **WetSnow/** → Wet Snow Detection
- **Type:** Wet snow detection algorithm/outputs (2 subdirs)
- **Last modified:** Feb 2026 - recent!
- **Users:** vsc44965
- **Migration:** `projects/SNOWSHOP/WetSnow/` - active research

### 8. **AlphaEarth/** → Machine Learning Embeddings
- **Type:** ML-based Earth system embeddings (4 subdirs)
- **Last modified:** Jul 2025
- **Users:** vsc44965
- **Note:** May relate to `EXT/alpha_earth_embeddings/`
- **Migration:** `projects/SNOWSHOP/AlphaEarth/` or link to EXT/

### 9. **measurements/** → In-Situ Observations
- **Type:** Ground measurements, field data (7 subdirs)
- **Last modified:** Jan 2026 - very recent
- **Migration:** `shared/observations/ground/snow/`
- **Classification:** Observational data - valuable for validation

### 10. **snowcover/** → Snow Cover Products
- **Type:** Snow cover mapping/classification (7 subdirs)
- **Last modified:** Jan 2026 - very recent
- **Migration:** `shared/generated/SNOWSHOP/snowcover/`

### 11. **wavetrax/** → Related Project
- **Type:** Related to separate WAVETRAX directory
- **Note:** `/data/gent/vo/000/gvo00090/WAVETRAX/` exists (vsc42654)
- **Migration:** Create symlink or consolidate under WAVETRAX

### 12. **auxdata/** → Auxiliary Data
- **Type:** Supporting datasets (DEM, land cover, etc.)
- **Migration:** `projects/SNOWSHOP/auxdata/`

## Key Observations

### Very Active Project
- Multiple directories updated in 2026 (Jan-Apr)
- Continuous Sentinel-1 processing
- Multiple contributors (vsc40471, vsc44965, vsc45264)

### Multi-Scale Effort
- Continental-scale Sentinel-1 processing (4949 tiles!)
- Regional studies (Alps, Andes, Nordic)
- Multiple data sources (SAR, Lidar, PMW, in-situ)

### Data Products
Several components appear to be research outputs/products:
- Sentinel-1 snow products
- Snow climatology
- Snow cover maps
- PMW SWE retrievals

## Questions for SNOWSHOP Team

1. **Sentinel-1 products:**
   - Are `g0_100m/` products used by other research groups?
   - Should they be shared/generated/?
   - Spatial coverage? (4949 tiles suggests major region)

2. **Data sharing:**
   - Which products are intended for broader use?
   - Which are project-internal?

3. **WAVETRAX relationship:**
   - Should `wavetrax/` be merged with `/WAVETRAX/`?
   - Or are they different aspects?

4. **FMI data:**
   - License/sharing restrictions?
   - Should be properly documented with source

5. **Archive opportunities:**
   - Can `g0_100m_tar/` be moved to tape archive?
   - Temp directories needed?

6. **AlphaEarth:**
   - Relationship with `EXT/alpha_earth_embeddings/`?
   - Consolidation opportunity?

7. **Active products:**
   - Which outputs are actively used?
   - Update frequency?

## Proposed Migration Plan

### Structure (Hybrid Approach)

```
shared/
├── external/
│   └── FMI/
│       └── snowclim/              # Snowclim_FMI
├── observations/
│   ├── lidar/snow/                # Lidar
│   └── ground/snow/               # measurements
└── generated/SNOWSHOP/
    ├── metadata.yaml
    ├── README.md
    ├── Sentinel1/                 # Major product
    │   ├── g0_100m/               # Active data
    │   ├── SD_RETRIEVAL/
    │   └── SNAPPY/
    ├── snowcover/                 # Snow cover products
    ├── Snowclim/                  # If shared product
    └── PMW_SWE/                   # If original product

projects/SNOWSHOP/
├── internal/
│   ├── WetSnow/                   # Active research
│   ├── AlphaEarth/                # ML experiments
│   └── forcings/                  # Regional extracts
├── auxdata/
├── processing/
│   ├── g0_100m_tmp/               # Temp processing
│   └── archive/
│       └── g0_100m_tar/           # Or move to tape
├── pythonenv/                     # Or remove if conda
└── shared -> ../../shared/generated/SNOWSHOP/
```

### WAVETRAX Consideration
```
projects/WAVETRAX/                 # Main project
├── data/
└── shared_with_SNOWSHOP -> ../SNOWSHOP/wavetrax/
```

## Recommended Actions

1. **Contact team leads:** vsc40471, vsc44965, vsc45264 - determine sharing plan
2. **Document Sentinel-1 coverage:** What region/time period is `g0_100m/`?
3. **Archive planning:** Move `g0_100m_tar/` to tape archive
4. **Clean temp dirs:** Remove or document need for `g0_100m_tmp/`, `g0_100m_untar/`
5. **FMI documentation:** Create metadata.yaml for Snowclim_FMI with source
6. **WAVETRAX consolidation:** Determine merge or link strategy
7. **Product documentation:** Create README for major products (Sentinel-1, snowcover)

## Notes

- **Impressive scale:** 4949 Sentinel-1 tiles suggests major processing effort
- **Active development:** Multiple recent updates (2026)
- **Multi-disciplinary:** Combines SAR, lidar, passive microwave, in-situ
- **Strong candidate for shared/generated:** Major data products likely useful to broader community
- **Well-organized:** Clear separation of data types
- **Processing artifacts:** Several temp/cache directories could be cleaned up
