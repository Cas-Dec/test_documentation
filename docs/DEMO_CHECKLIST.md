# Demo Checklist: HPC Data Documentation Site

## Quick Start

```bash
cd /kyukon/scratch/gent/vo/000/gvo00090/vsc46240/PhD/HPC-docs
./build_and_serve.sh
# Choose option 1, then open http://localhost:8000
```

## What to Show Colleagues

### 1. **Navigation & Overview** (2 min)
- [ ] Start at home page - show overall concept
- [ ] Navigate to "Folder structure" - explain shared/projects/personal
- [ ] Show "Dataset metadata spec" - what's required

### 2. **Data Catalog** (3 min)
- [ ] Open "Data catalog" page
- [ ] Show organized categories (external, generated, observations, processed)
- [ ] Click on **ERA5** - show complete metadata
- [ ] Click on **SNOWSHOP Sentinel-1** - show major generated product
- [ ] Click on **IGRA** - highlight consolidation from duplicates

### 3. **Migration Impacts** (10 min) ⭐ **Main Event**

Navigate to "Migration impacts" page and walk through:

#### Scenario 1: Using External Data
- [ ] Show before/after code for ERA5
- [ ] Explain two options: path update OR symlink
- [ ] Emphasize: **backward compatible**

#### Scenario 2: Consolidated Duplicates (IGRA)
- [ ] Highlight the problem: 3 copies, 100 GB wasted
- [ ] Show the solution: single location, symlinks
- [ ] Point out: **~100 GB saved from one dataset!**
- [ ] Show code updates are minimal

#### Scenario 3: GLEAM Confusion
- [ ] Show before: multiple GLEAM dirs, unclear which to use
- [ ] Show after: clear versioning, single canonical location
- [ ] Benefits: no confusion, proper citation

#### Scenario 6: Storage Savings Table
- [ ] Scroll to "Storage Savings From Consolidation" table
- [ ] Highlight: **~250+ GB total savings**
- [ ] Point out: just from eliminating known duplicates!

### 4. **Real Examples from Inventories** (5 min)

Show that these aren't hypothetical:
- [ ] Point to SNOWSHOP inventory (4949 Sentinel-1 tiles)
- [ ] Point to D2D/FLEXPART IGRA duplication (real issue)
- [ ] Show HEAT ERA5 potential duplication (4.1 TB arco-era5)

### 5. **Key Selling Points** (5 min)

Emphasize:
- [ ] **Minimal disruption**: Symlinks mean old code keeps working
- [ ] **Storage savings**: 250+ GB recovered (and counting)
- [ ] **Better discovery**: Searchable catalog vs. hunting for data
- [ ] **Documentation**: Every dataset has metadata, citation, contact
- [ ] **Gradual migration**: 6-12 month timeline, no rush
- [ ] **Production clarity**: Know what's stable vs. experimental

### 6. **Timeline & Support** (2 min)
- [ ] Show proposed timeline at bottom of migration-impacts page
- [ ] Emphasize transition period where both paths work
- [ ] Mention migration helper tools (path scanner script)

## Key Statistics to Mention

| Metric | Value |
|--------|-------|
| Datasets documented (so far) | 8 examples |
| Storage saved from de-duplication | ~250+ GB |
| Projects inventoried | 8 (EXT, GLEAM, HEAT, FLEXPART, SNOWSHOP, D2D, BUCCS, tools) |
| Largest dataset | SNOWSHOP Sentinel-1 (2 TB, 4949 tiles) |
| Biggest single duplicate | IGRA (~100 GB) |
| Transition period | 6-12 months |

## Common Questions & Answers

**Q: "Do I have to rewrite all my code?"**
A: No! Symlinks maintain backward compatibility. Update gradually or not at all.

**Q: "What if I'm in the middle of a project?"**
A: Keep using current paths. Symlinks ensure no disruption.

**Q: "How much work is creating metadata?"**
A: 10-15 minutes per dataset using template. Most info already known.

**Q: "What if data moves again?"**
A: Using `$VSC_DATA_VO` environment variable makes code portable.

**Q: "Can I still have project-internal data?"**
A: Absolutely! `projects/YOURPROJECT/internal/` is unchanged, no docs required.

**Q: "What about data that's not ready to share?"**
A: Keep in `projects/*/internal/`. Only `shared/` requires metadata.

## Follow-up Actions

After demo, propose:
1. [ ] Get feedback on migration timeline
2. [ ] Identify volunteers for pilot migration (BUCCS? tools?)
3. [ ] Schedule follow-up to discuss specific concerns
4. [ ] Set date for next phase (stakeholder outreach)

## Fallback: If MkDocs Not Available

If can't serve the site, show directly:
1. Open `docs-site/docs/migration-impacts.md` in editor
2. Walk through scenarios 1, 2, and 6
3. Show storage savings table
4. Open example metadata.yaml files to show structure

---

**Estimated total demo time: 25-30 minutes**
**Core message: Better organization, storage savings, minimal disruption**
