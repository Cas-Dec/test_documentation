# Folder structure

`$VSC_DATA_VO` is split into three top-level areas:

```text
$VSC_DATA_VO/
├── shared/
│   ├── external/        # raw datasets, no processing (ERA5-Land, MODIS_BA, ...)
│   ├── processed/        # processed from external data, useful for everyone
│   └── generated/        # internally generated, used across teams (GLEAM, FLEXPART, ...)
├── projects/
│   ├── GLEAM/
│   │   ├── internal/
│   │   └── shared/ -> $VSC_DATA_VO/shared/generated/GLEAM   (symlink)
│   ├── HEAT/
│   └── ...
└── personal/
    ├── <vsc_username_1>/
    └── ...
```

## Which folder does my data belong in?

- **It's raw data you downloaded from an external provider, unchanged?**
  → `shared/external/<dataset>/`
- **You processed/derived it from external data, and it's useful beyond
  your own project?** → `shared/processed/<dataset>/`
- **It's generated in-house (a model run, a reanalysis post-processing
  step, ...) and more than one project/team uses it?** →
  `shared/generated/<dataset>/`
- **It only matters to your project?** → `projects/<your_project>/internal/`
  — no `metadata.yaml`, no catalog entry, do whatever your project needs.
- **It's your own scratch/working files, not tied to a specific
  project?** → `personal/<your_vsc_username>/`

If a project *produces* something that belongs in `shared/`, keep the
canonical copy in `shared/` and symlink it back into the project folder
(see `projects/GLEAM/shared` above) rather than duplicating it. That way
there's only ever one copy on disk, and the dataset still gets picked up
by the automated catalog scan.

Everything under `shared/` is expected to have a `metadata.yaml` and a
`README.md` — see [Dataset metadata spec](metadata-spec.md). Nothing
under `projects/` or `personal/` is scanned or requires either.
