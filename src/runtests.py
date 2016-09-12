#!/usr/bin/env python
import sys
import os
from django.conf import settings
from django.core.management import execute_from_command_line

if not settings.configured:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fluentdemo.settings.env.unittest")

DEFAULT_TEST_APPS = [
    'apps',
    'frontend',
]


def runtests():
    other_args = filter(lambda arg: arg.startswith('-'), sys.argv[1:])
    test_apps = filter(lambda arg: not arg.startswith('-'), sys.argv[1:]) or DEFAULT_TEST_APPS
    argv = sys.argv[:1] + ['test', '--traceback'] + other_args + test_apps
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
