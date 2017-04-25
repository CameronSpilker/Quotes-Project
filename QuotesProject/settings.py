"""
Django settings for QuotesProject project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import shutil

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8rqc)%=k-^w*ulol!x+1g!f(-u18*w67ut7hxy2#abyeptomua'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus',
    'django.contrib.postgres',
    'homepage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django_mako_plus.RequestInitMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'QuotesProject.urls'

TEMPLATES = [
    {
        'NAME': 'django_mako_plus',
        'BACKEND': 'django_mako_plus.MakoTemplates',
        'OPTIONS': {
            # functions to automatically add variables to the params/context before templates are rendered
            'CONTEXT_PROCESSORS': [
                'django.template.context_processors.static',            # adds "STATIC_URL" from settings.py
                'django.template.context_processors.debug',             # adds debug and sql_queries
                'django.template.context_processors.request',           # adds "request" object
                'django.contrib.auth.context_processors.auth',          # adds "user" and "perms" objects
                'django.contrib.messages.context_processors.messages',  # adds messages from the messages framework
                'django_mako_plus.context_processors.settings',         # adds "settings" dictionary
            ],

            # identifies where the Mako template cache will be stored, relative to each template directory
            'TEMPLATES_CACHE_DIR': '.cached_templates',

            # the default app and page to render in Mako when the url is too short
            'DEFAULT_PAGE': 'index',
            'DEFAULT_APP': 'homepage',

            # the default encoding of template files
            'DEFAULT_TEMPLATE_ENCODING': 'utf-8',

            # imports for every template
            'DEFAULT_TEMPLATE_IMPORTS': [
                # import DMP (required)
                'import django_mako_plus',

                # uncomment this next line to enable alternative syntax blocks within your Mako templates
                # 'from django_mako_plus import django_syntax, jinja2_syntax, alternate_syntax

                # the next two lines are just examples of including common imports in templates
                # 'from datetime import datetime',
                # 'import os, os.path, re, json',
            ],

            # whether to send the custom DMP signals -- set to False for a slight speed-up in router processing
            # determines whether DMP will send its custom signals during the process
            'SIGNALS': False,

            # whether to minify using rjsmin, rcssmin during 1) collection of static files, and 2) on the fly as .jsm and .cssm files are rendered
            # rjsmin and rcssmin are fast enough that doing it on the fly can be done without slowing requests down
            'MINIFY_JS_CSS': True,

            # the name of the SASS binary to run if a .scss file is newer than the resulting .css file
            # happens when the corresponding template.html is accessed the first time after server startup
            # if DEBUG=False, this only happens once per file after server startup, not for every request
            # specify the binary in a list below -- even if just one item (see subprocess.Popen)

            # Python 3.3+:
            #'SCSS_BINARY': [ shutil.which('scss'), '--unix-newlines' ],

            # Python 3.0 to 3.2:
            #'SCSS_BINARY': [ '/path/to/scss', '--unix-newlines' ],

            # Disabled (no sass integration)
            'SCSS_BINARY': None,

            # see the DMP online tutorial for information about this setting
            # it can normally be empty
            'TEMPLATES_DIRS': [
                # '/var/somewhere/templates/',
            ],
        },
    },
    {
        'NAME': 'django',
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

WSGI_APPLICATION = 'QuotesProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'QuotesProject',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': '1234',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # SECURITY WARNING: this next line must be commented out at deployment
    BASE_DIR,
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# A logger for DMP
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG  # SECURITY WARNING: never set this True on a live site
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'dmp_simple': {
            'format': '%(levelname)s::DMP %(message)s'
        },
    },
    'handlers': {
        'dmp_console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'dmp_simple'
        },
    },
    'loggers': {
        'django_mako_plus': {
            'handlers': ['dmp_console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

