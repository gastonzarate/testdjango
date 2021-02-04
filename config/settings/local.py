
from .base import * # NOQA
from .base import TEMPLATES, env, INSTALLED_APPS

# Base
DEBUG = True

# Security
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1'
]

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Apps
INSTALLED_APPS += [
    'django_extensions',
]

# Database
DATABASES = {
    'default': env.db('DATABASE_URL')
}
