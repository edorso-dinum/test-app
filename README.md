# test-app

Test application deployment configuration using Helm and Helmfile.

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
