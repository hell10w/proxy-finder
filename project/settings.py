"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
relative_path = lambda *args: os.path.join(BASE_DIR, *args)


SITE_ID = 1


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%shvv0!dce3ow#kw9(y&400cs+s+q=_hoban#^eg9p_5+kh*ha'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ['127.0.0.1', ]
ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'grappelli',
    'django.contrib.admin',

    'south',
    'debug_toolbar',
    'rest_framework',
    'rosetta',
    'crispy_forms',
    'pipeline',
    'bootstrap3',

    'layout',
    'proxyfinder',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'layout.middleware.LayoutMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'proxy_finder',
        'USER': 'root',
        'PASSWORD': '654321',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Novosibirsk'

USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (
    #os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'proxyfinder', 'locale'),
)

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
)

ROSETTA_WSGI_AUTO_RELOAD = True
ROSETTA_MESSAGES_PER_PAGE = 100

#
TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'layout.context_processors.layout',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = relative_path('static')
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_ENABLED = not DEBUG
PIPELINE_CSS = {
    'vendor': {
        'source_filenames': (
            'css/bootstrap.css',
        ),
        'output_filename': 'css/vendor.css',
    },
    'own': {
        'source_filenames': (
            'css/main.css',
        ),
        'output_filename': 'css/own.css',
    },
}

PIPELINE_JS = {
    'header': {
        'source_filenames': (
            'js/vendor/jquery-1.10.1.min.js',
            'js/vendor/modernizr-2.6.2-respond-1.1.0.min.js',
        ),
        'output_filename': 'js/header.js',
    },
    'footer': {
        'source_filenames': (
            'js/vendor/bootstrap.js',
            'js/main.js',
        ),
        'output_filename': 'js/footer.js',
    }
}

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    ),

    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


LOGGING = {
    'version': 1,
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'grab': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
