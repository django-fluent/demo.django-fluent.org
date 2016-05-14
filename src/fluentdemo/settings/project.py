"""
Project specific settings
"""
from .defaults import *
from django.utils.translation import ugettext_lazy as _

# -------------------------------------
# TODO: update the email settings here!
# -------------------------------------

# Admins receive 500 errors, managers receive 404 errors.
ADMINS = (
    ('fluentdemo', 'sysadmin@fluentdemo.example.org'),
)
MANAGERS = ADMINS

SERVER_EMAIL = 'root@localhost'
DEFAULT_FROM_EMAIL = 'info@fluentdemo.example.com'
EMAIL_SUBJECT_PREFIX = '[Django][fluentdemo] '

# Project language settings
TIME_ZONE = 'Europe/Amsterdam'
LANGUAGE_CODE = 'en'

# These are all languages that content can be written in.
LANGUAGES = (
    ('en', _('English')),  # Primary language first
    ('nl', _('Dutch')),
)

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

SITE_ID = 1

# Database to use
DATABASES = {
    'default': {
        # Choose between PostgreSQL or MySQL:
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        #'ENGINE':   'django.db.backends.mysql',
        'NAME':     'fluentdemo',
        'USER':     'fluentdemo',
        'PASSWORD': 'testtest',
    },
}

SECRET_KEY = 'c3#r=h50=zuea%=0-9mx@gf2l0*m^yhmy_hi_0-oc98+1by2so'

# Apps to use
INSTALLED_APPS += (
    # Site parts
    'frontend',
    'apps.blog',
    'apps.wysiwyg_config',

    # CMS parts
    'fluent_blogs',
    'fluent_blogs.pagetypes.blogpage',
    'fluent_pages',
    'fluent_pages.pagetypes.fluentpage',
    'fluent_pages.pagetypes.redirectnode',
    'fluent_comments',
    'fluent_contents',

    # CMS plugins
    'fluent_contents.plugins.text',
    'fluent_contents.plugins.oembeditem',
    'fluent_contents.plugins.picture',
    'fluent_contents.plugins.sharedcontent',
    'fluent_contents.plugins.rawhtml',
    'fluentcms_contactform',
    'fluentcms_cookielaw',
    'fluentcms_countdown',
    'fluentcms_file',
    'fluentcms_forms_builder',
    'fluentcms_googlemaps',
    'fluentcms_jumbotron',
    #'fluentcms_link',
    'fluentcms_pager',
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
    'taggit_autosuggest',
    'tinymce',

    # and enable the admin
    'fluent_dashboard',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'flat',
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'raven.contrib.django.middleware.SentryLogMiddleware',       # make 'request' available on all logs.
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',  # on 404, report to sentry.
) + MIDDLEWARE_CLASSES + (
    'axes.middleware.FailedLoginMiddleware',
    'fluent_contents.middleware.HttpRedirectRequestMiddleware',
)

TEMPLATES[0]['OPTIONS']['context_processors'] += (
    'frontend.context_processors.frontend',
)

TEMPLATES[0]['OPTIONS']['loaders'] += (
    'admin_tools.template_loaders.Loader',  # Allow {% extends "appname:template" %}
)

FORMAT_MODULE_PATH = 'fluentdemo.settings.locale'  # Consistent date formatting

# Avoid 600 permission for filebrowser uploads.
FILE_UPLOAD_PERMISSIONS = 0o644

IGNORABLE_404_URLS = (
    #re.compile(r'^/favicon.ico$'),
    #re.compile(r'^/wp-login.php$'),
)


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


## -- Third party app settings

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

DJANGO_WYSIWYG_FLAVOR = 'tinymce_advanced'

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

FLUENT_CONTENTS_CACHE_OUTPUT = True

text_plugins = ('TextPlugin', 'PicturePlugin', 'OEmbedPlugin', 'RawHtmlPlugin',)
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
        ),
    },
    'blog_content': {
        'plugins': text_plugins + (
            # Allow a lot of content in the main area.
            'SharedContentPlugin',
            'FilePlugin',
            # 'LinkPlugin',
            'MapPlugin',
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
            'apps.blog.*',
            'apps.news.*',
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
    (_('Impact Platform'), {
        'models': (
            'apps.impactmap.*',
            'apps.oscar_extra.giveone.*',
        ),
        'module': 'fluent_dashboard.modules.AppIconList',
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

PING_CHECKS = (
    'ping.checks.check_database_sessions',
    'ping.checks.check_database_sites',
    #'ping.checks.check_celery', # Fails..
)

PHONENUMBER_DEFAULT_REGION = 'NL'
PHONENUMBER_DEFAULT_FORMAT = 'NATIONAL'

THUMBNAIL_DEBUG = False
THUMBNAIL_FORMAT = 'JPEG'
THUMBNAIL_ALTERNATIVE_RESOLUTIONS = [2]  # Generate 2x images for everything!
#THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
#THUMBNAIL_REDIS_HOST = 'localhost'
#THUMBNAIL_REDIS_DB = 1
