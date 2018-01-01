from urlparse import urlparse
from .defaults import *

from fluentdemo.lib.healthchecks import git_version

# All environment settings can be overwritten with `docker run -e`

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['demo.django-fluent.org'])
ALLOWED_HOSTS.append('localhost')

DEBUG = env.bool('DJANGO_DEBUG', default=False)
COMPRESS_ENABLED = env.bool('COMPRESS_ENABLED', not DEBUG)

CACHES['default'] = env.cache(default='locmemcache://')
DATABASES['default'] = env.db(default='sqlite://' + ROOT_DIR + '/demo.db')
locals().update(env.email_url(default='consolemail://'))

# When the container restarts, and memcache still indicates the files are present,
# django-compressor will not recreate the files on the fly. Better use offline compression
CACHES['compressor'] = env.cache('COMPRESSOR_CACHE', 'locmemcache://')
COMPRESS_CACHE_BACKEND = 'compressor'
COMPRESS_CSS_HASHING_METHOD = 'hash'  # Not using mtime in case it differs between servers.
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'  # generate .gz too

RAVEN_CONFIG = {
    'dsn': env.str('SENTRY_DSN', default=''),
    'release': git_version(),
}

if 'redis' in CACHES['default']['BACKEND']:
    # Cache thumbnails in redis, avoids many db calls
    _redis_url = urlparse(CACHES['default']['LOCATION'])
    THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
    THUMBNAIL_REDIS_HOST = _redis_url.hostname
    THUMBNAIL_REDIS_PORT = int(_redis_url.port or 6379)
    THUMBNAIL_REDIS_DB = int(_redis_url.path.lstrip('/'))
    THUMBNAIL_REDIS_PASSWORD = CACHES['default'].get('OPTIONS', {}).get('PASSWORD', '')

if not DEBUG:
    # Production!
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
