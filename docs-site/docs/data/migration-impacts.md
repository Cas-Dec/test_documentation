# Migration Impacts: What Changes for Your Code?

This page shows **concrete examples** of how the data reorganization affects different types of users and workflows. Most changes are minimal or can be handled with symlinks.

## Quick Summary

| Your Situation | Impact Level | What You Need to Do |
|----------------|--------------|---------------------|
| **Using external datasets** (ERA5, CHIRPS, etc.) | ⚠️ **Low** | Update paths once, benefits from better documentation |
| **Using generated datasets** (GLEAM, FLEXPART outputs) | ⚠️ **Low-Medium** | Update paths, use metadata to find versions |
| **Project-internal data only** | ✅ **None** | Your `projects/YOURPROJECT/internal/` unchanged |
| **Sharing data between projects** | ✅ **Better** | Easier discovery via catalog, avoid duplication |
| **Managing/producing datasets** | ⚠️ **Medium** | Need to create metadata.yaml and README |

---

## Scenario 1: Using External Data (e.g., ERA5)

### Before Migration

```python
#!/usr/bin/env python3
"""Load ERA5 temperature data - OLD VERSION"""
import xarray as xr

# Hardcoded path to wherever ERA5 was downloaded
era5_path = "/data/gent/vo/000/gvo00090/EXT/data/ERA5/by_var_nc/t2m_1hourly/"
t2m = xr.open_mfdataset(f"{era5_path}/t2m_*.nc")
```

**Issues with old approach:**
- No documentation - which version? which variables available?
- No contact info - who maintains this?
- Hardcoded absolute path - breaks if data moves
- Potential duplicates - multiple projects downloading same data

### After Migration (Option A: Update Path)

```python
#!/usr/bin/env python3
"""Load ERA5 temperature data - NEW VERSION (path update)"""
import xarray as xr
import os

# Use environment variable + standard location
base = os.environ['VSC_DATA_VO']
era5_path = f"{base}/shared/external/ERA5/by_var_nc/t2m_1hourly/"
t2m = xr.open_mfdataset(f"{era5_path}/t2m_*.nc")
```

**Benefits:**
- Portable across systems (uses `$VSC_DATA_VO`)
- Clear organization (`shared/external/`)
- Documented in catalog with metadata

### After Migration (Option B: Compatibility Symlink)

If updating paths is difficult, a symlink maintains backward compatibility:

```bash
# Symlink created during migration
/data/gent/vo/000/gvo00090/EXT/data/ERA5
  → /data/gent/vo/000/gvo00090/shared/external/ERA5
```

**Your old code still works:**
```python
# Old path still works via symlink
era5_path = "/data/gent/vo/000/gvo00090/EXT/data/ERA5/by_var_nc/t2m_1hourly/"
t2m = xr.open_mfdataset(f"{era5_path}/t2m_*.nc")
```

**Impact:** ✅ **Zero code changes needed** (symlink handles it)

---

## Scenario 2: Consolidated Duplicates (IGRA Example)

### Problem: Data Duplication

**Before migration**, IGRA radiosonde data existed in **3 locations**:
- `/data/gent/vo/000/gvo00090/D2D/data/IGRA_PAIRS_20190515/` (11 GB)
- `/data/gent/vo/000/gvo00090/D2D/data/IGRA_PAIRS_20190419/` (47 GB)
- `/data/gent/vo/000/gvo00090/FLEXPART/observations/IGRA_PAIRS_20190515/` (35 subdirs)

**Total duplication:** ~100 GB of wasted space!

### After Migration: Single Canonical Location

```
shared/observations/atmospheric/IGRA/
├── metadata.yaml          # Documents version, source, contact
├── README.md
├── v20190419/            # Older version
└── v20190515/            # Current version
```

**Projects link to shared location:**
```
projects/D2D/data/IGRA → $VSC_DATA_VO/shared/observations/atmospheric/IGRA/v20190515
projects/FLEXPART/observations/IGRA → (same symlink)
```

### Your Code Updates

**D2D project code:**
```python
# Before
igra_path = "/data/gent/vo/000/gvo00090/D2D/data/IGRA_PAIRS_20190515/"

# After (Option 1: use shared location directly)
import os
igra_path = os.path.join(os.environ['VSC_DATA_VO'],
                         "shared/observations/atmospheric/IGRA/v20190515")

# After (Option 2: use project symlink - no code change needed)
igra_path = "/data/gent/vo/000/gvo00090/projects/D2D/data/IGRA/"
# Symlink makes old path still work!
```

**FLEXPART project code:**
```python
# Before
igra_path = "/data/gent/vo/000/gvo00090/FLEXPART/observations/IGRA_PAIRS_20190515/"

# After (via project symlink)
igra_path = "/data/gent/vo/000/gvo00090/projects/FLEXPART/observations/IGRA/"
```

**Impact:** ⚠️ **Low** - Symlinks maintain compatibility, or one-line path update

**Benefits:**
- **100 GB saved** from de-duplication
- Single source of truth
- Version clearly documented
- Both projects stay in sync with updates

---

## Scenario 3: Project Using GLEAM Outputs

