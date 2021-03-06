import os

from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR_LOG = config('BASE_DIR_LOG', default=BASE_DIR + '/log/app_logs_')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

COVID19_APPS = ['api', 'frontend']

INSTALLED_APPS += COVID19_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'covidapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'covidapi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CELERYD_PREFETCH_MULTIPLIER = 1
SCHEDULED_TASK_TIME = config('SCHEDULED_TASK_TIME', 3600)
TASK_LOCK_EXPIRE = config('TASK_LOCK_EXPIRE', 3600)
CELERY_BROKER_URL = config(
    'BROKER_URL', default='amqp://guest:guest@localhost//')

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     # How to format the output
#     'formatters': {
#         'standard': {
#             'format':
#             "[%(asctime)s] %(threadName)s, %(name)s, %(levelname)s [%(filename)s:%(lineno)d]:  %(message)s",
#             'datefmt':
#             "%d/%m/%Y %H:%M:%S"
#         },
#         'djangolog': {
#             'format':
#             '[%(asctime)s] - %(name)s, [%(filename)s:%(lineno)d]: %(message)s',
#             'datefmt':
#             '%d/%m/%Y %H:%M:%S'
#         },
#     },
#     # Log handlers (where to go)
#     'handlers': {
#         'log_file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': BASE_DIR_LOG + 'django_app.log',
#             'maxBytes': (1024 * 1024) * 2,
#             'backupCount': 10,
#             'formatter': 'djangolog',
#         },
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#         'api_tasks': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': BASE_DIR_LOG + 'api_tasks.log',
#             'maxBytes': (1024 * 1024) * 2,
#             'backupCount': 10,
#             'formatter': 'standard'
#         },
#     },
#     # Loggers (where does the log come from)
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'log_file'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'api_tasks': {
#             'handlers': ['console', 'api_tasks'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#     }
# }
