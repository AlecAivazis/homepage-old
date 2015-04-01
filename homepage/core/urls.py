# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file defines the url paths for the base of the homepageapplication

# python imports
from django.conf.urls import url, patterns
from django.views.generic import TemplateView

# import the views from the base application
from .views import *

# base urls
urlpatterns = patterns('',
    url(r'(?i)^$', Home.as_view()),
    url(r'(?i)^portfolio$', Portfolio.as_view()),
)

# end of file
