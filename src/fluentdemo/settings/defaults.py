"""
The settings for this project.
"""
import environ
import os
import re

from django.utils.translation import ugettext_lazy as _

import fluentdemo

env = environ.Env()

# --- Environment

SITE_ID = 1
DEBUG = env.bool('DJANGO_DEBUG', True)

SRC_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
ROOT_DIR = os.path.dirname(SRC_DIR)

# Paths
MEDIA_ROOT   = ROOT_DIR + '/web/media/'
MEDIA_URL    = '/media/'        # Must end with /
ROOT_URLCONF = 'fluentdemo.urls'

STATIC_ROOT = ROOT_DIR + '/web/static/'
STATIC_URL  = '/static/'

# --- Locale settings

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Amsterdam'

LANGUAGES = (
    # These are all languages that content can be written in.
    ('en', _('English')),  # Primary language first
    ('nl', _('Dutch')),
)

USE_I18N = True                   # False for optimizations
USE_L10N = True
USE_TZ = True

# --- Email

ADMINS = (
    ('fluentdemo', 'sysadmin@django-fluent.org'),
)
MANAGERS = ADMINS

SERVER_EMAIL = 'sysadmin@django-fluent.org'
DEFAULT_FROM_EMAIL = 'info@django-fluent.org'
EMAIL_SUBJECT_PREFIX = '[Django][fluentdemo] '

# --- Security

SECRET_KEY = env.str('DJANGO_SECRET_KEY', 'c3#r=h50=zuea%=0-9mx@gf2l0*m^yhmy_hi_0-oc98+1by2so')
SESSION_COOKIE_HTTPONLY = True  # can't read cookie from JavaScript
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', False)

CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', False)

X_FRAME_OPTIONS = 'SAMEORIGIN'  # Prevent iframes. Can be overwritten per view using the @xframe_options_.. decorators

INTERNAL_IPS = ('127.0.0.1',)

IGNORABLE_404_URLS = (
    re.compile(r'^favicon.ico$'),
    # re.compile(r'^/favicon.ico$'),
    # re.compile(r'^/wp-login.php$'),
)

# --- Plugin components

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'compressor',

    # Site parts
    'frontend',
    'fluentdemo.apps.blog',
    'fluentdemo.apps.wysiwyg_config',

    # CMS parts
    'fluent_blogs',
    'fluent_blogs.pagetypes.blogpage',
    'fluent_pages',
    'fluent_pages.pagetypes.fluentpage',
    'fluent_pages.pagetypes.flatpage',
    'fluent_pages.pagetypes.redirectnode',
    'fluent_pages.pagetypes.textfile',
    'fluent_comments',
    'fluent_contents',
    'fluentcms_emailtemplates',
    'fluentcms_emailtemplates.plugins.emailtext',

    # CMS plugins
    'fluent_contents.plugins.code',
    'fluent_contents.plugins.commentsarea',
    'fluent_contents.plugins.googledocsviewer',
    'fluent_contents.plugins.iframe',
    'fluent_contents.plugins.markup',
    'fluent_contents.plugins.oembeditem',
    'fluent_contents.plugins.picture',
    'fluent_contents.plugins.rawhtml',
    'fluent_contents.plugins.sharedcontent',
    'fluent_contents.plugins.text',
    'fluentcms_button',
    'fluentcms_contactform',
    'fluentcms_cookielaw',
    'fluentcms_countdown',
    'fluentcms_file',
    'fluentcms_forms_builder',
    'fluentcms_googlemaps',
    'fluentcms_jumbotron',
    # 'fluentcms_link',
    'fluentcms_pager',
    'fluentcms_privatenotes',
    'fluentcms_teaser',
    'fluentcms_twitterfeed',

    # Support libs
    'analytical',
    'any_imagefield',
    'any_urlfield',
    'axes',
    'captcha',
    'categories_i18n',
    'crispy_forms',
    'django_comments',
    'django_wysiwyg',
    'filebrowser',
    'forms_builder.forms',
    'geoposition',  # for map picker
    'mptt',
    'parler',
    'polymorphic',
    'polymorphic_tree',
    'slug_preview',
    'staff_toolbar',
    'sorl.thumbnail',
    'taggit',
    'taggit_selectize',
    'tinymce',

    # and enable the admin
    'fluent_dashboard',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
)

