from .. import *

DEBUG = False
COMPRESS_ENABLED = True

# https only site
# See http://ponycheckup.com/
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'fluentdemo',
        'USER':     'fluentdemo',
        'PASSWORD': 'testtest',
    },
}

RAVEN_CONFIG = {
    'dsn': '',
}

INSTALLED_APPS += (
    #'raven.contrib.django.raven_compat',
    #'gunicorn',
)

TEMPLATES[0]['OPTIONS']['loaders'] = (
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
)

ALLOWED_HOSTS = (
    'demo.django-fluent.org',
)

CACHES['default']['KEY_PREFIX'] = 'fluentdemo.production'

GOOGLE_ANALYTICS_PROPERTY_ID = None  # TODO
