# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file contains the settings necessary for local deployment of homepage

from .homepage import *

# enable debugging support
DEBUG = False
TEMPLATE_DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'homepage',
        'USER': 'homepage',
        'PASSWORD': 'darksteel',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# end of file
