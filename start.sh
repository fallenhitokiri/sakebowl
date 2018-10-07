#!/bin/sh
python3 ./manage.py migrate
python3 ./manage.py qcluster &
gunicorn -w 3 sakebowl.wsgi
