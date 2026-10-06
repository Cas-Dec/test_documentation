# HEAT/ Structure Inventory

**Path:** `/data/gent/vo/000/gvo00090/HEAT/`
**Owner:** vsc45925 (primary), Multiple contributors
**Purpose:** Heat wave analysis and prediction system with ERA5 data and forecasts
**Total Size:** ~6+ TB

## Directory Structure

| Subdirectory | Owner | Last Modified | Size | Type | Proposed Location |
|--------------|-------|---------------|------|------|-------------------|
| **Data/** | vsc46240 | 2026-09-29 | ~6TB | Raw datasets | `shared/generated/HEAT/data/` or `projects/HEAT/data/` |
| **Preds/** | vsc42145 | 2025-07-29 | 2.8GB | Predictions/outputs | `shared/generated/HEAT/predictions/` or `projects/HEAT/predictions/` |
| **download_scripts/** | vsc46240 | 2025-05-22 | - | Scripts | `projects/HEAT/scripts/download/` |
| **stats/** | vsc46240 | 2025-06-10 | - | Analysis scripts | `projects/HEAT/scripts/analysis/` |

## Detailed Analysis

### 1. **Data/** → Classification TBD
- **Type:** Large-scale climate data collection for heat analysis
- **Structure:**
  - `arco-era5/` - 4.1TB - Analysis-ready cloud-optimized ERA5
  - `ERA5_old/` - 1.5TB - Legacy ERA5 data
  - `forecasts/` - 375GB - Weather forecast data (12 subdirs)
  - `climatology/` - 21GB - Climatological statistics (12 subdirs)
  - `climate_indices/` - 6.9MB - Climate variability indices
  - `arco-era5/` - 256 subdirs - Extensive variable coverage
  - `wb/`, `wb2/` - Working directories
- **Status:** Very active (Sep 2026), multiple users
- **Users:** vsc46240 (primary), vsc42145
- **Migration Decision Needed:**
  - If cross-team heat analysis tool → `shared/generated/HEAT/`
  - If project-specific research → `projects/HEAT/internal/`
  - ERA5 data might duplicate EXT/ERA5 - consolidation opportunity?

### 2. **Preds/** → TBD based on Data/ classification
- **Type:** Model predictions/outputs
- **Structure:**
  - `Heatdome/` - 2.8GB - Heat dome predictions
- **Status:** Active (Jul 2025)
- **Users:** vsc42145
- **Migration:** Follow Data/ classification
  - If shared → `shared/generated/HEAT/predictions/`
  - If internal → `projects/HEAT/predictions/`

### 3. **download_scripts/** → `projects/HEAT/scripts/`
- **Type:** Data acquisition scripts
- **Last modified:** May 2025
- **Migration:** Keep in project space regardless of data location

### 4. **stats/** → `projects/HEAT/scripts/`
- **Type:** Statistical analysis scripts
- **Last modified:** Jun 2025
- **Migration:** Keep in project space

## Key Questions for HEAT Team

1. **Project scope:**
   - Is HEAT a tool/dataset used by multiple research groups?
   - Or is it a single project/paper?

2. **ERA5 data redundancy:**
   - `Data/arco-era5/` (4.1TB) vs `EXT/ERA5/`
   - Should these be consolidated?
   - Is arco-era5 a specialized processing or different source?

3. **Forecasts data:**
   - Is `forecasts/` (375GB) operational forecast data?
   - Source and update frequency?
   - Used by other projects?

4. **ERA5_old vs current:**
   - Can `ERA5_old/` (1.5TB) be archived?
   - Or is it different temporal/spatial coverage?

5. **Predictions workflow:**
   - Are `Preds/` outputs consumed by other teams?
   - Should they be in shared/generated/?

6. **Active users:**
   - Who are the primary users: vsc46240, vsc42145?
   - Any other consumers of this data?

## Proposed Migration Plan

### Option A: If Cross-Team Resource
```
shared/generated/HEAT/
├── metadata.yaml
├── README.md
├── data/
│   ├── era5/           # Consolidate with EXT/ERA5?
│   ├── forecasts/
│   ├── climatology/
│   └── climate_indices/
└── predictions/
    └── Heatdome/

projects/HEAT/
├── scripts/
│   ├── download/
│   └── analysis/
└── shared -> ../../shared/generated/HEAT/
```

### Option B: If Project-Internal Research
```
projects/HEAT/
├── data/
│   ├── era5/
│   ├── arco-era5/
│   ├── forecasts/
│   └── climatology/
├── predictions/
│   └── Heatdome/
└── scripts/
    ├── download/
    └── analysis/
```

### Option C: Hybrid (Recommended if uncertain)
```
shared/generated/HEAT/
├── metadata.yaml
├── README.md
├── climatology/        # Derived products - sharable
└── predictions/        # Model outputs - sharable

projects/HEAT/
├── internal/
│   ├── data/          # Working data
│   └── experiments/
├── scripts/
└── shared -> ../../shared/generated/HEAT/
```

## Recommended Actions

1. **Immediate:** Contact vsc46240 and vsc42145 to determine project scope
2. **Assess ERA5 overlap:** Compare with EXT/ERA5 for consolidation
3. **Document arco-era5:** Understand processing pipeline and uniqueness
4. **Archive assessment:** Determine if ERA5_old can be removed
5. **User survey:** Identify all consumers of HEAT data/predictions

## Notes

- **Very active:** Last modifications Sep 2026 - currently in use
- **Large scale:** 6TB+ suggests significant computational investment
- **Multiple owners:** Suggests collaborative project
- **World-writable permissions:** May need to be restricted in new structure
- **arco-era5 format:** Analysis-Ready Cloud-Optimized format suggests modern, efficient data structure worth preserving
