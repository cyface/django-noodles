"""Simple settings for tests and making migrations"""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
ROOT_URLCONF = 'noodles_tests.urls'
SECRET_KEY = 'nokey'

SITE_ID = 1
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
            ],
        },
    },
]


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'noodles',
    'noodles_tests'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
