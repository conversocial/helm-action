#!/bin/bash
TAG=$1
# TODO move this to GitHub's container registery
docker build -f Dockerfile.publish  . -t helm-action:$TAG
docker tag helm-action:$TAG conversocial/helm-action:$TAG
docker push conversocial/helm-action:$TAG
