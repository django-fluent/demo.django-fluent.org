import environ
from .production import *

env = environ.Env()

# Allow to override settings via `docker run -e`
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=ALLOWED_HOSTS + ('localhost',))
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', True)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', True)

DATABASES['default'] = env.db(default='postgresql://postgres/fluentdemo')
CACHES['default'] = env.cache(default='locmemcache://')
locals().update(env.email_url(default='consolemail://'))

# SSL settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

if 'THUMBNAIL_REDIS_URL' in env.ENVIRON:
    # Allow thumbnails to exist in redis cache
    redis_cache = env.cache('THUMBNAIL_REDIS_URL', default='rediscache://localhost:6379:1')

    THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
    THUMBNAIL_REDIS_HOST = redis_cache['LOCATION'].split(':')[0]
    THUMBNAIL_REDIS_DB = redis_cache['LOCATION'].split(':')[2]
