# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file contains the settings that are specific to the application as a whole

from .base import *

# Application definition

django_apps = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

third_party_apps = (
    'compressor',
 )

homepage_apps = (
    'homepage.api',
    'homepage.core',
    'homepage.blog',
)

INSTALLED_APPS = homepage_apps + third_party_apps + django_apps

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'homepage.urls'

APPEND_SLASH = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = RESOURCES
MEDIA_ROOT = UPLOADS

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Template definitions

TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader',(
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.filesystem.Loader',
    )),
)

TEMPLATE_DIRS = (
    TEMPLATES,
)

# django compressor settings

COMPRESS_ROOT = RESOURCES
COMPRESS_OUTPUT_DIR = "cache"

stylus_conf = ('-u jeet -u axis -u rupture -I ' +
               os.path.join(RESOURCES,'styles') +' < {infile} > {outfile}')

COMPRESS_PRECOMPILERS = (
    ('text/stylus', 'stylus '+ stylus_conf),
    ('text/coffeescript', 'coffee --compile --stdio -b'),
)

# end of file
