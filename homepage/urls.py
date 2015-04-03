# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the primary url router for homepage

# django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

# import the homepageapplications
from . import core, blog

# define the primary url patterns
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(core.urls)),
    url(r'(?i)blog/', include(blog.urls)),
    url(r'(?i)api/', include(api.urls)),
    # add the static urls
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# end of file
