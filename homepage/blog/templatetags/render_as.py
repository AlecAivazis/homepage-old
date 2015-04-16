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
    import markdown2
    # mark the rendered string as html safe
    return mark_safe(markdown2.markdown(value, 
                     extras=['fenced-code-blocks', 'footnotes']))


def html(value):
    """ Render the html """
    return mark_safe(value)


def text(value):
    """ Render the raw text """
    return mark_safe("<p>{}</p>".format(value))


# end of file