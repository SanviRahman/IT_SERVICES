#!/bin/sh
echo "BUILD START"

# Use a compatible Python version (adjust if necessary)
python3 -m pip install -r requirements.txt

# Run Django static files collection
python3 manage.py collectstatic --noinput --clear

# Ensure Vercel finds the output directory
mkdir -p staticfiles_build
cp -r staticfiles/* staticfiles_build/

echo "BUILD END"
