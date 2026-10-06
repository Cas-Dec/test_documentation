# D2D/ Structure Inventory

**Path:** `/data/gent/vo/000/gvo00090/D2D/`
**Owner:** vsc45925, Group: 2640220
**Purpose:** "Data-to-Diagnosis" - Atmospheric boundary layer analysis using soundings and model data
**Total Size:** ~2.8 TB
**Last Modified:** 2023-06-23

## Directory Structure

| Subdirectory | Last Modified | Size | Type | Proposed Location |
|--------------|---------------|------|------|-------------------|
| **data/** | 2023-03-06 | ~2.8TB | Primary datasets | See detailed breakdown below |
| **scripts/** | 2023-01-10 | - | Processing scripts | `projects/D2D/scripts/` |
| **software/** | 2023-03-04 | - | Analysis software | `projects/D2D/software/` |
| **archive/** | 2019-02-18 | - | Archived data | `projects/D2D/archive/` |
| **log/** | 2019-02-09 | - | Processing logs | `projects/D2D/logs/` |
| **D2D_scripts.tgz** | 2023-06-23 | 14MB | Script archive | Keep for reference |

## Detailed Data Inventory

### data/ Subdirectories (by size)

| Dataset | Size | Last Modified | Type | Proposed Location |
|---------|------|---------------|------|-------------------|
| **C4GL** | 2.4 TB | 2023-03-05 | Largest component | TBD - needs investigation |
| **GLEAM** | 184 GB | 2023-03-06 | GLEAM outputs | Link to GLEAM/ or archive |
| **SOUNDINGS** | 102 GB | 2021-02-18 | Radiosonde obs | `shared/observations/atmospheric/soundings/` |
| **IGRA_PAIRS_20190515** | 11 GB | 2019-08-22 | Radiosonde pairs | Consolidate with FLEXPART? |
| **IGRA_PAIRS_20190419** | 47 GB | 2019-05-14 | Earlier version | Archive or consolidate |
| **Aridity** | 21 GB | 2019-05-28 | Aridity indices | `shared/derived/aridity/` or archive |
| **IGRA_PAIRS_20190515.tar.gz** | 3.6 GB | 2021-06-24 | Compressed backup | Can be removed if data intact |
| **COSMO** | 3.3 GB | 2017-10-25 | COSMO model output | Archive (old) |
| **GLOBAL_20190515** | 31 MB | 2019-05-14 | Global metadata | Keep with IGRA |
| **FLUX_SITES** | 33 MB | 2017-10-18 | Flux tower sites | Link to EXT/FLUXNET? |
| **experiments** | 8 KB | 2022-03-23 | Experiment configs | `projects/D2D/experiments/` |
| **ERA5** | 2 KB | 2019-03-19 | Symlink/pointer | Link to EXT/ERA5 |
| **log** | 1 KB | 2019-03-12 | Processing log | `projects/D2D/logs/` |

## Critical Issue: C4GL (2.4 TB!)

### Unknown Large Dataset
- **Size:** 2.4 TB (86% of D2D total!)
- **Last modified:** Mar 2023
- **Structure:** 10 subdirs
- **Status:** **REQUIRES URGENT INVESTIGATION**
- **Questions:**
  - What is C4GL? (No obvious acronym match)
  - Is it actively used?
  - Can it be archived or moved?
  - Should it be separate from D2D?

**Action needed:** Investigate C4GL structure before migration

## Detailed Analysis

### 1. **data/C4GL/** → URGENT: Needs Investigation
- **Size:** 2.4 TB - Dominates D2D storage
- **Structure:** 10 subdirectories (need to explore)
- **Last modified:** Mar 2023 - relatively recent
- **Migration:** Cannot proceed without understanding this dataset
- **Action:** `ls -lh /data/gent/vo/000/gvo00090/D2D/data/C4GL/` to investigate

### 2. **data/GLEAM/** → Link or Archive
- **Type:** GLEAM model outputs (184 GB)
- **Size:** 32K subdirectories suggests many files
- **Issue:** Duplicates main GLEAM/ directory?
- **Migration Options:**
  1. Create symlink to `shared/generated/GLEAM/`
  2. Determine if D2D-specific subset, keep as `projects/D2D/data/GLEAM/`
  3. Archive if no longer needed
- **Action:** Compare with main `/GLEAM/` directory

### 3. **data/SOUNDINGS/** → Shared Observations
- **Type:** Radiosonde soundings (102 GB)
- **Structure:** 25 subdirectories
- **Last modified:** Feb 2021
- **Status:** Likely still valuable
- **Migration:** `shared/observations/atmospheric/soundings/`
- **Note:** Well-organized observational resource

### 4. **data/IGRA_PAIRS_*** → Consolidate
- **Type:** Integrated Global Radiosonde Archive - matched pairs
- **Versions:**
  - `20190419` - 47 GB (11 subdirs) - Earlier
  - `20190515` - 11 GB (4 subdirs) + 3.6 GB tarball - Later
- **Issue:** Also in FLEXPART/observations/
- **Migration:**
  1. Consolidate all IGRA data into `shared/observations/atmospheric/IGRA/`
  2. Create version subdirs (v20190419, v20190515)
  3. Link from both D2D and FLEXPART projects
- **Action:** Survey all IGRA copies: `find /data/gent/vo/000/gvo00090/ -name "*IGRA*" -type d`

### 5. **data/Aridity/** → Archive or Shared Derived
- **Type:** Aridity index calculations (21 GB)
- **Last modified:** May 2019 (7+ years old)
- **Migration:**
  - If still used → `shared/derived/climate/aridity/`
  - If obsolete → archive
- **Action:** Check last access time

### 6. **data/COSMO/** → Archive
- **Type:** COSMO regional climate model output (3.3 GB)
- **Last modified:** Oct 2017 (9 years old)
- **Status:** Likely archived/superseded
- **Migration:** Move to archive unless actively referenced

### 7. **data/FLUX_SITES/** → Link to EXT
- **Type:** Flux tower metadata (33 MB)
- **Note:** Main flux data in `EXT/FLUXNET/`
- **Migration:** Create symlink to avoid duplication

### 8. **scripts/** and **software/** → Project Space
- **Type:** D2D-specific processing tools
- **Migration:** `projects/D2D/scripts/` and `projects/D2D/software/`
- **Note:** May contain valuable analysis methods

### 9. **archive/** → Keep as Archive
- **Last modified:** Feb 2019
- **Migration:** `projects/D2D/archive/`

## Data Duplication Issues

### Cross-Project Redundancies
1. **IGRA_PAIRS:**
   - D2D/data/IGRA_PAIRS_20190419/ (47 GB)
   - D2D/data/IGRA_PAIRS_20190515/ (11 GB + tarball)
   - FLEXPART/observations/IGRA_PAIRS_20190419/ (11 subdirs)
   - FLEXPART/observations/IGRA_PAIRS_20190515/ (35 subdirs + tarball)
   - **Recommendation:** Consolidate into shared/observations/

2. **GLEAM:**
   - D2D/data/GLEAM/ (184 GB)
   - /GLEAM/data/ (symlink to scratch)
   - **Recommendation:** Link D2D to canonical GLEAM location

3. **SOUNDINGS:**
   - D2D/data/SOUNDINGS/ (102 GB, 25 subdirs)
   - EXT/SOUNDINGS/ (mentioned in EXT inventory)
   - **Recommendation:** Determine canonical location

## Questions for D2D Team

1. **C4GL mystery:**
   - What is C4GL? (2.4 TB!)
   - Still actively used?
   - Should it be separate project?

2. **Project status:**
   - Is D2D actively maintained?
   - Last modification 2023 - still relevant?

3. **GLEAM relationship:**
   - Is `data/GLEAM/` (184 GB) a subset or duplicate?
   - Can it be replaced with symlink?

4. **IGRA consolidation:**
   - Which version is canonical?
   - Consolidate with FLEXPART's IGRA data?

5. **Archive candidates:**
   - COSMO (2017) - still needed?
   - Aridity (2019) - still accessed?
   - Old IGRA versions?

6. **Soundings:**
   - Relationship with EXT/SOUNDINGS/?
   - Which is primary source?

## Proposed Migration Plan

### Phase 1: Investigate C4GL
```bash
# Explore mysterious 2.4 TB dataset
ls -lh /data/gent/vo/000/gvo00090/D2D/data/C4GL/
du -sh /data/gent/vo/000/gvo00090/D2D/data/C4GL/*/
```

### Phase 2: Consolidate Shared Observations
```
shared/observations/atmospheric/
├── IGRA/
│   ├── metadata.yaml
│   ├── v20190419/    # From D2D + FLEXPART
│   └── v20190515/    # From D2D + FLEXPART
├── soundings/
│   └── [from D2D/data/SOUNDINGS/]
└── flux_sites/
    └── [link to EXT/FLUXNET/]
