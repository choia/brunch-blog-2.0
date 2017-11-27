from .base import *
import dj_database_url


SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['brunch-blog.herokuapp.com',]

INSTALLED_APPS += ['storages',]

DATABASES= {}
DATABASES['default'] = dj_database_url.config(default=os.environ['DATABASE_URL'])


#AWS S3 Settings
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID 		= os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY   = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_S3_CUSTOM_DOMAIN 	= '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION	= 'static'
STATICFILES_STORAGE 	= 'blog_settings.s3.aws_storages.StaticStorage'

 
MEDIAFILES_LOCATION		= 'media'
DEFAULT_FILE_STORAGE	= 'blog_settings.s3.aws_storages.MediaStorage'