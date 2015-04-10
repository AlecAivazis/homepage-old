# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the models for blog

# python imports
import requests

# django imports
from django.db import models
from django.utils import timezone
from django.utils.text import slugify, Truncator
from django.core.exceptions import FieldError, ValidationError

# thirdparty imports
from taggit.managers import TaggableManager


class PostQuerySet(models.QuerySet):
    """
    The query set mangaer for blog posts
    """
    def latest_first(self):
        """ 
        Return the posts with the latest one first if there are visible entries ;
        Otherwise return an empty list
        """
        return self.visible().order_by('-post_date')

    def oldest_first(self):
        """ Return the posts with the oldest one first  """
        return self.latest_first().reverse()

    def visible(self):
        """
        Return the posts which should be shown to the public
        """
        return self.filter(post_date__lte = timezone.now())

    def get_with_slug(self, slug):
        """ Return the post with the matching slug """
        return self.get(slug = slug)

    def with_tag(self, tag):
        """ Return the posts that have the requested tag """
        return self.filter(tags__name__in = [tag])


class Post(models.Model):
    """
    The base class for entries in the blog
    """
    title = models.CharField(max_length=1020, unique=True)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add = True)
    post_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(blank=True, max_length=50)
    format = models.CharField(max_length = 20)

    tags = TaggableManager()

    objects = PostQuerySet.as_manager()


    def __str__(self):
        """ Return the string representation of the Post """
        return self.title


    @models.permalink
    def get_absolute_url(self):
        """ Return a permanent URL where this post can be viewed """
        return ('post_detail', (), {
            'slug': self.slug
        })


    def save(self, *args, **kwargs):
        """ Make sure we automatically generate the post slugs """
        # if the post has yet to go live or this is the first time its created
        if (self.post_date and self.post_date > timezone.now()) or not self.id or not self.slug:
            # set the slug of the post off of the first 50 characters
            self.slug = slugify(Truncator(self.title).chars(50))
        # save the changes
        super().save(*args, **kwargs)

    



# end of file
