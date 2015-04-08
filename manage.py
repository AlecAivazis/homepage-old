#!/usr/bin/env python3
#
# alec aivazis
# 
 
#

# main
if __name__ == "__main__":
    # externals
    import os
    import sys
    # point django to the project settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homepage.settings.live")
    # pull the shell
    import django.core.management
    # and invoke it
    django.core.management.execute_from_command_line(sys.argv)

# end of file
