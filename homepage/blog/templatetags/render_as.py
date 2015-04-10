""" provides support for 'markdown' template tag """

# author: alec aivazis

import requests

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

# grab the template register
register = template.Library()


@register.filter
# make sure the value is a string
@stringfilter
def render_as(value, format):
    """ Render the text in the specified format """
    if format == 'markdown':
        return markdown(value)
    elif format == 'html':
        return html(value)
    elif format == 'text':
        return text(value)


def markdown(value):
    """ Render the text using a custom markdown engine """

    # define the request header
    headers = {'Content-type': 'text/plain'}

    # make a request to the github servers
    request = requests.post('https://api.github.com/markdown/raw', 
                                    headers=headers, data=value)

    # return the response text
    return mark_safe(request.text)

def html(value):
    """ Render the html """
    return mark_safe(value)

def text(value):
    """ Render the raw text """
    return mark_safe("<p>{}</p>".format(value))


# end of file