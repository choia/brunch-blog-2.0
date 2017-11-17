from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['brunch-blog.herokuapp.com',]

INSTALLED_APPS += ['storages', ]