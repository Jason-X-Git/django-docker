from .default import *

DATABASES = {
    # Local Postgres
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sales',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'LOCALHOST',
        'PORT': '5432',
    }

    # Docker Postgres
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'HOST': os.environ.get('DB_HOST'),
    #     'NAME': os.environ.get('DB_NAME'),
    #     'USER': os.environ.get('DB_USER'),
    #     'PASSWORD': os.environ.get('DB_PASS'),
    # }
}
