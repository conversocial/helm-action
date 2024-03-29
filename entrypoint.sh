#!/bin/bash -ex
cd $GITHUB_WORKSPACE

helm repo add helm-private $HELM_PRIVATE_REPO_URL --username $NEXUS3_USERNAME --password $NEXUS3_PASSWORD

python3 /helm-repo-add.py

helm repo list

helm dependency build

helm lint $HELM_LINT_ARGS

helm unittest --helm3 .

helm package .
