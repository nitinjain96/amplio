import os
import sys
import site

# Add the site-packages of the chosen virtual environment to work with
site.addsitedir('/home/dhruv/Environments/python3.5env/lib/python3.5/site-packages')

# Add the app directory to the PYTHONPATH
sys.path.append('/home/dhruv/PycharmProjects/django-apps')
sys.path.append('/home/dhruv/PycharmProjects/django-apps/django_apps')

# Load settings from django_apps
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_apps.settings'

# Activate your virtual environment
activate_env = "/home/dhruv/Environments/python3.5env/bin/activate_this.py"
exec(compile(open(activate_env).read(), activate_env, 'exec'), dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

# Launch the application over WSGI
application = get_wsgi_application()