#!/usr/bin/env python

"""
Runserver
---------
This module is used to run the application with Flasks built in WSGI server.
Should NOT be used in production.

"""

# Import each "site" here, the last one being the "default"
from proteus import awesome_new_site, default_site


if __name__ == '__main__':
    import sys

    if (len(sys.argv) > 1):
        to_run = sys.argv[1]
        try:
            port = int(sys.argv[2])
        except:
            port = 5000
    else:
        to_run = 'default_site'
        port = 5000

    locals().get(to_run, 'default_site').app.run(port=port)
