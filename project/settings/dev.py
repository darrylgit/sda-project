from .base import *
import os


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ([
    os.environ.get('APP_ALLOWED_HOSTS')
    if 'APP_ALLOWED_HOSTS' in os.environ
    else '127.0.0.1' 
])

INSTALLED_APPS+=[
	#added
	'haystack',
    'widget_tweaks',
    'videokit',
	#apps
    'apps.search',
	'apps.upload',
    'apps.blog',
    'apps.flatpages',
]

DATABASE_DEFAULT = {
    'default': {
        'ENGINE': os.environ.get('APP_BASE_ENGINE'),
        'NAME': os.environ.get('APP_BASE_NAME'),
        'USER': os.environ.get('APP_BASE_USER'),
        'PASSWORD': os.environ.get('APP_BASE_PASSWORD'),
        'HOST': os.environ.get('APP_BASE_HOST'),

        'TEST': {
            'NAME': os.environ.get('APP_BASE_TEST_NAME'),
        },
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}

DATABASES = (
    DATABASE_DEFAULT
    if 'APP_BASE_HOST' in os.environ
    else {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATES[0]['OPTIONS']['context_processors']

TEMPLATE_CONTEXT_PROCESSORS += (
    'apps.search.context_processors.search_form',
    'apps.admin.context_processors.from_settings',
    )

ENVIRONMENT_NAME = 'Development'
ENVIRONMENT_COLOR = 'red'



