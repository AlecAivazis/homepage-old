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
    The index template
    """
    template_name = 'splash.jade'


class Projects(TemplateView):
    """
    The Projects view
    """
    template_name = 'core/projects.jade'

    def get_context_data(self, **kwargs):
        """ add the necessary context variables for the project view """
        # get the parent context
        context = super().get_context_data()
        # add the projects to the context
        context['projects'] = Project.objects.all()
        # return the augmented context
        return context


class About(TemplateView):
    """
    The about me page
    """
    template_name = 'core/about.jade'


# end of file
