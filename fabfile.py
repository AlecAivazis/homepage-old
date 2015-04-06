#!/usr/bin/env python
#
# this file describes the various tasks necessary to manage and build homepage
# author: alec aivazis

# invoke imports
from fabric.api import local

def server():
    """ run the local server """
    local('./manage.py runserver')


# end of file