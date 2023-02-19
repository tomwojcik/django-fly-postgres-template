#!/usr/bin/env bash

set -o errexit

#while ! echo 'SELECT 1' | PGPASSWORD=$POSTGRES_PASSWORD psql --host $POSTGRES_HOST --user $POSTGRES_USER $POSTGRES_DB; do echo "Waiting for DB"; sleep 5; done

echo "Runserver starting"
python -Wd manage.py runserver_plus 0.0.0.0:8000
