# GLEAM/ Structure Inventory

**Path:** `/data/gent/vo/000/gvo00090/GLEAM/`
**Owner:** vsc45925 (primary), Group: ggleam
**Purpose:** GLEAM (Global Land Evaporation Amsterdam
Model) outputs and variants 

## Directory Structure

Subdirectory Owner Last Modified Type Proposed Location
|--------------|-------|---------------|------|-----------│--------|
**data** vsc45925 2023-09-15 Symlink to scratch
`shared/generated/GLEAM/` (canonical outputs)
**GLEAM-Hybrid** vsc44412 2024-06-28 Production
output (1980-2020 by year)
`shared/generated/GLEAM-Hybrid/`
**GLEAM4_outputs** vsc42444 2026-04-22 Recent
production (aggregated_output, fractions_output)
`shared/generated/GLEAM4/` or part of canonical
**HERMES** vsc46187 2026-04-02 ML-based variant
(HERMESv1.0) `shared/generated/HERMES/` or
`projects/GLEAM/HERMES/`
**GLANCE** vsc46187 2026-09-28
Analysis/experiments (convergence tests, ensembles)
`projects/GLEAM/internal/GLANCE/`
**ET-SENSE** vsc45925 2020-07-07 Older project
(forcing, pygleam, pyval)
`projects/GLEAM/internal/ET-SENSE/` or archive
**gleam-hr** vsc45925 2020-02-23 High-resolution
variant (forcing, static)
`projects/GLEAM/internal/gleam-hr/` or archive
**GLEAM-PIE** vsc45925 2018-04-26 Old project
(data, scripts) `projects/GLEAM/internal/GLEAM-PIE/` or archive 
**scripts** vsc45925 2020-01-27 Processing scripts
 (v32, v33, v34) Keep in projects/GLEAM/ or distribute

## Detailed Analysis  

### 1. **data/** → `shared/generated/GLEAM/`
- **Type:** Symlink to
`/scratch/gent/vo/000/gvo00090/GLEAM/data/`
- **Status:** Main canonical GLEAM outputs, actively
accessed
- **Migration:** Create proper structure in
`shared/generated/GLEAM/` with metadata.yaml
- **Note:** Need to check scratch directory structure to
understand actual data layout

### 2. **GLEAM-Hybrid/** →
`shared/generated/GLEAM-Hybrid/`
- **Type:** Production dataset
- **Structure:** One directory per year (1980-2020), 16K
each
- **Status:** Recently updated (Jun 2024), complete
40-year run  
- **Users:** vsc44412 (owner), accessible to ggleam group
- **Migration:** Separate product with own metadata, or  
variant of main GLEAM?
- **Question:** Is this the main "official" GLEAM output 
or an experimental variant? 
 
### 3. **GLEAM4_outputs/** → TBD 
- **Type:** Recent production outputs  
- **Structure:**
  - `parallel_outputs/aggregated_output/` (7 subdirs) 
  - `parallel_outputs/fractions_output/` (7 subdirs)  
- **Status:** Very recent (Apr 2026), actively developed 
- **Users:** vsc42444 
- **Migration:** Determine if this is: 
  - The next version of canonical GLEAM → 
`shared/generated/GLEAM/` (version 4)  
  - Experimental → `projects/GLEAM/internal/GLEAM4_dev/` 
 
### 4. **HERMES/** → `shared/generated/HERMES/` OR 
`projects/GLEAM/HERMES/` 
- **Type:** Machine learning-based ET model variant
- **Structure:**
  - `HERMESv1.0/` (7 processing stages: selection, 
in_situ, forcings, stressnet, output, training, 
validation)  
  - `HERMES_Tiles/`
  - `Preprocessed_data/` 
  - `Processed_data/` 
- **Status:** Active (last modified Apr 2026)
- **Users:** vsc46187 
- **Question:** Is HERMES:  
  - A new official GLEAM product used by multiple teams? → │
 `shared/generated/HERMES/`
  - A project-specific ML experiment? →
`projects/GLEAM/internal/HERMES/`
- **Note:** Has versioning (v1.0), suggesting it may be  
intended as a product 
 
### 5. **GLANCE/** → `projects/GLEAM/internal/GLANCE/`
- **Type:** Analysis/experimental runs 
- **Structure:** Multiple convergence analysis  
experiments, ensemble tests 
- **Status:** Very recent (Sep 2026), active development 
- **Users:** vsc46187 
- **Classification:** Clearly experimental/analysis → 
internal to GLEAM project
- **Migration:** `projects/GLEAM/internal/GLANCE/` (no
metadata required) 
 
