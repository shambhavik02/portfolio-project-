#!/bin/bash

# Install dependencies if not handled by Vercel automatically (optional)
# pip install -r requirements.txt

# Create migrations (if local ones are missing)
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput --clear
