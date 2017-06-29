import os
import sys

path = '/home/uma/Mark'
if path not in sys.path:
        sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Mark.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
