from . import *

# All environment settings can be overwritten with `docker run -e`

# Don't allow all hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['demo.django-fluent.org'])

# Change some defaults
DEBUG = env.bool('DJANGO_DEBUG', default=False)
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', not DEBUG)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', not DEBUG)

FLUENT_CONTENTS_CACHE_OUTPUT = env.bool('FLUENT_CONTENTS_CACHE_OUTPUT', not DEBUG)
FLUENT_CONTENTS_CACHE_PLACEHOLDER_OUTPUT = env.bool('FLUENT_CONTENTS_CACHE_PLACEHOLDER_OUTPUT', not DEBUG)

# Raven is only enabled in production to avoid warnings in development
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
    #'gunicorn',
)

# Keep templates in memory
TEMPLATES[0]['OPTIONS']['loaders'] = (
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
)