FORMAT_MODULE_PATH = 'fluentdemo.settings.locale'  # Consistent date formatting

LOCALE_PATHS = (
    os.path.join(SRC_DIR, 'locale'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE = MIDDLEWARE_CLASSES = (
    'raven.contrib.django.middleware.SentryMiddleware',  # make 'request' available on all logs.
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',  # on 404, report to sentry.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # calls translation.activate() based on the URL
    'fluent_contents.middleware.HttpRedirectRequestMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (),
        'OPTIONS': {
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'admin_tools.template_loaders.Loader',  # Allow {% extends "appname:template" %}
            ),
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'frontend.context_processors.frontend',
            ),
        },
    },
]

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# --- Services

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

CACHES = {
    'default': env.cache(default='redis://127.0.0.1:6379/1?TIMEOUT=86400&KEY_PREFIX=fluentdemo'),
}

DATABASES = {
    'default': env.db(default='postgresql://fluentdemo:testtest@localhost/fluentdemo'),
}

locals().update(env.email_url(default='smtp://'))

RAVEN_CONFIG = {
    'dsn': env.str('SENTRY_DSN', default=''),
    'release': fluentdemo.version_sha,
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': u'%(levelname)s: %(asctime)s %(process)d %(thread)d %(module)s: %(message)s',
        },
        'simple': {
            'format': u'%(levelname)s:\t%(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db': {
            'handlers': ['console'],
            'level': 'ERROR',  # to show queries or not.
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

# --- Third party app settings

ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

AXES_LOGIN_FAILURE_LIMIT = 6
AXES_COOLOFF_TIME = 1  # hours
AXES_IP_WHITELIST = INTERNAL_IPS

CRISPY_TEMPLATE_PACK = 'bootstrap3'

CAPTCHA_NOISE_FUNCTIONS = ()
CAPTCHA_FONT_SIZE = 30
CAPTCHA_LETTER_ROTATION = (-10,10)

COMMENTS_APP = 'fluent_comments'

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
)

COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.JSMinFilter',
)

COMPRESS_ENABLED = env.bool('COMPRESS_ENABLED', not DEBUG)

DJANGO_WYSIWYG_FLAVOR = 'tinymce_advanced'

FILE_UPLOAD_PERMISSIONS = 0o644  # Avoid 600 permission for filebrowser uploads.

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.png', '.gif'],
    'Document': ['.pdf', '.doc', '.xls', '.csv', '.docx', '.xlsx'],
    'Video': ['.swf', '.mp4', '.flv', '.f4v', '.mov', '.3gp'],
}
FILEBROWSER_EXCLUDE = ('cache', '_versions', '_admin_thumbnail\.', '_big\.', '_large\.', '_medium\.', '_small\.', '_thumbnail\.')
FILEBROWSER_MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # in bytes
FILEBROWSER_STRICT_PIL = True
FILEBROWSER_ADMIN_VERSIONS = [
    'thumbnail',
    #'small',
    #'medium',
    #'big',
    #'large',
]
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'
FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large', 'width': 680, 'height': '', 'opts': ''},
}

FLUENT_BLOGS_ENTRY_MODEL = 'blog.Post'
FLUENT_BLOGS_ENTRY_LINK_STYLE = '/{year}/{month}/{slug}/'

FLUENT_COMMENTS_USE_EMAIL_NOTIFICATION = False  # not in demo!

FLUENT_COMMENTS_MODERATE_AFTER_DAYS = 30
FLUENT_COMMENTS_FORM_CLASS = 'fluentdemo.apps.blog.forms.CommentForm'
FLUENT_COMMENTS_FIELD_ORDER = ('comment', 'name', 'email', 'url')
FLUENT_COMMENTS_MODERATE_BAD_WORDS = ()

