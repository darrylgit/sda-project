from .base import *
import os


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS+=[
	#added
    #'debug_toolbar',
	'haystack',
    'widget_tweaks',
    'videokit',
	#apps
    'apps.search',
	'apps.uploads',
    'apps.blog',
    'apps.flatpages',
]

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



