from os.path import dirname, basename, realpath
import os
import sys


def bootstrap_wsgi_settings(wsgi_file):
    """
    Setup the base configuration:
    """
    project_folder = dirname(dirname(realpath(wsgi_file)))
    src_folder = dirname(project_folder)

    # Set startup settings
    # Avoid having to do this in the application server
    if src_folder not in sys.path:
        sys.path.append(src_folder)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fluentdemo.settings.env.docker')

    # Redirect print statements to apache log
    sys.stdout = sys.stderr