FLUENT_CONTENTS_CACHE_OUTPUT = True
FLUENT_CONTENTS_CACHE_PLACEHOLDER_OUTPUT = False  # Not in dev.

FLUENTCMS_CONTACTFORM_DEFAULT_FIELDS = ('name', 'email', 'phone_number', 'message')

text_plugins = ('TextPlugin', 'PicturePlugin', 'OEmbedPlugin', 'RawHtmlPlugin', 'ButtonPlugin', 'PrivateNotesPlugin',)
FLUENT_CONTENTS_PLACEHOLDER_CONFIG = {
    # This limits which plugins can be used for certain placeholder slots.
    'homepage': {
        'plugins': text_plugins + (
            # The homepage has a restricted set of elements you can use.
            'SharedContentPlugin',
            'JumbotronPlugin',
            'CountDownPlugin',
            'TeaserPlugin',
        ),
    },
    'main': {
        'plugins': text_plugins + (
            # Allow a lot of content in the main area.
            'SharedContentPlugin',
            'ContactFormPlugin',
            'FormPlugin',
            'CountDownPlugin',
            'TwitterRecentEntriesPlugin',
            'TwitterSearchPlugin',
            'FilePlugin',
            #'LinkPlugin',
            'MapPlugin',
            'TeaserPlugin',
            'PagerPlugin',
            'RestructuredtextMarkupPlugin',
            'MarkdownMarkupPlugin',
        ),
    },
    'blog_contents': {
        'plugins': text_plugins + (
            # Allow a lot of content in the main area.
            'SharedContentPlugin',
            'FilePlugin',
            # 'LinkPlugin',
            'MapPlugin',
            'RestructuredtextMarkupPlugin',
            'MarkdownMarkupPlugin',
            'IframePlugin',
        ),
    },
    'blog_sidebar': {
        'plugins': text_plugins + (
            # Allow a lot of content in the main area.
            'SharedContentPlugin',
            'CountDownPlugin',
            'TwitterRecentEntriesPlugin',
            'TwitterSearchPlugin',
        ),
    },
    'all': {
        # no restrictions here
    },
    'shared_content': {
        'plugins': text_plugins + (
            # The shared content doesn't allow embedding itself,
            # and deals with elements that can be shown everywhere.
            'CookieLawPlugin',
        ),
    }
}

FLUENT_DASHBOARD_APP_ICONS = {
    'blog/post': 'newspaper1.png',
}
FLUENT_DASHBOARD_DEFAULT_MODULE = 'ModelList'
FLUENT_DASHBOARD_APP_GROUPS = (
    (_('CMS'), {
        'models': [
            "fluent_pages.models.db.Page",
            "fluent_blogs.*",
            "fluent_faq.models.FaqQuestion",
            'fluentdemo.apps.blog.*',
            'fluentdemo.apps.news.*',
            'django.contrib.redirects.*',
        ],
        'module': 'fluent_dashboard.modules.CmsAppIconList',
        'collapsible': False,
    }),
    (_('Content Library'), {
        'models': [
            'fluent_contents.*',
            'fluentcms_googlemaps.*',
            'forms_builder.forms.*',
            "filebrowser.*",
        ],
        'module': 'fluent_dashboard.modules.CmsAppIconList',
        'collapsible': False,
    }),
    (_('Interactivity'), {
        'models': (
            'django.contrib.comments.*',
            'form_designer.*',
            'fluent_comments.*',
            'fluentcms_contactform.*',
            'threadedcomments.*',
        ),
        'module': 'fluent_dashboard.modules.AppIconList',
        'collapsible': False,
    }),
    (_('Administration'), {
        'models': (
            'django.contrib.auth.*',
            'django.contrib.sites.*',
            '*.UserProfile',
            'registration.*',
            'google_analytics.*',
        ),
        'module': 'fluent_dashboard.modules.AppIconList',
        'collapsible': False,
    }),
    (_('Applications'), {
        'models': ('*',),
        'module': FLUENT_DASHBOARD_DEFAULT_MODULE,
        'collapsible': False,
    }),
)

