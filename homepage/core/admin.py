# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the base administration for homepage

# homepage imports
from .models import Project

# import the django admin
from django.contrib import admin

# register the base models
admin.site.register(Project)

# end of file
