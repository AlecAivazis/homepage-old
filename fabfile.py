#!/usr/bin/env python
#
# this file describes the various tasks necessary to manage and build homepage
# author: alec aivazis

# the name of the project
project_name = "homepage"

# invoke imports
from fabric.api import local, cd, lcd

def server():
    """ run the local server """
    local('./manage.py runserver')


def init():
    """ perform the necessary tasks to initialize the project locally """

    # go into the folder with the dependency files
    with lcd('doc'):
        # install python dependencies
        local('pip install -r requirements.txt')
        # install bower dependencies
        local('bower install')

    # create the local database
    local('./manage.py syncdb')
    

def init_server():
    """ initialize the local project and then run the server """
    execute(init)
    execute(server)


def deploy():
    """ deploy the application to orthologue """




# end of file