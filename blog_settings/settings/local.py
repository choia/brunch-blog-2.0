from .base import *


SECRET_KEY = os.environ['LOCAL_SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]

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


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/blog/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'blog/staticfiles')
STATICFILES_DIRS = [
   os.path.join(PROJECT_ROOT, 'blog/static'),
   ]

MEDIA_URL = '/blog/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'blog/mediafiles')

#INSTALLED_APPS += ['debug_toolbar', ]