FLUENT_PAGES_TEMPLATE_DIR = os.path.join(SRC_DIR, 'frontend', 'templates')

FLUENT_MARKUP_LANGUAGES = ('restructuredtext', 'markdown')

FLUENT_TEXT_CLEAN_HTML = True
FLUENT_TEXT_SANITIZE_HTML = True
FLUENT_TEXT_PRE_FILTERS = (
    'fluent_contents.plugins.text.filters.smartypants.smartypants_filter',
)

FLUENTCMS_CONTACTFORM_STYLES = (
    ('default', {
        'title': _("Default"),
        'form_class': 'fluentcms_contactform.forms.default.DefaultContactForm',
        'required_apps': (),
    }),
    ('captcha', {
        'title': _("Default with captcha"),
        'form_class': 'fluentcms_contactform.forms.captcha.CaptchaContactForm',
        'required_apps': ('captcha',),
    }),
    ('compact', {
        'title': _("Compact"),
        'form_class': 'fluentcms_contactform.forms.compact.CompactContactForm',
    }),
)

FLUENTCMS_EMAILTEMPLATES_PLUGINS = (
    'EmailTextPlugin',
    'PicturePlugin',
)

MAPSEARCH_JS = "fluentcms_googlemaps/js/mapsearch.js"
FLUENTCMS_GOOGLEMAPS_STYLES = (
    ('default', {
        'title': _("Default"),
        'template': "fluentcms_googlemaps/maps/default.html",
    }),
    ('compact', {
        'title': _("Compact (for sidebar)"),
        'template': "fluentcms_googlemaps/maps/compact.html",
    }),
    ('search', {
        'title': _("Search field"),
        'template': "fluentcms_googlemaps/maps/search.html",
        'extra_js': (
            MAPSEARCH_JS,
        ),
    }),
)

GEOPOSITION_GOOGLE_MAPS_API_KEY = env.str('GEOPOSITION_GOOGLE_MAPS_API_KEY', default='AIzaSyAaJBQv8r2Qiio_fPQfhxc4-AFQIIwHjl4')

GOOGLE_ANALYTICS_PROPERTY_ID = env.str('GOOGLE_ANALYTICS_PROPERTY_ID', default='')

HEALTH_CHECKS = {
    'database': 'django_healthchecks.contrib.check_database',
    'cache': 'django_healthchecks.contrib.check_cache_default',
    'ip': 'django_healthchecks.contrib.check_remote_addr',
    'git_version': 'fluentdemo.lib.healthchecks.git_version',
}
HEALTH_CHECKS_ERROR_CODE = 503

PARLER_DEFAULT_LANGUAGE_CODE = 'en'
PARLER_ENABLE_CACHING = True
PARLER_LANGUAGES = {
    1: [
        {'code': 'en'},
        {'code': 'nl'},
    ],
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}

PHONENUMBER_DEFAULT_REGION = 'NL'
PHONENUMBER_DEFAULT_FORMAT = 'NATIONAL'

TAGGIT_TAGS_FROM_STRING = 'taggit_selectize.utils.parse_tags'
TAGGIT_STRING_FROM_TAGS = 'taggit_selectize.utils.join_tags'

THUMBNAIL_DEBUG = False
THUMBNAIL_FORMAT = 'JPEG'
THUMBNAIL_ALTERNATIVE_RESOLUTIONS = [2]  # Generate 2x images for everything!

if 'THUMBNAIL_REDIS_URL' in env.ENVIRON:
    # Allow thumbnails to exist in redis cache
    redis_cache = env.cache('THUMBNAIL_REDIS_URL')  # e.g. 'rediscache://localhost:6379:1'

    THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
    THUMBNAIL_REDIS_HOST = redis_cache['LOCATION'].split(':')[0]
    THUMBNAIL_REDIS_DB = redis_cache['LOCATION'].split(':')[2]
