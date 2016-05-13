from .. import *

DEBUG = False
COMPRESS_ENABLED = True

DATABASES = {
    'default': {
        # Choose between PostgreSQL or MySQL:
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'fluentdemo',
        'USER':     'fluentdemo',
        'PASSWORD': 'testtest',
    },
}

INSTALLED_APPS += (
    #'gunicorn',
)

TEMPLATES[0]['OPTIONS']['loaders'] = (
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
)

ALLOWED_HOSTS = (
    'demo.django-fluent.org',
)

CACHES['default']['KEY_PREFIX'] = 'fluentdemo.beta'
