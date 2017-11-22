from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['brunch-blog.herokuapp.com',]

INSTALLED_APPS += ['storages', ]


#AWS S3 Settings
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID 		= os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY   = os.environ['AWS_SECRET_ACCESS_KEY']
STATICFILES_STORAGE 	= 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_CUSTOM_DOMAIN 	= '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
