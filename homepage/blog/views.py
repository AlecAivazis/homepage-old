# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the for blog

# django imports
from django.views.generic import ListView, DetailView

# homepage imports
from .models import Post

class Latest(ListView):
    """
    Handle the latest posts
    """
    template_name = 'blog/list.jade'

    def get_context_data(self, **kwargs):
        """
        Add the necessary data for the template
        """
        # grab the parent context
        context = super().get_context_data(**kwargs)
        # add the title of the page
        context['title'] = 'Latests Posts'
        # return the new context
        return context


    def get_queryset(self):
        """ Return the latest posts """
        return Post.objects.latest_first()


class CategoryList(ListView):
    """
    Handle the latest posts
    """
    template_name = 'blog/list.jade'

    def get_context_data(self, **kwargs):
        """
        Add the necessary data for the template
        """
        # grab the parent context
        context = super().get_context_data(**kwargs)
        # add the title of the page
        context['title'] = 'Posts matching "{}"'.format(self.kwargs['tag']) 
        # return the new context
        return context


    def get_queryset(self):
        """ Return the latest posts """
        return Post.objects.with_tag(self.kwargs['tag'])


class PostDetail(DetailView):
    """
    Individual post details
    """
    queryset = Post.objects
    template_name = 'blog/post_detail.jade'


# end of file
