# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the models for blog

# django imports
from django.db import models
from django.utils import timezone
from django.utils.text import slugify, Truncator
from django.core.exceptions import FieldError, ValidationError

# python imports
import requests


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
        """
        Return the posts with the oldest one first
        """
        return self.latest_first().reverse()

    def visible(self):
        """
        Return the posts which should be shown to the public
        """
        return self.filter(post_date__lte = timezone.now())

    def get_with_slug(self, slug):
        """ Return the post with the matching slug """
        return self.get(slug = slug)


class Post(models.Model):
    """
    The base class for entries in the blog
    """
    title = models.CharField(max_length=1020, unique=True)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add = True)
    post_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(blank=True)
    format = models.CharField(max_length = 20)

    objects = PostQuerySet.as_manager()


    @property
    def body_clean(self):
        """ Return an HTML safe version of the body (render markdown if necessary) """
        # plaintext
        if self.format == 'text':
            # just return the content (it's already safe)
            return self.body
        # html
        elif self.format == 'html':
            # just return the content (it's already safe)
            return self.body
        # markdown
        elif self.format == 'markdown':
            # generate the html document using github's api
            content = ''
            # define the request header
            headers = {'Content-type': 'text/plain'}

            # make sure that the body is in the right encoding
            if type(self.body) == str:
                # encode the body as utf
                content = self.body.encode('utf-8')
            # otherwise if its a byte string
            elif type(self.body) == byte:
                # don't do anything
                content = self.body
            # otherwise its some crazy type I don't know about
            else:
                # throw an exception
                raise FieldError('Unable to encode post for GitHub api.')

            # make a request to the github servers
            request = requests.post('https://api.github.com/markdown/raw', 
                                            headers=headers, data=content)

            # return the response text
            return request.text.encode('utf-8')

        # otherwise it is a format I don't expect
        else:
            # throw an exception
            raise ValidationError('Unknown content format.')


    @property
    def preview(self):
        """ Generate a text preview of the post based on its content """
        # return the first 30 words of the body
        return " ".join(self.body.split(' ')[0:31]) + "..."


    @models.permalink
    def get_absolute_url(self):
        """ Return a permanent URL where this post can be viewed """
        return ('post_detail', (), {
            'slug': self.slug
        })


    def save(self, *args, **kwargs):
        """ Make sure we automatically generate the post slugs """
        # if the post has yet to go live or this is the first time its created
        if (self.post_date and self.post_date > timezone.now()) or not self.id:
            # set the slug of the post off of the first 50 characters
            self.slug = slugify(Truncator(self.title).chars(50))
        # save the changes
        super().save(*args, **kwargs)

    



# end of file
