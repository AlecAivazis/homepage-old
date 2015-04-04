# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the for blog

# django imports
from django.views.generic import TemplateView

# homepage imports
from .models import Post

class Latest(TemplateView):
    """
    render the index template
    """
    template_name = 'blog/list.jade'

    def get_context_data(self, **kwargs):
        """
        Add the necessary data for the template
        """
        # grab the parent context
        context = super().get_context_data(**kwargs)
        # add the latests posts 
        context['posts'] = Post.objects.latest_first()
        # add the title of the page
        context['title'] = 'Latests Posts'
        # return the new context
        return context


# end of file
