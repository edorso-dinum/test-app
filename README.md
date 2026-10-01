# test-app

Test application deployment configuration using Helm and Helmfile.

A small Django website (in `src/`) lists two sets of names, each stored in its own
PostgreSQL database (`premier_roles` and `doublures`) hosted by a CNPG cluster already
running on the target Kubernetes cluster. The seed data (`data/*.sql`) is loaded into
those databases as a migration step (a Helm pre-install/pre-upgrade `Job`) when the
`helm/website` chart is deployed.

## Building the Docker image

```bash
docker build -t <registry>/test-app/website:<tag> .
```

The image runs the Django app with `gunicorn`, listening on port `8000`.

## Helm charts

- `helm/nginx`: a basic NGINX deployment.
- `helm/website`: deploys the `test-app` website Docker image, wiring it to the two
  PostgreSQL databases via existing CNPG "app" Secrets (`postgresql.premierRoles.existingSecret`
  and `postgresql.doublures.existingSecret` in `values.yaml`), and loads `data/premier_roles.sql`
  / `data/doublure.sql` into those databases through a migration `Job` run on install/upgrade.

## Usage

A `Makefile` is available to lint, build, test, and render manifests for this project:

```bash
# Display help with available targets
make help

# Run all lint checks (yamllint, helm lint, helmfile lint)
make lint

# Build/package Helm charts and Helmfile state
make build

# Test Helm charts and Helmfile template rendering
make test

# Run all stages (lint, build, test)
make all

# Render Kubernetes manifests to stdout
make template

# Clean build artifacts
make clean
```
