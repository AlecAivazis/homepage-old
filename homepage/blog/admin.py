# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the administration for blog

# import the django admin
from django.contrib import admin

from .models import Post

# register the base models
admin.site.register(Post)


# end of file
