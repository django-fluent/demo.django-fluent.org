"""Extra healthchecks to run"""
from django.conf import settings
import fluentdemo

try:
    with open(settings.SRC_DIR + '/.docker-git-version') as f:
        GIT_VERSION = f.read().strip()
except IOError:
    GIT_VERSION = fluentdemo.version_sha


def git_version():
    return GIT_VERSION or 'undefined'
