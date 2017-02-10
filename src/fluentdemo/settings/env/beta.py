from .. import *

DEBUG = False
COMPRESS_ENABLED = True

# https only site
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

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
)

TEMPLATES[0]['OPTIONS']['loaders'] = (
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
)

ALLOWED_HOSTS = (
    'demo.django-fluent.org',
)

CACHES['default']['KEY_PREFIX'] = 'fluentdemo.beta'
