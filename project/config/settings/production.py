from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    os.getenv('PUBLIC_IP', '*'),
    os.getenv('DOMAIN_NAME', '*'),
    os.getenv('WWW_DOMAIN_NAME', '*'),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_APP', 'app_db'),
        'USER': os.getenv('DB_USER', 'admin'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'devpass'),
        'HOST': os.getenv("DB_HOST", "postgresdb"),
        'PORT': os.getenv("DB_PORT", "5432"),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
