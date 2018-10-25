#!/bin/sh
python3 ./manage.py migrate
python3 ./manage.py collectstatic
python3 ./manage.py qcluster &
gunicorn -b 0.0.0.0:8000 -w 3 sakebowl.wsgi
