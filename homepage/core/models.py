# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the base models for homepage

# django imports
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=1020)
    description = models.CharField(max_length=1020)
    preview = models.FileField()
    link = models.CharField(max_length=1020, blank=True)
    github = models.CharField(max_length=1020, blank=True)

    # definitions for type choices
    TYPE_CHOICES = (
        ('project', 'project'),
        ('research', 'research')
    )

    type = models.CharField(max_length = 10, choices = TYPE_CHOICES)
    
    # the string behavior is to return the title
    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        """ Return a permanent URL where this project can be viewed """
        return ('project_detail', (), {
            'name': self.title
        })


class ProjectScreenshot(models.Model):
    """ The model for a scheen shot associated with a given project """
    file = models.FileField()
    project = models.ForeignKey(Project, related_name="screenshots")


# end of file
