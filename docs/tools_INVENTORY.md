# tools/ Structure Inventory

**Path:** `/data/gent/vo/000/gvo00090/tools/`
**Owner:** vsc45925, Group: 2640367
**Purpose:** Shared utilities and templates for VO group
**Total Size:** ~3 MB (mainly documentation and small scripts)
**Last Modified:** 2023-01-13

## Directory Structure

| Subdirectory | Type | Size | Last Modified | Purpose | Keep/Move |
|--------------|------|------|---------------|---------|-----------|
| **ecmwf_tools/** | Scripts | ~10 KB | 2022-02-09 | ECMWF data download | Keep |
| **hpc_tools/** | Templates | ~35 KB | 2021-12-23 | HPC job templates | Keep |
| **vo_tools/** | Scripts | ~3 KB | 2023-01-13 | VO data management | Keep |
| **tier1_data/** | Documentation | ~2 KB | 2021-12-23 | Tier-1 access guide | Keep |
| **gitdemo/** | Tutorial | ~2.3 MB | 2021-12-23 | Git training materials | Keep/Update |

## Detailed Analysis

### 1. **ecmwf_tools/** → ECMWF Data Access
- **Type:** Python scripts for downloading ERA5 and ERA-Interim
- **Contents:**
  - `get_era5_generic.py` (2.4 KB) - Generic ERA5 download
  - `get_eraint_example1.py` (1.2 KB) - ERA-Interim example 1
  - `get_eraint_example2.py` (2.5 KB) - ERA-Interim example 2
  - `README.md` (492 bytes) - Documentation
  - `tables/` - Reference tables (4 subdirs)
- **Status:** ERA-Interim retired in 2019, ERA5 still relevant
- **Value:** Template scripts for data access
- **Migration:** Keep in `tools/ecmwf/`
- **Improvement:** Update README, note ERA-Interim deprecated

### 2. **hpc_tools/** → Job Submission Templates
- **Type:** SLURM and Torque job script templates
- **Contents:**
  - `slurm_job.sh` (503 bytes) - Basic SLURM job
  - `slurm_array_job.sh` (526 bytes) - SLURM array job
  - `slurm_job_val.sh` (510 bytes) - SLURM validation job
  - `torque_job.sh` (470 bytes) - Basic Torque job (deprecated)
  - `torque_array_job.sh` (485 bytes) - Torque array (deprecated)
  - `torque_job_val.sh` (477 bytes) - Torque validation (deprecated)
  - `README.md` (537 bytes) - Documentation
  - `LICENSE` (34 KB) - GPL license
- **Status:** SLURM still relevant, Torque outdated
- **Value:** Essential onboarding resource for new users
- **Migration:** Keep in `tools/hpc/`
- **Improvement:**
  - Update for current VSC HPC setup
  - Add modern SLURM features (GPU jobs, etc.)
  - Remove or mark Torque templates as historical

### 3. **vo_tools/** → VO Data Management Scripts
- **Type:** Shell scripts for VO data operations
- **Contents:**
  - `check_inode_usage.sh` (441 bytes, executable) - Check file count
  - `count_number_of_files_in_folder.sh` (56 bytes, executable) - File counter
  - `archive_data.sh` (859 bytes) - Data archival helper
  - `share_data_with_vsc.sh` (1.3 KB) - Permission management
  - `access_to_networkshares.sh` (543 bytes) - Network mount helper
  - `README.md` (125 bytes) - Minimal documentation
- **Status:** Last updated Jan 2023, likely still relevant
- **Value:** Critical VO management utilities
- **Migration:** Keep in `tools/vo_admin/`
- **Improvement:**
  - Enhance documentation
  - Add examples
  - Consider adding quota checking scripts

### 4. **tier1_data/** → Tier-1 HPC Documentation
- **Type:** Documentation for accessing Tier-1 supercomputer
- **Contents:**
  - `README.md` (1.9 KB) - Guide to Tier-1 data access
- **Status:** Tier-1 access procedures may have changed since 2021
- **Value:** Important for users needing Tier-1 resources
- **Migration:** Keep in `tools/docs/tier1/` or `docs/hpc/tier1/`
- **Improvement:**
  - Verify procedures are current
  - Add updated links
  - Include contact information

### 5. **gitdemo/** → Git Training Materials
- **Type:** Interactive Git tutorial
- **Contents:**
  - `gitintro.pdf` (1.2 MB) - Git introduction presentation
  - `conversation.sh` (1.9 KB, executable) - Interactive demo script
  - `oracle.py` (648 bytes) - Demo helper script
  - `convert2sha1.sh` (251 bytes, executable) - SHA1 converter
  - `fancylog.txt` (262 bytes) - Example log output
  - `README.md` (1.2 KB) - Tutorial instructions
- **Status:** Git tutorial from 2021
- **Value:** Useful onboarding material for version control
- **Migration:** Keep in `tools/training/git/` or `docs/training/git/`
- **Improvement:**
  - Update for modern Git workflows
  - Add GitLab/GitHub examples (VSC GitLab)
  - Include branch strategies

## Overall Assessment

### Purpose and Value
- **Onboarding resource:** Essential for new VO members
- **Documentation:** Captures institutional knowledge
- **Templates:** Reduces learning curve for common tasks
- **Size:** Tiny (< 3 MB) - no storage concern

### Current Status
- **Generally outdated:** Most content from 2021-2022
- **Still relevant:** Core concepts remain valid
- **Needs updates:** Links, procedures may have changed
- **Well-intentioned:** Good idea to have shared tools

### Usage Patterns
- **Last modification:** Jan 2023 (vo_tools)
- **Likely low traffic:** Small updates suggest infrequent use
- **Passive resource:** Reference material, not active development

## Proposed Migration Plan

### Recommended Structure
```
tools/
├── README.md              # Overview of all tools, quickstart
├── ecmwf/
│   ├── README.md          # Updated documentation
│   ├── get_era5_generic.py
│   ├── tables/
│   └── examples/
│       ├── basic_download.py
│       └── advanced_download.py
├── hpc/
│   ├── README.md          # Updated for current VSC setup
│   ├── slurm/
│   │   ├── basic_job.sh
│   │   ├── array_job.sh
│   │   ├── gpu_job.sh     # Add modern features
│   │   └── mpi_job.sh     # Add MPI example
│   └── archive/
│       └── torque/        # Keep for historical reference
├── vo_admin/
│   ├── README.md          # Enhanced documentation
│   ├── check_inode_usage.sh
│   ├── count_files.sh
│   ├── archive_data.sh
│   ├── share_data.sh
│   └── check_quota.sh     # Add new utility
└── docs/
    ├── tier1_access.md    # Updated procedures
    ├── data_organization.md
    └── training/
        └── git/
            ├── README.md
            ├── gitintro.pdf
            └── examples/

# Alternative: Separate documentation
docs/
├── training/
│   └── git/
└── hpc/
    └── tier1/

tools/
├── ecmwf/
├── hpc/
└── vo_admin/
```

## Recommended Actions

### Priority 1: Update Documentation
1. **HPC templates:**
   - Verify SLURM templates work on current VSC systems
   - Add GPU job examples
   - Document resource limits
   - Update module load examples

2. **ECMWF tools:**
   - Note ERA-Interim deprecation
   - Update to CDS API v2 if needed
   - Add authentication instructions
   - Link to official ECMWF docs

3. **Tier-1 access:**
   - Verify current procedures
   - Update links and contact info
   - Add application process details

### Priority 2: Enhance Tools
1. **Add missing utilities:**
   - Quota checking script
   - Data validation tools
   - Batch file operations

2. **Improve vo_tools:**
   - Better error handling
   - Usage examples
   - Integration with VSC tools

3. **Git training:**
   - Update for GitLab workflows
   - Add VSC-specific examples
   - Include CI/CD basics

### Priority 3: Organize
1. **Create top-level README:**
   - Index of all tools
   - Quick reference guide
   - Getting started section

2. **Consolidate documentation:**
   - Centralize guides
   - Cross-reference related topics
   - Link to VSC official docs

3. **Version control:**
   - Move tools to Git repository
   - Enable collaborative updates
   - Track changes and versions

## Integration with Proposed Structure

### Link from Projects
```
projects/TEMPLATE/
├── tools -> ../../tools/  # Each project links to shared tools
└── scripts/               # Project-specific scripts
```

### Reference from Documentation
```
docs/
├── getting_started.md     # Links to tools/
├── data_management.md     # References vo_admin tools
└── hpc_usage.md          # References HPC templates
```

## Questions for VO Admin

1. **Maintenance:**
   - Who updates these tools?
   - Process for contributing improvements?

2. **Usage statistics:**
   - Are these tools actively used?
   - What's missing that users need?

3. **HPC changes:**
   - Any major VSC updates since 2021?
   - New features to document?

4. **ECMWF access:**
   - Do users still download ERA5 manually?
   - Or use pre-downloaded EXT/ERA5/?

5. **Training:**
   - Is gitdemo still used for onboarding?
   - Other training materials needed?

## Migration Complexity: LOW

### Why Simple
1. **Tiny size:** < 3 MB total
2. **No dependencies:** Self-contained scripts
3. **No data:** Only code and docs
4. **Clear purpose:** Well-defined utility
5. **Low risk:** Copies are safe, originals retained

### Migration Steps
1. Create updated `tools/` structure
2. Copy existing tools (< 1 minute)
3. Update README files (1-2 hours)
4. Test scripts on current systems (2-3 hours)
5. Announce updates to VO members

## Notes

- **High value-to-size ratio:** Small but useful
- **Onboarding critical:** Helps new users get started
- **Update recommended:** Content is dated but salvageable
- **Good foundation:** Structure is sound, needs refreshing
- **Consider Git:** Move to GitLab for collaborative maintenance
- **Link in docs:** Should be prominently referenced in documentation
- **Training opportunity:** Update materials for workshops
