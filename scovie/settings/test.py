from scovie.settings.prod import *  # noqa:F401,F403


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'scovie.sqlite3',
        'DEBUG_NAME': 'scovie-debug.sqlite3',
    },
}