```

### Phase 3: Project Structure
```
projects/D2D/
├── data/
│   ├── C4GL/         # If D2D-specific
│   └── derived/
│       └── aridity/  # If still needed
├── scripts/
├── software/
├── experiments/
├── archive/
│   ├── COSMO/
│   └── old_versions/
└── shared/
    ├── GLEAM -> ../../../shared/generated/GLEAM/
    ├── IGRA -> ../../../shared/observations/atmospheric/IGRA/
    └── soundings -> ../../../shared/observations/atmospheric/soundings/
```

## Recommended Actions (Priority Order)

1. **URGENT: Investigate C4GL** - Cannot plan migration without understanding 2.4 TB dataset
2. **Survey IGRA copies** - Find all instances and consolidate
3. **Compare GLEAM** - Determine if D2D/GLEAM duplicates main GLEAM/
4. **Check access times** - `ls -ltu` on old datasets (COSMO, Aridity)
5. **Contact D2D team** - Determine project status and active datasets
6. **Document soundings** - Clarify relationship with EXT/SOUNDINGS/
7. **Plan archive** - Move old/unused data to tape archive

## Notes

- **D2D appears semi-retired:** Last major update Jun 2023
- **C4GL dominates storage:** 86% of space - critical to understand
- **Significant duplication:** IGRA, GLEAM, SOUNDINGS appear elsewhere
- **Storage savings potential:** Consolidation could free up 100+ GB
- **Scripts preserved:** D2D_scripts.tgz (14 MB) backup exists
- **Well-structured:** Clear separation of data/scripts/software/archive
