#!/bin/sh

cd `dirname $0/..`
docker build -t demo.django-fluent.org .
