# Overview

This site documents how data is organized on the lab's shared VO storage
(`$VSC_DATA_VO`), and how to find, understand, and correctly cite any
dataset on it.

!!! note "This is a local proof-of-concept"
    This particular deployment of the site is generated from example data
    checked into the `hpc-docs` repository, standing in for the real
    `$VSC_DATA_VO` while the cluster is offline. See the repo root
    `README.md` for what's real vs. illustrative.

## Where things live

- **[Folder structure](structure.md)** — the `shared/` / `projects/` /
  `personal/` layout, and which one your data belongs in.
- **[Dataset metadata spec](metadata-spec.md)** — the `metadata.yaml`
  fields every shared dataset must fill in, and how it's validated.
- **[Data catalog](../datasets/index.md)** — every dataset currently under
  `shared/`, generated automatically from each dataset's `metadata.yaml`.
- **[Migrating personal code](migration-guide.md)** — worked examples of
  what changes (often nothing but a symlink) in your own analysis code
  when a dataset you depend on moves.

## Getting help

Every dataset's `metadata.yaml` has a `contact` field — that's who to
reach out to if something about the data is unclear. For anything about
the reform or this site itself, see the contact info in the root
`README.md`.
