# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the for api

# django imports
from django.shortcuts import render_to_response

# index view
def home(request):
    # return the rendered template
    return render_to_response('index.jade')


# end of file
