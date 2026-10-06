# BUCCS/ Structure Inventory

**Path:** `/data/gent/vo/000/gvo00090/BUCCS/`
**Owner:** vsc45925, Group: 2542247
**Purpose:** Belgian Urban Climate Convection Study (BUCCS) - High-resolution meteorological modeling
**Total Size:** ~100 MB (mainly software/tools)
**Last Modified:** 2023-03-04

## Directory Structure

| Subdirectory | Type | Size | Last Modified | Proposed Location |
|--------------|------|------|---------------|-------------------|
| **UFB_0010_EXTPAR.nc** | Static data file | 100 MB | 2018-08-03 | `projects/BUCCS/data/static/` |
| **nccd/** | Software (uncompressed) | - | 2023-03-04 | `projects/BUCCS/software/nccd/` |
| **nccd.tar.gz** | Software archive | 670 KB | 2018-08-03 | Keep for reference |
| **ec2caf/** | Software (uncompressed) | - | 2023-03-04 | `projects/BUCCS/software/ec2caf/` |
| **ec2caf.tar.gz** | Software archive | 645 KB | 2018-08-03 | Keep for reference |
| **scripts/** | Processing scripts | - | 2023-03-04 | `projects/BUCCS/scripts/` |

## Detailed Analysis

### 1. **UFB_0010_EXTPAR.nc** → Static Geographical Data
- **Type:** COSMO/WRF external parameters file (100 MB netCDF)
- **Content:** Static geographical data (topography, land use, soil type)
- **Domain:** "UFB_0010" suggests Urban domain, Belgium, 0.01° (~1km) resolution
- **Last modified:** Aug 2018 (8 years old)
- **Status:** Static data - doesn't change over time
- **Migration:** `projects/BUCCS/data/static/extpar/`
- **Note:** Standard COSMO external parameter file

### 2. **nccd/** → NCCD Software
- **Type:** Software tool/library (8 subdirs)
- **Size:** Small (< 1 MB based on tarball)
- **Last modified:** Mar 2023
- **Compressed:** nccd.tar.gz (670 KB)
- **Likely:** "NetCDF Climate Data" processing tools or similar
- **Migration:** `projects/BUCCS/software/nccd/`
- **Note:** Should document version and link to source repo if available

### 3. **ec2caf/** → EC2CAF Conversion Tool
- **Type:** Software tool (2 subdirs)
- **Size:** Small (< 1 MB based on tarball)
- **Last modified:** Mar 2023
- **Compressed:** ec2caf.tar.gz (645 KB)
- **Likely:** "ECMWF to CAF" (Climate Analysis Format?) converter
- **Migration:** `projects/BUCCS/software/ec2caf/`
- **Note:** May be for converting ECMWF data to specific format

### 4. **scripts/** → Processing/Analysis Scripts
- **Type:** BUCCS-specific processing scripts (4 subdirs)
- **Last modified:** Mar 2023
- **Migration:** `projects/BUCCS/scripts/`

## Project Assessment

### BUCCS Background
- **BUCCS** = Belgian Urban Climate Convection Study
- **Focus:** High-resolution urban meteorology over Belgium
- **Typical setup:** COSMO or WRF regional climate model runs
- **Domain:** Belgian urban areas at ~1 km resolution

### Current Status
- **Last activity:** Mar 2023 (18 months ago)
- **Data content:** Minimal - only 1 static file (100 MB)
- **Mainly software:** Processing tools and scripts
- **No simulation outputs:** Suggests output data elsewhere or archived

### Key Observations
1. **Static data only:** No dynamic model outputs present
2. **Software-focused:** Mainly tools for data processing
3. **Modest size:** 100 MB total - easy to migrate
4. **Old project:** 2018 data suggests completed study
5. **Maintained tools:** Scripts updated 2023 despite old data

## Questions for BUCCS Team

1. **Project status:**
   - Is BUCCS completed or ongoing?
   - Last activity Mar 2023 - still active?

2. **Model output location:**
   - Where are COSMO/WRF simulation outputs?
   - In user scratch directories?
   - Already archived?

3. **Software usage:**
   - Are nccd and ec2caf still in use?
   - General tools or BUCCS-specific?
   - Available in public repos?

4. **Static data:**
   - Is UFB_0010_EXTPAR.nc still needed?
   - Generated from standard COSMO preprocessing?

5. **Collaboration:**
   - Single researcher or group project?
   - Data/tools shared with others?

6. **Scripts:**
   - Actively maintained?
   - Should be in Git repository?

## Proposed Migration Plan

### Simple Project Structure
```
projects/BUCCS/
├── README.md              # Project description, status, publications
├── data/
│   └── static/
│       └── extpar/
│           └── UFB_0010_EXTPAR.nc
├── software/
│   ├── nccd/              # Uncompressed tools
│   │   └── [8 subdirs]
│   ├── ec2caf/            # Uncompressed tools
│   │   └── [2 subdirs]
│   └── archives/          # Keep compressed backups
│       ├── nccd.tar.gz
│       └── ec2caf.tar.gz
├── scripts/               # Processing scripts
│   └── [4 subdirs]
└── docs/
    └── software_docs.md   # Document nccd and ec2caf usage
```

### Alternative: If Software is General-Purpose
If `nccd` and `ec2caf` are general tools (not BUCCS-specific):
```
tools/
├── nccd/                  # Move from BUCCS if general-purpose
└── ec2caf/                # Move from BUCCS if general-purpose

projects/BUCCS/
├── data/static/
├── scripts/
└── software -> ../../tools/  # Symlinks to specific tools
```

## Recommended Actions

1. **Contact vsc45925** - Determine project status and future plans
2. **Locate simulation data** - Find actual COSMO/WRF outputs if still needed
3. **Document software:**
   - What do nccd and ec2caf do?
   - Link to source repositories if available
   - Document dependencies and usage
4. **Git repository:**
   - Move scripts to Git if not already there
   - Version control for active code
5. **Archive assessment:**
   - If project completed, document and archive
   - If active, plan for future data organization
6. **Check user directories:**
   - `ls -la /data/gent/vo/000/gvo00090/vsc45925/` for related data
   - May have model outputs in personal space

## Comparison with Related Directories

### Similar Projects
- **D2D/data/COSMO/** - COSMO model outputs (3.3 GB, 2017) - archived
- **BUCCS** - Only static COSMO files (2018)
- Suggests BUCCS may also be completed project

### Software Overlap
- `tools/` directory exists with shared utilities
- Consider if `nccd` and `ec2caf` belong in shared `tools/`

## Migration Complexity: LOW

### Why Migration is Straightforward
1. **Small size:** Only 100 MB + software
2. **Simple structure:** 6 items total
3. **No dependencies:** Self-contained
4. **Clear organization:** Already well-organized
5. **No active data streams:** Static content only

### Migration Steps
1. Create `projects/BUCCS/` structure
2. Copy data (100 MB) - fast
3. Move software directories
4. Move scripts
5. Create README documenting project
6. Total time: < 1 hour

## Notes

- **Minimal storage impact:** Only 100 MB data
- **Low priority:** Small, stable, not actively generating data
- **Good documentation candidate:** Small enough to fully document
- **Potential archive:** If project completed, good candidate for documentation + archive
- **Software preservation:** nccd and ec2caf may be valuable tools worth documenting
- **Clean structure:** Already well-organized, minimal cleanup needed
