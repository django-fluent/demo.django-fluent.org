from .. import *

DEBUG = False
COMPRESS_ENABLED = True

DATABASES = {
    'default': {
        # Choose between PostgreSQL or MySQL:
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        #'ENGINE':   'django.db.backends.mysql',
        'NAME':     'fluentdemo',
        'USER':     'fluentdemo',
        'PASSWORD': '',
    },
}

INSTALLED_APPS += (
    #'gunicorn',
)

TEMPLATES[0]['OPTIONS']['loaders'] = (
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
)

ALLOWED_HOSTS = (
    'fluentdemo.testing.mycompany.tld',
)

CACHES['default']['KEY_PREFIX'] = 'fluentdemo.beta'
