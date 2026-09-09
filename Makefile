SHELL                 := /bin/bash
HELM                  ?= helm
HELMFILE              ?= helmfile
YAMLLINT              ?= yamllint
HELMFILE_FILE         ?= helmfiles/helmfile.yaml.gotmpl
HELMFILE_ENVIRONMENT  ?= default
CHARTS_DIR            ?= helm
BUILD_DIR             ?= dist

.PHONY: all help lint lint-helm lint-helmfile lint-yaml build build-helm build-helmfile package test test-helm test-helmfile template deps clean

all: lint build test

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

## Linting
lint: lint-yaml lint-helm lint-helmfile ## Run all linters (yaml, helm, helmfile)

lint-yaml: ## Lint YAML files with yamllint
	@if command -v $(YAMLLINT) >/dev/null 2>&1; then \
		echo "==> Running yamllint..."; \
		$(YAMLLINT) .; \
	else \
		echo "yamllint not found, skipping YAML linting"; \
	fi

lint-helm: ## Lint Helm charts
	@echo "==> Linting Helm charts..."
	@for chart in $(CHARTS_DIR)/*; do \
		if [ -d "$$chart" ] && [ -f "$$chart/Chart.yaml" ]; then \
			$(HELM) lint "$$chart"; \
		fi \
	done

lint-helmfile: ## Lint Helmfile releases
	@echo "==> Linting Helmfile..."
	$(HELMFILE) -e $(HELMFILE_ENVIRONMENT) -f $(HELMFILE_FILE) lint

## Building / Packaging
build: build-helm build-helmfile ## Build Helm charts and Helmfile state

build-helm package: ## Package Helm charts into archive files
	@echo "==> Packaging Helm charts to $(BUILD_DIR)..."
	@mkdir -p $(BUILD_DIR)
	@for chart in $(CHARTS_DIR)/*; do \
		if [ -d "$$chart" ] && [ -f "$$chart/Chart.yaml" ]; then \
			$(HELM) package "$$chart" -d $(BUILD_DIR); \
		fi \
	done

build-helmfile: ## Build Helmfile state
	@echo "==> Building Helmfile state..."
	$(HELMFILE) -e $(HELMFILE_ENVIRONMENT) -f $(HELMFILE_FILE) build

## Testing / Template validation
test: test-helm test-helmfile ## Test Helm charts and Helmfile template rendering

test-helm: ## Test Helm chart template rendering
	@echo "==> Testing Helm chart templates..."
	@for chart in $(CHARTS_DIR)/*; do \
		if [ -d "$$chart" ] && [ -f "$$chart/Chart.yaml" ]; then \
			$(HELM) template "$$chart" > /dev/null; \
		fi \
	done

test-helmfile: ## Test Helmfile template rendering
	@echo "==> Testing Helmfile template rendering..."
	$(HELMFILE) -e $(HELMFILE_ENVIRONMENT) -f $(HELMFILE_FILE) template > /dev/null

## Utilities
template: ## Render Helmfile manifests to stdout
	$(HELMFILE) -e $(HELMFILE_ENVIRONMENT) -f $(HELMFILE_FILE) template

deps: ## Update Helm chart dependencies
	@echo "==> Updating dependencies..."
	@for chart in $(CHARTS_DIR)/*; do \
		if [ -d "$$chart" ] && [ -f "$$chart/Chart.yaml" ]; then \
			$(HELM) dependency update "$$chart" 2>/dev/null || true; \
		fi \
	done
	$(HELMFILE) -e $(HELMFILE_ENVIRONMENT) -f $(HELMFILE_FILE) deps 2>/dev/null || true

clean: ## Clean build artifacts
	@echo "==> Cleaning build artifacts..."
	rm -rf $(BUILD_DIR) *.tgz
