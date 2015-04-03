# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the models for blog

# import the django models
from django.db import models


class PostQuerySet(models.QuerySet):
    """
    The query set mangaer for blog posts
    """
    def latest_first(self):
        """
        Return the posts with the latest one first
        """
        return self.order_by('-creation_date')

    def oldest_first(self):
        """
        Return the posts with the oldest one first
        """
        return self.latest_first().reverse()


class Post(models.Model):
    """
    The base class for entries in the blog
    """
    title = models.CharField(max_length=1020)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add = True)

    objects = PostQuerySet.as_manager()



# end of file
