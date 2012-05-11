# Django settings for dashboard project.

import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


DIRNAME = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG', False)

ADMINS = (
    ('Admin', 'bugs@incuna.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dashboard',
        'USER': 'dashboard',
        'PASSWORD': 'X#u_7F54+a6gh,tQ',
        'HOST': '127.0.0.1',
        'PORT': '',
    },
    # 'redmine': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'redmine',
    #     'USER': 'redmine',
    #     'PASSWORD': 'moo',
    #     'HOST': 'redmine.incuna.com',
    #     'HOST': 'dev.incuna.com',
    #     'PORT': '',
    # }
}

DATABASE_ROUTERS = ['status.modules.redmine.routers.RedmineRouter']

TIME_ZONE = 'Europe/London'
USE_TZ = True

LANGUAGE_CODE = 'en-GB'
USE_I18N = False # Internationalization
USE_L10N = True # Locale

MEDIA_ROOT = os.path.join(DIRNAME, 'client_media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(DIRNAME, 'static_media')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
INCUNA_MEDIA_URL = STATIC_URL + 'incuna/'
STATICFILES_DIRS = (
    ('', os.path.join(DIRNAME, 'static')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

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
)

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

    'django_extensions',
    'gunicorn',
    'profiles',
    'south',
    'uni_form',
    'incuna',

    'dashboard',
    'contacts',
    'holiday',
    # 'imc',
    # 'password',

    'status',
    'status.modules.redmine',
    'status.modules.shoppinglist',
    'status.modules.weather',
)

SOUTH_MIGRATION_MODULES = {
    'profiles': 'project_migrations.profiles',
}

BBC_HOURLY_WEATHER = 'http://newsrss.bbc.co.uk/weather/forecast/25/ObservationsRSS.xml'

BBC_WEEKLY_WEATHER = 'http://newsrss.bbc.co.uk/weather/forecast/25/Next3DaysRSS.xml'

#HOLIDAYCAL_URL = 'http://holiday.incuna.com'

HOLIDAY_DEFAULT_ANNUAL_DAYS = 20

IMC_DEFAULT_PERIOD = 14

AUTH_PROFILE_MODULE = 'profiles.Profile'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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
