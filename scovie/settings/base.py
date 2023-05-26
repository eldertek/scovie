"""
    Django Project settings
"""
import logging
import os as __os
from pathlib import Path as __Path


ENV_TYPE = __os.environ.get('ENV_TYPE', None)
print(f'ENV_TYPE:{ENV_TYPE!r}')


###############################################################################

# Build paths relative to the project root:
PROJECT_PATH = __Path(__file__).resolve().parent.parent.parent
print(f'PROJECT_PATH:{PROJECT_PATH}')

# Build paths relative to the current working directory:
BASE_PATH = __Path().cwd().resolve()
print(f'BASE_PATH:{BASE_PATH}')

# Paths with Django dev. server:
# BASE_PATH...: .../django-for-runners
# PROJECT_PATH: .../django-for-runners

# But the paths are different, if it's installed as python package!

###############################################################################

LOGIN_URL = 'admin:login'

###############################################################################


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False


# SECURITY WARNING: keep the secret key used in production secret!
__SECRET_FILE = __Path(BASE_PATH, 'secret.txt').resolve()
if not __SECRET_FILE.is_file():
    print(f'Generate {__SECRET_FILE}')
    from secrets import token_urlsafe as __token_urlsafe

    __SECRET_FILE.write_text(__token_urlsafe(128))

SECRET_KEY = __SECRET_FILE.read_text().strip()


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'scovie.apps.ScovieAppConfig',
    'screen.apps.ScreenAppConfig',
    'solo',
]

ROOT_URLCONF = 'scovie.urls'
WSGI_APPLICATION = 'scovie.wsgi.application'


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.middleware.locale.LocaleMiddleware',
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

USE_TZ = True

# _____________________________________________________________________________

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# _____________________________________________________________________________

# Mark CSRF cookie as "secure" -> browsers sent cookie only with an HTTPS connection:
CSRF_COOKIE_SECURE = True

# Mark session cookie as "secure" -> browsers sent cookie only with an HTTPS connection:
SESSION_COOKIE_SECURE = True

# HTTP header/value combination that signifies a request is secure
# Your nginx.conf must set "X-Forwarded-Protocol" proxy header!
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

# SecurityMiddleware should redirects all non-HTTPS requests to HTTPS:
SECURE_SSL_REDIRECT = True

# SecurityMiddleware should preload directive to the HTTP Strict Transport Security header:
SECURE_HSTS_PRELOAD = True

# Instruct modern browsers to refuse to connect to your domain name via an insecure connection:
SECURE_HSTS_SECONDS = 3600

# SecurityMiddleware should add the "includeSubDomains" directive to the Strict-Transport-Security
# header: All subdomains of your domain should be served exclusively via SSL!
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# _____________________________________________________________________________
# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = str(__Path(BASE_PATH, 'static'))

MEDIA_URL = '/media/'
MEDIA_ROOT = str(__Path(BASE_PATH, 'media'))

# _____________________________________________________________________________
# cut 'pathname' in log output

old_factory = logging.getLogRecordFactory()


def cut_path(pathname, max_length):
    if len(pathname) <= max_length:
        return pathname
    return f'...{pathname[-(max_length - 3):]}'


def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.cut_path = cut_path(record.pathname, 30)
    return record


logging.setLogRecordFactory(record_factory)

# -----------------------------------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)8s %(cut_path)s:%(lineno)-3s %(message)s',
        }
    },
    'handlers': {'console': {'class': 'logging.StreamHandler', 'formatter': 'verbose'}},
    'loggers': {
        'django': {'handlers': ['console'], 'level': 'INFO', 'propagate': False},
        'scovie': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': False},
    },
}

# -----------------------------------------------------------------------------
# Internationalization
from django.contrib.admin.sites import AdminSite
from django.utils.translation import gettext_lazy as _


AdminSite.site_title = _("Scovie")
AdminSite.site_header = _("Scovie - Information management software")
AdminSite.index_title = _("Administration of Scovie")

LANGUAGES = [
    ('en', 'English'),
    ('fr', 'Français'),
]

LANGUAGE_CODE = "en"

LOCALE_PATHS = [BASE_PATH / 'locale']

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
