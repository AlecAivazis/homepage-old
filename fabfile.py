#!/usr/bin/env python
#
# this file describes the various tasks necessary to manage and build homepage
# author: alec aivazis

from fabric.api import *

# the server hosting the project
env.hosts = ['104.236.200.165']
# the user to connect to the server as
env.user = "homepage"


@task
def server():
    """ run the local server """
    local('./manage.py runserver')


@task
def update_dependencies():
    """ update the project dependencies """
    # go into the folder with the dependency files
    with lcd('doc'):
        # install python dependencies
        # install bower dependencies
        local('bower install')


@task
def init():
    """ perform the necessary tasks to initialize the project locally """
    # update the local dependencies
    update_dependencies()
    # create the local database
    local('./manage.py syncdb')


@task
def deploy():
    """ deploy the application """
    with cd('repository'):
        # update the repository
        run('git pull origin master')
        # update the local dependencies
        run('fab update_dependencies')
        # update the database
        run('./manage.py migrate')
        # update the static files
        run('./manage.py collectstatic')
        # restart the application server
        run('sudo service gunicorn restart')


# end of file