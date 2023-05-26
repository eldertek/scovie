from scovie.settings.prod import *  # noqa:F401,F403


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'scovie',
        'DEBUG_NAME': 'scovie',
    },
}
