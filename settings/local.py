from .base import *
import psycopg2
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['psicopedagogia-integral.herokuapp.com']
# ALLOWED_HOSTS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_URL = 'postgres://hfvnteqpznirmz:fe3d7c9a9a60122eafe69de454419466669a96d76370b45c3942eacdc95d7482@ec2-35-168-77-215.compute-1.amazonaws.com:5432/ddr2o6jlu0o3f8'

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('HOST'),
        'PORT': config('PORT'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

STATICFILES_DIRS = (BASE_DIR, 'static')

