#!/bin/bash

sleep 5

# Collect static files
echo "Collect static files"
python code/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python code/manage.py makemigrations --merge --noinput
python code/manage.py makemigrations
python code/manage.py migrate
python code/manage.py migrate --run-syncdb

#Create admin user
echo "Creating admin user"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin4242')" | python code/manage.py shell

# Start server
echo "Starting server"
python code/manage.py runserver 0.0.0.0:8080