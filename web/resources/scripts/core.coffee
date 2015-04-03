# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
# this file describes the core javascript for {project.name}

# toggle the navigation menu
@toggleNav = ->
    # toggle the actual html element
    $('#navigation').toggle()


# when the document is ready for javascript
$(document).ready ->

    ## add event handlers

    # when the user clicks on the navigation gutter or the close element
    $(document).on 'click', '.close, #navigation', (event) ->
        # close the menu
        toggleNav()
        # prevent the event from bubbling up
        event.stopPropagation()
        
    # when the user clicks on the list container
    $(document).on 'click', '#navigation ul', (event) ->
        # prevent the event from bubbling up
        event.stopPropagation()


# end of file
