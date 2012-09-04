# Django settings for dashboard project.
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
import django_cache_url
import dj_database_url


DIRNAME = os.path.abspath(os.path.dirname(__file__))

DEBUG = bool(os.environ.get('DEBUG', False))

ADMINS = (('Admin', 'bugs@incuna.com'),)
MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config(default='postgres://localhost/dashboard')}
CACHES = {'default': django_cache_url.config()}

TIME_ZONE = 'UTC'
USE_L10N = True # Locale
USE_TZ = True

LANGUAGE_CODE = 'en-GB'
USE_I18N = False # Internationalization

# S3 Backend
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Static
MEDIA_ROOT = os.path.join(DIRNAME, 'client_media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(DIRNAME, 'static_media')
STATIC_URL = '/static/' if DEBUG else 'http://{0}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
INCUNA_MEDIA_URL = STATIC_URL + 'incuna/'
STATICFILES_DIRS = (('', os.path.join(DIRNAME, 'static')),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

TEMPLATE_DEBUG = DEBUG
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
AUTH_PROFILE_MODULE = 'profiles.Profile'
SOCIAL_AUTH_USER_MODEL = 'profiles.Profile'

ROOT_URLCONF = 'dashboard.urls'
SITE_ID = 1
SECRET_KEY = '_o273km705m5xdai56i5g%bd3jiaj60h$f87q+#e2phuyvi2c4'
WSGI_APPLICATION = 'dashboard.wsgi.application'

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
    'raven.contrib.django',
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
    'status.modules.shoppinglist',
    'status.modules.weather',
)

SENTRY_DSN = 'http://e14704ffb3bd45a49c2411066163acd2:daf162a3a494436e9acc82ba8788e8c6@sentry.incuna.com/14'
SENTRY_TESTING = DEBUG
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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

# Debug Toolbar
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
INTERNAL_IPS = ('127.0.0.1',)

# Holiday
HOLIDAY_DEFAULT_ANNUAL_DAYS = 20

# imc
IMC_DEFAULT_PERIOD = 14

# South
SOUTH_MIGRATION_MODULES = {
    'profiles': 'dashboard.project_migrations.profiles',
}

# Weather
BBC_HOURLY_WEATHER = 'http://newsrss.bbc.co.uk/weather/forecast/25/ObservationsRSS.xml'
BBC_WEEKLY_WEATHER = 'http://newsrss.bbc.co.uk/weather/forecast/25/Next3DaysRSS.xml'

