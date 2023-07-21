#!/usr/bin/env bash
# exit on error

set -o errexit
/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip
/opt/render/project/src/.venv/bin/python -m pip install -r requirements.txt

# poetry install
# poetry lock
/opt/render/project/src/.venv/bin/python manage.py collectstatic --no-input
/opt/render/project/src/.venv/bin/python manage.py migrate

# poetry add gunicorn
