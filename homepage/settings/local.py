# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file contains the settings necessary for local deployment of homepage

from .homepage import *

# enable debugging support
DEBUG = True
TEMPLATE_DEBUG = True
COMPRESS_DEBUG_TOGGLE = True

# change the django compressor settings to point to a more friendly place
COMPRESS_ROOT = RESOURCES

# add django_toolbar to the installed apps
INSTALLED_APPS += ("debug_toolbar", )

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE, 'db', 'homepage.sqlite3'),
    }
}

# end of file
