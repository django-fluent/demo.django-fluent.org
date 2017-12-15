#!/bin/sh
cd `dirname $0`
for file in secrets/*.secrets
do
  basename="$(basename $file)"
  kubectl create secret generic "${basename%.*}" --from-env-file="$file" -o yaml --dry-run | kubectl apply -f -
done
