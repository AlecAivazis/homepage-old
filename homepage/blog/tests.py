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
        self.first = Post.objects.create(title="first", body="first", post_date=timezone.now(), 
                                                                                format="markdown")
        self.second = Post.objects.create(title="second", body="second", post_date=timezone.now())
        # add different tags to each
        self.first.tags.add('first')
        self.second.tags.add('second')


    def test_filter_post_latest_first(self):
        """ verfiy that the latest post is first  """
        # get the latest post
        latest = Post.objects.latest_first()[0]
        # verify that is the was the one that was created second
        self.assertEqual(latest, self.second)


    def test_filter_post_earliest_first(self):
        """ test that the earliest post is the first """
        # get the earliest post
        earliest = Post.objects.oldest_first()[0]
        # verify that it was the one that was created first
        self.assertEqual(earliest, self.first)


    def test_filter_post_by_tag(self):
        """ test that we can retrieve posts by their tags """
        # return the post that matches 
        retrieved = Post.objects.with_tag('first')[0]
        # verify that we got the first one
        self.assertEqual(retrieved, self.first)


    def test_retrieve_by_slug(self):
        """ test that we can retrieve a particular post by its slug """
        # retrieve the post that has the second's slug
        retrieved = Post.objects.get_with_slug(self.second.slug)
        # verify that the two posts are the same
        self.assertEqual(retrieved, self.second)


    def test_can_clean_markdown(self):
        """ test that we can pass our stuff through a markdown engine """
        # check that we get a string back
        self.assertIsInstance(self.first.body_clean, str)



# end of file