### Before Migration

```python
#!/usr/bin/env python3
"""Analyze GLEAM evapotranspiration - OLD VERSION"""
import xarray as xr

# Where is GLEAM? It's... somewhere in /GLEAM/data/ which is a symlink to scratch?
gleam_path = "/data/gent/vo/000/gvo00090/GLEAM/data/"
# Wait, or is it in D2D?
# gleam_path = "/data/gent/vo/000/gvo00090/D2D/data/GLEAM/"  # Another copy?

et = xr.open_dataset(f"{gleam_path}/E_2020_GLEAM_v3.8a.nc")
```

**Confusion:**
- Multiple GLEAM directories (`GLEAM/`, `D2D/data/GLEAM/`, `GLEAM-Hybrid/`, `GLEAM4_outputs/`)
- Which is current? Which version?
- Which one should I use?

### After Migration: Clear Structure

```
shared/generated/GLEAM/
├── metadata.yaml          # Clearly documents this is v3.8a, canonical location
├── README.md              # Usage examples, citation
├── v3.8a/                # Main version
│   ├── E_2020_GLEAM_v3.8a.nc
│   └── ...
└── experimental/          # Clearly marked non-production

shared/generated/GLEAM-Hybrid/
├── metadata.yaml          # Separate dataset with own docs
└── ...

projects/GLEAM/
├── internal/
│   ├── GLEAM4_dev/       # Development version
│   └── experiments/
└── shared → ../../shared/generated/GLEAM/  # Symlink to outputs
```

### Your Updated Code

```python
#!/usr/bin/env python3
"""Analyze GLEAM evapotranspiration - NEW VERSION"""
import xarray as xr
import os

# Clear, documented location
base = os.environ['VSC_DATA_VO']
gleam_path = f"{base}/shared/generated/GLEAM/v3.8a/"
et = xr.open_dataset(f"{gleam_path}/E_2020_GLEAM_v3.8a.nc")

# Can check metadata for version info, citation, contact
```

**Impact:** ⚠️ **Low-Medium** - Need to update path, but clearer which version to use

**Benefits:**
- **Clear versioning** - no confusion about which GLEAM
- **Documented** - metadata has citation, DOI, version info
- **No duplication** - D2D links to canonical location instead of copying

---

## Scenario 4: Producing/Sharing New Datasets

### Example: You Process ERA5-Land for Your Project

**Situation:** You've created bias-corrected ERA5-Land that other projects might use.

### Before Migration

```bash
# Where to put it? Personal directory? Project directory?
/data/gent/vo/000/gvo00090/vsc46240/myproject/era5land_corrected/

# Problems:
# - Hard for others to discover
# - No documentation of processing steps
# - Unclear if it's ready for use by others
```

### After Migration: Proper Shared Dataset

**1. Put data in right location:**
```bash
$VSC_DATA_VO/shared/processed/ERA5-Land_biascorrected/
```

**2. Create metadata.yaml:**
```yaml
dataset:
  name: ERA5-Land_biascorrected
  version: "1.0"
  description: >
    ERA5-Land daily temperature bias-corrected against Belgian station
    observations using quantile mapping.

source:
  provider: Processed from ERA5-Land
  license: CC BY 4.0

contact:
  name: Your Name
  email: your.email@ugent.be
  vsc_username: vsc46240

history:
  - date: "2026-09-15"
    description: Processed ERA5-Land with quantile mapping bias correction
    source: https://github.com/yourorg/bias-correction/blob/main/process.py
```

**3. Add README.md with usage example**

**4. Your project links to it:**
```bash
projects/MYPROJECT/
├── internal/              # Your working code
├── scripts/
└── data/
    └── era5land_corrected → ../../../shared/processed/ERA5-Land_biascorrected/
```

**Impact:** ⚠️ **Medium** - Need to create documentation

**Benefits:**
- **Discoverable** - Appears in catalog automatically
- **Citable** - Metadata includes processing DOI
- **Reproducible** - History links to processing code
- **No duplication** - Others link instead of copying

---

## Scenario 5: Managing Large Project (SNOWSHOP Example)

### Before Migration: Ad-hoc Organization

```
/data/gent/vo/000/gvo00090/SNOWSHOP/
├── Sentinel1/            # Is this production or experimental?
├── WetSnow/              # Different user, different project?
├── AlphaEarth/           # ML experiments
├── measurements/         # In-situ data
├── Forcings/             # Meteorology
├── pythonenv/            # Should this be here?
└── .snap/                # Cache files mixed with data
```

**Issues:**
- Unclear what's production vs. experimental
- Hard to know what's safe to use
- Processing artifacts mixed with data
- No clear entry point for new users

### After Migration: Organized Structure

