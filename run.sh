#!/bin/sh
/code/scripts/wait-for-it.sh database:5432
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000 --settings=scrappy.settings
