# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file defines the url paths for blog

# python imports
from django.conf.urls import url, patterns
from django.views.generic import TemplateView

# import the views from the base application
from .views import *

# base urls
urlpatterns = patterns('',
    url(r'^$', Latest.as_view()),
    url(r'category/(?P<tag>[\w-]+)', CategoryList.as_view(), name="category_list"),
    url(r'(?P<slug>[\w-]+)', PostDetail.as_view(), name="post_detail"),
)

# end of file