```
shared/
├── generated/SNOWSHOP/
│   ├── Sentinel1/                    # Production output
│   │   ├── metadata.yaml             # Documented!
│   │   ├── README.md                 # Usage examples
│   │   └── g0_100m/
│   └── snowcover/                    # Other production products
└── observations/
    ├── ground/snow/ → SNOWSHOP measurements
    └── lidar/snow/ → SNOWSHOP lidar

projects/SNOWSHOP/
├── README.md                          # Project overview
├── internal/
│   ├── WetSnow/                      # Active research
│   ├── AlphaEarth/                   # ML experiments
│   └── experiments/
├── forcings/                          # Input data
├── processing/
│   └── cache/                        # Temp/cache (not backed up)
└── shared → ../../shared/generated/SNOWSHOP/  # Links to outputs
```

### User Impact

**For production users:**
```python
# Clear, documented access to production data
import os
base = os.environ['VSC_DATA_VO']
s1_path = f"{base}/shared/generated/SNOWSHOP/Sentinel1/g0_100m/"

# Metadata tells you:
# - Coverage (Alps, Andes, Nordic)
# - Version (1.0)
# - Contact (vsc40471)
# - Citation (pending publication)
# - Related validation data
```

**For SNOWSHOP team members:**
```bash
# Clear separation: production vs. experiments
cd $VSC_DATA_VO/projects/SNOWSHOP/internal/WetSnow/  # Experiments
cd $VSC_DATA_VO/projects/SNOWSHOP/shared/            # Production outputs
```

**Impact:** ⚠️ **Low for users, Medium for maintainers**

**Benefits:**
- Clear production/experimental separation
- New users know what's safe to use
- Documented with metadata
- Easier onboarding

---

## Scenario 6: Multi-Project Workflows

### Example: Heat Wave Analysis Using Multiple Datasets

**Before migration - data detective work:**
```python
# Where is everything?
era5_path = "/data/gent/vo/000/gvo00090/EXT/data/ERA5/???"  # Where exactly?
gleam_path = "/data/gent/vo/000/gvo00090/GLEAM/data/"      # Is this current?
stations_path = "???"  # Where are station obs?

# Each dataset: different structure, no docs, unclear versions
```

**After migration - clear catalog:**

```python
#!/usr/bin/env python3
"""Heat wave analysis using multiple datasets"""
import os

base = os.environ['VSC_DATA_VO']

# All datasets documented in catalog at docs-site
# Clear paths, versions, citation info
era5 = f"{base}/shared/external/ERA5/by_var_nc/t2m_1hourly/"
gleam = f"{base}/shared/generated/GLEAM/v3.8a/"
stations = f"{base}/shared/observations/ground/meteorology/belgium/"

# Metadata tells you:
# - Compatible time periods
# - Spatial resolution differences
# - How to cite each
# - Who to contact with questions
```

**Impact:** ✅ **Better** - Easier to discover and combine datasets

---

## Storage Savings From Consolidation

Based on current inventories:

| Duplicate Data | Original Locations | New Location | Space Saved |
|----------------|-------------------|--------------|-------------|
| **IGRA soundings** | D2D (58 GB), FLEXPART (duplicate) | `shared/observations/atmospheric/IGRA/` | **~58 GB** |
| **GLEAM** | GLEAM/, D2D/GLEAM/ (184 GB) | `shared/generated/GLEAM/` (link from D2D) | **~184 GB** |
| **ERA5** | EXT/ERA5/, HEAT/ERA5_old/ (1.5 TB), HEAT/arco-era5 (4.1 TB)? | Consolidate or clarify | **TBD** |
| **Total estimated savings** | | | **~250+ GB** |

---

## Migration Tools & Support

### Path Translation Helper

We provide a script to help update paths in your code:

```bash
# Scan your code for old paths and suggest updates
python $VSC_DATA_VO/tools/migration/scan_paths.py ~/myproject/

# Output:
# Found 3 old paths:
#  - scripts/download.py:15: /data/.../EXT/data/ERA5/
#    → Suggest: $VSC_DATA_VO/shared/external/ERA5/
#  - analysis/load_data.py:42: /data/.../GLEAM/data/
#    → Suggest: $VSC_DATA_VO/shared/generated/GLEAM/v3.8a/
```

### Compatibility Symlinks

For datasets you can't update immediately, symlinks preserve old paths:

```bash
# Old path still works during transition period
/data/gent/vo/000/gvo00090/EXT/data/ERA5/
  → /data/gent/vo/000/gvo00090/shared/external/ERA5/
```

### Find Datasets via Catalog

Browse the [data catalog](../datasets/index.md) to discover available datasets with full metadata.

---

## Timeline & Transition Period

1. **Phase 1 (Months 1-2):** Create `shared/` structure, add metadata
2. **Phase 2 (Months 3-4):** Create symlinks, both old and new paths work
3. **Phase 3 (Months 5-6):** Encourage users to update to new paths
4. **Phase 4 (Month 12+):** Deprecate old paths (with advance notice)

**You have time** to update your code gradually!

---

## Questions?

- **"My code breaks!"** → Check if symlinks are in place, or consult migration guide
- **"Where did dataset X go?"** → Check the [catalog](../datasets/index.md)
- **"Who maintains dataset Y?"** → Check its `metadata.yaml` contact field
- **"How do I share my data?"** → See [metadata spec](metadata-spec.md) and contact VO admin

For help: email VO admin or check dataset-specific contact in metadata.yaml
