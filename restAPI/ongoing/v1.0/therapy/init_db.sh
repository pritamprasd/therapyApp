#!/bin/sh
echo "------ Create database tables ------"
python manage.py migrate --noinput

echo "------ create default admin user ------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser(self,'admin', 'admin@myapp.local', 'Passw0rd')" | python manage.py shell

echo "------ starting gunicorn &nbsp;------"
gunicorn myapp.wsgi --workers 2