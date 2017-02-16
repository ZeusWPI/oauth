import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'UNSAFE_DEFAULT'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
FORCE_SCRIPT_NAME = '/'
LOGIN_URL = '/accounts/login/'

DEBUG = False

KRB5_REALM = ''
KRB5_SERVICE = ''
