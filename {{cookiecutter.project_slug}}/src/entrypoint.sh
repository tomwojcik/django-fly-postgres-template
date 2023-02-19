#!/usr/bin/env bash

set -o errexit

# why collectstatic here? see https://community.fly.io/t/django-collectstatic-from-deploy-release-command-success-but-staticfile-folder-not-found/6949  # noqa

python manage.py collectstatic  --noinput
python manage.py migrate  --noinput

gunicorn config.wsgi:application --workers 2 --bind 0.0.0.0:8000 --reload --access-logfile '-' --log-level 'info' --capture-output --enable-stdio-inheritance
