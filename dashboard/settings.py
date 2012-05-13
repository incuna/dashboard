# Django settings for dashboard project.

import os

import dj_database_url
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


DIRNAME = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG', False)

ADMINS = (
    ('Admin', 'bugs@incuna.com'),
)

MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config()}

TIME_ZONE = 'Europe/London'
USE_TZ = True

LANGUAGE_CODE = 'en-GB'
USE_I18N = False # Internationalization
USE_L10N = True # Locale

# S3 Backend
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Static
MEDIA_ROOT = os.path.join(DIRNAME, 'client_media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(DIRNAME, 'static_media')
STATIC_URL = 'http://{0}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
INCUNA_MEDIA_URL = STATIC_URL + 'incuna/'
STATICFILES_DIRS = (('', os.path.join(DIRNAME, 'static')),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

TEMPLATE_DIRS = (os.path.join(DIRNAME, 'templates'),)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.request',)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'incuna.auth.middleware.LoginRequiredMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)
GOOGLE_OAUTH2_CLIENT_ID = '906873610360.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'g1zuOBlx25xB3FsYyJLTxDEe'
GOOGLE_WHITE_LISTED_DOMAINS = ['incuna.com']

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'
LOGIN_EXEMPT_URLS = ['^complete/*', '^login/*', '^login-error/']

SOCIAL_AUTH_USER_MODEL = 'profiles.Profile'

ROOT_URLCONF = 'dashboard.urls'
SITE_ID = 1
SECRET_KEY = '_o273km705m5xdai56i5g%bd3jiaj60h$f87q+#e2phuyvi2c4'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'social_auth',

    'django_extensions',
    'gravatar',
    'gunicorn',
    'profiles',
    'south',
    'storages',
    'uni_form',
    'incuna',

    'dashboard',
    'contacts',
    'holiday',
    # 'imc',
    'password',

    'status',
    'status.modules.redmine',
    'status.modules.shoppinglist',
    'status.modules.weather',
)

SOUTH_MIGRATION_MODULES = {
    'profiles': 'dashboard.project_migrations.profiles',
}

BBC_HOURLY_WEATHER = 'http://newsrss.bbc.co.uk/weather/forecast/25/ObservationsRSS.xml'

BBC_WEEKLY_WEATHER = 'http://newsrss.bbc.co.uk/weather/forecast/25/Next3DaysRSS.xml'

#HOLIDAYCAL_URL = 'http://holiday.incuna.com'

HOLIDAY_DEFAULT_ANNUAL_DAYS = 20

IMC_DEFAULT_PERIOD = 14

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError, e:
    pass
