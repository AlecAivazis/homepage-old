# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the for blog

# django imports
from django.views.generic import TemplateView

class Home(TemplateView):
    """
    render the index template
    """
    template_name = 'blog/index.jade'

# end of file
