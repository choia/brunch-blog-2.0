from .base import *

SECRET_KEY = os.environ['LOCAL_SECRET_KEY']

DEBUG = True

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'brunchblog',
'USER': 'brunchbloguser',
'PASSWORD': 'brunch',
'HOST': 'localhost',
'PORT': '',
	}
}

#INSTALLED_APPS += ['debug_toolbar', ]