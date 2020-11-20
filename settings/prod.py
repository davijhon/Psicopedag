from .base import *
import psycopg2
import dj_database_url
from decouple import config


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 'psicopedagogia-integral.herokuapp.com'
ALLOWED_HOSTS = ['psicopedagogia-integral.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_URL = config('DATABASE_URL')

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

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)