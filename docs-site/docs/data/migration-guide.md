# Migrating personal code

When a dataset you depend on moves under the reform, your own analysis
code on `$VSC_SCRATCH` or in a project folder needs to keep working. In
most cases that's a symlink and nothing else. This page walks through a
worked example; the full runnable code is in
[`VSC_SCRATCH_USER/example_project/`](https://github.com/h-cel/hpc-docs/tree/main/VSC_SCRATCH_USER/example_project)
in the repo.

## Scenario 1 — the dataset only moved: use a symlink

GLEAM output moved from a flat `$VSC_DATA_VO/GLEAM/` to
`$VSC_DATA_VO/shared/generated/GLEAM/`, keeping the same simple
one-file-per-variable layout. Before:

```python
data_dir = VSC_DATA_VO / "GLEAM"
files = sorted(data_dir.glob("*.nc"))
```

Create a symlink once, in your own project directory:

```bash
ln -s "$VSC_DATA_VO/shared/generated/GLEAM" ./data
```

...and the only change to the code is what `data_dir` points at:

```python
data_dir = Path(__file__).parent / "data" / "daily" / "E"
files = sorted(data_dir.glob("*.nc"))
```

The glob logic doesn't change, because the thing that moved is *where*
the folder is, not *what's inside it*. This covers the majority of
migrations — old project-local absolute paths become a symlink plus one
path constant.

## Scenario 2 — the dataset was renamed/restructured: symlinks aren't enough

ERA5 became `ERA5-Land` and switched from one flat folder to a
subfolder-per-variable layout with CF-style filenames. Before:

```python
data_dir = VSC_DATA_VO / "EXT" / "ERA5"
files = sorted(data_dir.glob(f"ERA5_{variable}_*.nc"))
```

A symlink at `shared/external/ERA5-Land` doesn't help here — the dataset
name, the subfolder layout, and the filename pattern all changed. The
glob itself has to be updated:

```python
data_dir = VSC_DATA_VO / "shared" / "external" / "ERA5-Land" / "hourly" / variable
files = sorted(data_dir.glob(f"{variable}_ERA5-Land_*_*.nc"))
```

## Rule of thumb

| What changed | Fix |
|---|---|
| Only the dataset's location | Symlink, no code change |
| Dataset renamed | Symlink target name changes; code often unaffected if you use a path variable |
| Layout restructured (e.g. new subfolder per variable) | Code that searches for files must change |
| Filename convention changed (e.g. adopted CF naming) | Code that parses/globs filenames must change |

Always check the dataset's `README.md`/`metadata.yaml` in its new
location under `shared/` for the current layout before updating your
glob patterns — see the [data catalog](../datasets/index.md).
