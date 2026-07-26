#!/usr/bin/env bash
set -o errexit

pip install -r requriment.txt

python manage.py collectstatic --noinput
python manage.py migrate --noinput
