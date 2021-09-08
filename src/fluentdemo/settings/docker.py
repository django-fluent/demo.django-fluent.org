from .production import *

ALLOWED_HOSTS.append('localhost')

# Safe defaults to allow startups without many settings.
CACHES['default'] = env.cache(default='locmemcache://')
CACHES['axes'] = env.cache(default='dummycache://')

# Need to different way to get the release, since there is no .git folder to read.
try:
    with open(SRC_DIR + '/.docker-git-version') as f:
        GIT_VERSION = f.read().strip()
except IOError:
    pass

SILENCED_SYSTEM_CHECKS = (
    'security.W001',  # SecurityMiddleware is handled by uWSGI instead.
    'security.W004',  # SECURE_HSTS_SECONDS is handled by uWSGI
    'security.W006',  # SECURE_CONTENT_TYPE_NOSNIFF is handled by uWSGI
    'security.W007',  # SECURE_BROWSER_XSS_FILTER is handled by uWSGI
    'security.W008',  # SECURE_SSL_REDIRECT is handled by uWSGI
)

# Docker sites typically run behind a HTTP proxy.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
