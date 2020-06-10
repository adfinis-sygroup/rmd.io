"""
Django settings for rmd.io

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import datetime
import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="",
    integrations=[DjangoIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "qkk)_bi42*bikzfakx3)vqlr$7o3vn92z*or66c@8z2)$o767d"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django_extensions",
    "mails",
    "widget_tweaks",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "maildelay.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "maildelay.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "maildelay",
        "USER": "rmdio",
        "PASSWORD": "rmdio",
        "HOST": "postgres",
        "PORT": "5432",
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

TIME_ZONE = "Europe/Zurich"

LANGUAGE_CODE = "en-us"

SITE_URL = "http://localhost:8000"

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Login redirects to

LOGIN_REDIRECT_URL = "/mails/"

LOGIN_REDIRECT_URL_FAILURE = "/login/"

LOGOUT_REDIRECT_URL = "/home/"

# Auth

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "mails.auth.EmailBackend",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Media

MEDIA_ROOT = ""

MEDIA_URL = ""

# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "[%(asctime)s] %(levelname)s " "[%(name)s:%(lineno)s] %(message)s"
            ),
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "error.log"),
            "formatter": "verbose",
        },
    },
    "loggers": {"mails": {"handlers": ["console"], "level": "DEBUG",},},
}

# Mailserver login settings

EMAIL_HOST_USER = "maildelay@dev.rmd.io"
DEFAULT_FROM_EMAIL = "maildelay@dev.rmd.io"
# EMAIL_HOST_PASSWORD = "password"
EMAIL_HOST = "mailcatcher"
EMAIL_PORT = 1025
EMAIL_FOLDER = "INBOX"

MAILBOXES = [
    ("1d", "Mail Delay for 1 day"),
    ("2d", "Mail Delay for 2 days"),
    ("3d", "Mail Delay for 3 days"),
    ("4d", "Mail Delay for 4 days"),
    ("5d", "Mail Delay for 5 days"),
    ("6d", "Mail Delay for 6 days"),
    ("7d", "Mail Delay for 7 days"),
    ("8d", "Mail Delay for 8 days"),
    ("9d", "Mail Delay for 9 days"),
    ("10d", "Mail Delay for 10 days"),
    ("11d", "Mail Delay for 11 days"),
    ("1w", "Mail Delay for 1 week"),
    ("2w", "Mail Delay for 2 weeks"),
    ("3w", "Mail Delay for 3 weeks"),
    ("4w", "Mail Delay for 4 weeks"),
    ("5w", "Mail Delay for 5 weeks"),
    ("6w", "Mail Delay for 6 weeks"),
    ("7w", "Mail Delay for 7 weeks"),
    ("8w", "Mail Delay for 8 weeks"),
    ("9w", "Mail Delay for 9 weeks"),
    ("10w", "Mail Delay for 10 weeks"),
    ("11w", "Mail Delay for 11 weeks"),
    ("1m", "Mail Delay for 1 month"),
    ("2m", "Mail Delay for 2 months"),
    ("3m", "Mail Delay for 3 months"),
    ("4m", "Mail Delay for 4 months"),
    ("5m", "Mail Delay for 5 months"),
    ("6m", "Mail Delay for 6 months"),
    ("7m", "Mail Delay for 7 months"),
    ("8m", "Mail Delay for 8 months"),
    ("9m", "Mail Delay for 9 months"),
    ("10m", "Mail Delay for 10 months"),
    ("11m", "Mail Delay for 11 months"),
]

BLOCK_DELAYS = {
    1: datetime.timedelta(minutes=10),
    2: datetime.timedelta(hours=1),
    3: datetime.timedelta(days=1),
    4: datetime.timedelta(days=3),
    5: datetime.timedelta(days=7),
}

EMAIL_SUFFIX_TO_DAY = {
    "d": 1,
    "w": 7,
    "m": 30,
}


CALENDAR_STRIP_PREFIXES = (
    r"^Re:\s*",
    r"^Ant:\s*",
    r"^Fwd:\s*",
    r"^Wg:\s*",
)

DATEPARSER_SETTINGS = {
    "PREFER_DATES_FROM": "future",
    "TIMEZONE": "UTC",
    "DATE_ORDER": "DMY",
    "RETURN_AS_TIMEZONE_AWARE": True,
}
