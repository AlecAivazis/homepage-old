# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the base views for homepage

# homepage imports
from .models import Project

# django imports
from django.views.generic import TemplateView


class Home(TemplateView):
    """
    render the index template
    """
    template_name = 'core/about.jade'


class Portfolio(TemplateView):
    """
    render the portfolio
    """
    template_name = 'core/portfolio.jade'
    # add the various projects to the view
    projects = Project.objects.all()


class About(TemplateView):
    """
    render the about me page
    """
    template_name = 'core/about.jade'
    

# end of file
