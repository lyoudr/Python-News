#!/bin/bash
# print env SERVER_PORT
echo $SERVER_PORT

# make migrations first
python manage.py makemigrations

# Apply database migrations to database in container
echo "Apply database migrations"
python manage.py migrate

# Load Initial database data
python manage.py loaddata dump_data

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:$SERVER_PORT