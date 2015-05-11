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
    url(r'^about/$', About.as_view(), name="about"),
    url(r'^projects/$', Projects.as_view(), name="projects"),
    url(r'^projects/(?P<name>[\w-]+)$', ProjectDetail.as_view(), name="project_detail"),
    url(r'^$', Home.as_view()),
)

# end of file