### 6. **ET-SENSE** → Archive or 
`projects/GLEAM/internal/ET-SENSE/` 
- **Type:** Older project/variant
- **Structure:** forcing/, pygleam/, pyval/  
- **Last modified:** Jul 2020 (6+ years old) 
- **Status:** Likely inactive/archived 
- **Migration:** Verify if still needed, otherwise archive
 
### 7. **gleam-hr** → Archive or 
`projects/GLEAM/internal/gleam-hr/` 
- **Type:** High-resolution GLEAM variant 
- **Structure:** forcing/, static/  
- **Last modified:** Feb 2020 (6+ years old) 
- **Status:** Likely inactive/archived 
- **Migration:** Verify if still needed, otherwise archive
 
### 8. **GLEAM-PIE** → Archive
- **Type:** Very old project
- **Last modified:** Apr 2018 (8+ years old)
- **Status:** Almost certainly archived
- **Migration:** Move to archive unless someone objects  
 
### 9. **scripts/** → `projects/GLEAM/scripts/` or 
distribute
- **Type:** Processing scripts with versions (v32, v33,  
v34)
- **Last modified:** Jan 2020 
- **Status:** May still be referenced  
- **Migration:** Keep accessible in 
`projects/GLEAM/scripts/` or link to git repo
- **Alternative:** If these are download/processing
scripts, they should be in the metadata.yaml `history`
field as git permalinks  
 
## Key Questions for GLEAM Team  
 
1. **What is the "canonical" GLEAM product?**
- Is it `data/` (symlink to scratch)?  
- Is it `GLEAM-Hybrid/`? 
- Is `GLEAM4_outputs/` the new version?
 
2. **GLEAM-Hybrid classification:** 
- Official product or experimental? 
- Should it be separate dataset or variant/version of 
main GLEAM?  
 
3. **HERMES status:** 
- Cross-team product or GLEAM-project-only?  
- Should it get its own `shared/generated/HERMES/` 
space? 
 
4. **Archive candidates:**  
- Can we archive ET-SENSE, gleam-hr, GLEAM-PIE? 
- Are they referenced by any current work?
 
5. **Data location:** 
- Why is `data/` a symlink to scratch? 
- Should canonical outputs be moved from scratch to
`$VSC_DATA_VO/shared/generated/GLEAM/`?
 
6. **Version/variant naming:**
- What's the relationship between: data/, 
GLEAM-Hybrid/, GLEAM4_outputs/?  
- Should we establish naming convention: `GLEAM/`, 
`GLEAM-v4/`, `GLEAM-Hybrid/`, `HERMES/`?  
 
## Proposed Migration Plan  
 
### Phase 1: Clarify with GLEAM team
Contact owners to determine:
- Which outputs are "official" cross-team products 
- Which are experimental/project-internal 
- Which can be archived  
 
### Phase 2: Create canonical shared/ structure 
Based on team input, likely:
``` 
shared/generated/  
├── GLEAM/  # Main product (from current  
data/) 
  ├── metadata.yaml 
  ├── README.md  
  └── [data structure TBD based on scratch contents]
├── GLEAM-Hybrid/ # If deemed cross-team product
  ├── metadata.yaml 
  ├── README.md  
  └── [yearly directories 1980-2020] 
└── HERMES/ # If deemed cross-team product
 ├── metadata.yaml
 ├── README.md  
 └── HERMESv1.0/
``` 
 
### Phase 3: Organize project-internal space 
``` 
projects/GLEAM/ 
├── internal/
  ├── GLANCE/# Active experimental work 
  ├── GLEAM4_dev/  # If GLEAM4_outputs is still  
development  
  ├── HERMES/# If HERMES is project-only
  └── archive/
├── ET-SENSE/ 
├── gleam-hr/ 
└── GLEAM-PIE/
├── scripts/# Processing scripts 
└── shared -> ../../shared/generated/GLEAM  # Symlink to 
canonical outputs  
``` 
 
## Next Steps
 
1. **Contact GLEAM team leads** (vsc45925, vsc44412,  
vsc46187, vsc42444)
2. **Examine scratch data structure** to understand
canonical output format  
3. **Document GLEAM-Hybrid** file structure and naming
convention
4. **Check GLEAM4 status** - is it production-ready?
5. **Verify archive candidates** - last access times for 
ET-SENSE, gleam-hr, GLEAM-PIE
