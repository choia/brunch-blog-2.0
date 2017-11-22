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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = 'blog/static/'
STATIC_ROOT = 'blog/staticfiles'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'blog/static'),
   ]

#INSTALLED_APPS += ['debug_toolbar', ]