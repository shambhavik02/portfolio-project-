#!/bin/bash

# Change into the Django project directory
cd portfolio_project

# Install dependencies if not handled by Vercel automatically (optional)
# python3 -m pip install -r ../requirements.txt

# Create migrations (if local ones are missing)
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Collect static files
python3 manage.py collectstatic --noinput --clear
