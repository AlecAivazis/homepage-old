# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the base views for homepage

# homepage imports
from .models import Project

# django imports
from django.views.generic import TemplateView, ListView, DetailView


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


class ProjectDetail(DetailView):
    # base the urls on the name of the project
    slug_field = 'title'
    slug_url_kwarg = 'name'
    model = Project
    template_name = 'core/project_detail.jade'


class About(TemplateView):
    """
    The about me page
    """
    template_name = 'core/about.jade'


class Robots(TemplateView):
    """ 
    Render the robots.txt file
    """
    template_name = "robots.txt"
    content_type = "text/plain"

# end of file
