# Helm Lint, Unittest and Build a Helm Chart

This actions install a helm chart's dependencies, including from a repo named `helm-private` which
is an authenticated neuxus helm repo.

This action assumes that `HELM_PRIVATE_REPO_URL`, `NEXUS3_USERNAME` and `NEXUS3_PASSWORD` environment
variables are available in the action to add the `helm-private` repo. It skips adding the
`helm-private` repo if it finds it in a charts dependencies.

It users a basic script to add dependencies which aims to avoid the need to manage a pre repo
repositories.yaml file and/or add helm repo add for each repo manually into GitHub Actions.

It then runs helm lint, helm unittest and packages the Chart ready for publishing by other tools
such as sematic-release.

Optionally pass HELM_LINT_ARG for extra args to helm lint.

## Example Usage:
uses: conversocial/helm-action@v1
