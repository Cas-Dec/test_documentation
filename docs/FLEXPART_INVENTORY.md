# FLEXPART/ Structure Inventory

**Path:** `/data/gent/vo/000/gvo00090/FLEXPART/`
**Owner:** vsc45925 (primary), Group: 2640367
**Purpose:** FLEXPART Lagrangian particle dispersion model infrastructure - atmospheric transport modeling
**Last Modified:** 2023-09-14

## Directory Structure

| Subdirectory | Last Modified | Type | Proposed Location |
|--------------|---------------|------|-------------------|
| **forcing/** | 2023-11-15 | Meteorological input data | `shared/external/meteorology/` or `projects/FLEXPART/forcing/` |
| **hamster/** | 2022-10-06 | Unknown component | TBD |
| **observations/** | 2023-09-15 | Field campaign data | `shared/observations/atmospheric/` or `projects/FLEXPART/observations/` |
| **simulations/** | 2023-09-14 | Model outputs | `shared/generated/FLEXPART/` or `projects/FLEXPART/simulations/` |
| **tools/** | 2023-09-14 | Processing/analysis tools | `projects/FLEXPART/tools/` |
| **versions/** | 2023-01-10 | Model version archives | `projects/FLEXPART/versions/` |

## Detailed Analysis

### 1. **forcing/** → Meteorological Driving Data
- **Type:** ERA5 and ERA-Interim reanalysis data formatted for FLEXPART
- **Structure:**
  - `era5_ugent/` - ERA5 forcing by year (2013-2022+)
  - `eraint_global_ugent/` - ERA-Interim 2008-2016 (42 subdirs)
- **Status:** Updated Nov 2023, likely still active
- **Size:** Potentially large (reanalysis subsets)
- **Migration Options:**
  1. Link to `shared/external/ERA5/` if structure compatible
  2. Keep as `projects/FLEXPART/forcing/` if FLEXPART-specific preprocessing
  3. If used by multiple modeling groups → `shared/forcing/atmospheric/`

### 2. **observations/** → Field Campaign Data
- **Type:** Atmospheric observations and radiosonde data
- **Structure:**
  - `IGRA_PAIRS_20190515/` - 35 subdirs of radiosonde profiles
  - `IGRA_PAIRS_20190515_experiments_export/` - 35 subdirs + 5.1GB tarball
  - `IGRA_PAIRS_20190419/` - 11 subdirs (earlier version)
  - `GOAMAZON/`, `GOAMAZON5/`, `GOAMAZON6/` - Amazon field campaign
  - `GLOBAL_20181217/` - 20 subdirs
  - `IOPS/` - 21 subdirs
- **Status:** Last updated Jun 2021 (tarball export)
- **Classification:**
  - IGRA = Integrated Global Radiosonde Archive (public dataset)
  - GOAMAZON = GoAmazon field campaign (major international campaign)
  - May be FLEXPART-specific processing or general resource
- **Migration:**
  - If raw/general → `shared/observations/atmospheric/`
  - If FLEXPART-processed → `projects/FLEXPART/observations/`

### 3. **simulations/** → Model Outputs
- **Type:** FLEXPART simulation results
- **Structure:**
  - `era5_global_ugent/` - 49 subdirs (Apr 2025) - **Recently updated!**
  - `eraint_europe_ugent/` - Sep 2024 - Recent
  - `eraint_global_ugent/` - 44 subdirs (Jun 2023)
  - `eraint_global_uvigo/` - 42 subdirs (Dec 2022) - Different institution
- **Status:** **ACTIVE** - Updated as recently as Apr 2025
- **Users:** UGent + UVigo collaboration
- **Migration:**
  - If used by multiple research groups → `shared/generated/FLEXPART/`
  - If project-specific → `projects/FLEXPART/simulations/`

### 4. **tools/** → Processing/Analysis Software
- **Type:** FLEXPART-related utilities
- **Last modified:** Sep 2023
- **Migration:** `projects/FLEXPART/tools/`
- **Note:** May contain important processing scripts

### 5. **versions/** → Model Code Archives
- **Type:** Different FLEXPART model versions
- **Last modified:** Jan 2023
- **Migration:** `projects/FLEXPART/versions/` or link to Git repo
- **Note:** If model versions are in Git, document in README instead

### 6. **hamster/** → TBD
- **Type:** Unknown component
- **Last modified:** Oct 2022
- **Action:** Needs investigation before migration

## Key Observations

### Active Development
- **simulations/era5_global_ugent/** updated **Apr 2025** - very recent!
- Multiple simulation variants suggest ongoing research
- Cross-institution collaboration (UGent + UVigo)

### Data Relationship Questions
1. **Forcing data:**
   - Is `forcing/era5_ugent/` redundant with `EXT/ERA5/`?
   - Or FLEXPART-specific preprocessing (unit conversion, spatial subsetting)?

2. **IGRA observations:**
   - Also appears in `D2D/data/IGRA_PAIRS_*`
   - Should be consolidated or linked?

3. **CESM forcing:**
   - `EXT/CESM_data_for_FLEXPART/` exists
   - Should be moved to `FLEXPART/forcing/cesm/`?

## Proposed Migration Plan

### Recommended Structure (Hybrid Approach)

```
shared/
├── observations/atmospheric/
│   └── IGRA/              # If general resource
│       ├── metadata.yaml
│       └── [link or move from FLEXPART/observations/]
└── generated/FLEXPART/
    ├── metadata.yaml
    ├── README.md
    └── simulations/
        ├── era5_global/   # Recent outputs used by multiple groups
        └── eraint_global/

projects/FLEXPART/
├── forcing/
│   ├── era5/              # Preprocessed for FLEXPART
│   ├── eraint/
│   └── cesm/              # Move from EXT/
├── observations/
│   ├── GOAMAZON/          # Campaign-specific
│   └── [IGRA if FLEXPART-specific processing]
├── simulations/
│   ├── experiments/       # Project-specific runs
│   └── archive/           # Old simulations
├── tools/
├── versions/
└── shared -> ../../shared/generated/FLEXPART/
```

## Questions for FLEXPART Team

1. **Project scope:**
   - Is FLEXPART infrastructure shared across multiple research groups?
   - Or single project/group?

2. **Active simulations:**
   - `era5_global_ugent/` updated Apr 2025 - ongoing work?
   - Who uses these simulation outputs?

3. **Forcing data preprocessing:**
   - Is `forcing/` FLEXPART-specific or general meteorology?
   - Relationship with `EXT/ERA5/`?

4. **IGRA data:**
   - Used only by FLEXPART or general radiosonde resource?
   - Consolidate with `D2D/data/IGRA_PAIRS_*`?

5. **UVigo collaboration:**
   - `eraint_global_uvigo/` - joint project?
   - Data sharing arrangement?

6. **hamster/ component:**
   - What is this? Still needed?

7. **Archive candidates:**
   - Can older ERA-Interim simulations be archived?
   - Export tarball suggests data packaging - still needed?

## Recommended Actions

1. **Contact team lead:** Determine active users and project scope
2. **Check recent activity:** `find /data/gent/vo/000/gvo00090/FLEXPART/simulations/era5_global_ugent/ -type f -mtime -180` (files modified in last 6 months)
3. **Document preprocessing:** Understand forcing/ data workflow
4. **IGRA consolidation:** Survey all IGRA copies across VO space
5. **Move CESM forcing:** Relocate `EXT/CESM_data_for_FLEXPART/` to `FLEXPART/forcing/`
6. **Archive plan:** Identify old simulations for archival

## Notes

- **Well-organized structure:** Clear separation of forcing/observations/simulations
- **Active system:** Recent updates suggest operational status
- **Cross-institution:** UVigo collaboration indicates broader community use
- **Potential for shared resource:** If multiple groups use FLEXPART, strong candidate for shared/generated/
- **FLEXPART:** Widely-used atmospheric transport model in European research community
