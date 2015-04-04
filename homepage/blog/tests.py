# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes tests for blog

# django imports
from django.test import TestCase
from django.utils import timezone
# homepage imports
from .models import Post

# define base tests

class PostTestCase(TestCase):
    """
    The test case for the Post schema
    """


    def setUp(self):
        """ Create the necessary models for the test case """
        self.first = Post.objects.create(title="first", body="first", post_date=timezone.now())
        self.second = Post.objects.create(title="second", body="second", post_date=timezone.now())


    def test_posts_retrieve_latest_first(self):
        """ verfiy that the latest post is first  """
        # get the latest post
        latest = Post.objects.latest_first()[0]
        # verify that is the was the one that was created second
        self.assertEqual(latest, self.second)


    def test_posts_retrieve_earliest_first(self):
        """ test that the earliest post is the first """
        # get the earliest post
        earliest = Post.objects.oldest_first()[0]
        # verify that it was the one that was created first
        self.assertEqual(earliest, self.first)


    def test_retrieve_by_slug(self):
        """ that that we can retrieve a particular post by its slug """
        # retrieve the post that has the second's slug
        retrieved = Post.objects.with_slug(self.second.slug)
        # verify that the two posts are the same
        self.assertEqual(retrieved, self.second)


# end of file
