import os
import sys

# Add the app directory to the PYTHONPATH
sys.path.append('/home/dhruv/Documents/PyCharmProjects/amplio')

# Load settings from amplio_app
os.environ['DJANGO_SETTINGS_MODULE'] = 'amplio_app.settings'

# Activate your virtual environment
activate_env = "/home/dhruv/Environments/python3.5env/bin/activate_this.py"
exec(compile(open(activate_env).read(), activate_env, 'exec'), dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

# Launch the application over WSGI
application = get_wsgi_application()