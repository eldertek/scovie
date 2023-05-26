#!/bin/sh

export DJANGO_SETTINGS_MODULE=scovie.settings.local

exec poetry run python3 manage.py "$@"
