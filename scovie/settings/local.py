import sys as __sys

from scovie.settings.base import *  # noqa:F401,F403


print('Use settings:', __file__)


##################################################################################


MIDDLEWARE = list(MIDDLEWARE) + [  # noqa
    'django_tools.middlewares.local_auto_login.AlwaysLoggedInAsSuperUserMiddleware',
]
ADMIN_URL_PREFIX = '/admin/'  # Restrict auto login for the admin


##################################################################################


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True


# Disable caches:
CACHES = {'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}}


# Required for the debug toolbar to be displayed:
INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', 'localhost')


ALLOWED_HOSTS = INTERNAL_IPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_PATH / 'scovie.sqlite3'),  # noqa:405
        # https://docs.djangoproject.com/en/dev/ref/databases/#database-is-locked-errors
        'timeout': 30,
    }
}
print(f'Use Database: {DATABASES["default"]["NAME"]!r}', file=__sys.stderr)


##################################################################################


# Disable security features, because development server doesn't support HTTPS
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_PROXY_SSL_HEADER = None  # type: ignore[assignment]
SECURE_SSL_REDIRECT = False
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
