# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the base models for homepage

# import the django models
from django.db import models

# base models
class Project(models.Model):
    title = models.CharField(max_length=1020)
    description = models.CharField(max_length=1020)
    preview = models.FileField()
    link = models.CharField(max_length=1020, blank=True)

    # definitions for type choices
    TYPE_CHOICES = (
        ('project', 'project'),
        ('research', 'research')
    )

    type = models.CharField(max_length = 10, choices = TYPE_CHOICES)
    
    # the string behavior is to return the title
    def __str__(self):
        return self.title


# end of file
