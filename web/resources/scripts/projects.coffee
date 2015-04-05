# this file describes the javascript functionality that is unique to my projects page
# author: alec

# when the document is ready
$(document).ready ->
    console.log 'hello'
    # initialize the popups
    $('.imageLink').magnificPopup
        type: 'image'


# end of file