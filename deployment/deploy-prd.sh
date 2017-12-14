#!/bin/sh

if (( $# < 1 )); then
  echo "$0 image-tag [helm-args]" >&2
  exit 1
fi

CHART="./chart/"
RELEASE_NAME="demo-django-fluent-org"
TAG="$1"; shift

cd `dirname $0`
helm upgrade --install --reset-values "$RELEASE_NAME" "$CHART" -f "values-prd.yml" --set="imageTag=$TAG" "$@"
