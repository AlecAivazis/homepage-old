# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the base views for homepage

# homepage imports
from .models import Project

# django imports
from django.views.generic import TemplateView, ListView


class Home(TemplateView):
    """
    The index template
    """
    template_name = 'splash.jade'


class Projects(ListView):
    """
    The Projects view
    """
    template_name = 'core/projects.jade'
    queryset = Project.objects


class About(TemplateView):
    """
    The about me page
    """
    template_name = 'core/about.jade'


# end of file
