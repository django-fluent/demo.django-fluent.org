from .defaults import *

# All environment settings can be overwritten with `docker run -e`

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['demo.django-fluent.org'])
ALLOWED_HOSTS.append('localhost')

DEBUG = env.bool('DJANGO_DEBUG', default=False)

CACHES['default'] = env.cache(default='locmemcache://')
DATABASES['default'] = env.db(default='sqlite://' + ROOT_DIR + '/demo.db')

if not DEBUG:
    # Production!
    COMPRESS_ENABLED = True
    FLUENT_CONTENTS_CACHE_OUTPUT = True
    FLUENT_CONTENTS_CACHE_PLACEHOLDER_OUTPUT = True

    # https only site, see http://ponycheckup.com/
    CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', True)
    SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', True)

    # SSL settings
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Optimize template loading.
    TEMPLATES[0]['OPTIONS']['loaders'] = (
        ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
    )
