# -*- coding: utf-8 -*-
"""
Awesome New Site
==================

This will be the new website init

"""

from flask import Flask
from flask.ext.themes2 import Themes

from .blueprint import blueprint
from .config import Config

app = Flask('awesome_new_site')

# this try block allows local development settings to be set
try:
    app.config.from_pyfile('proteus/awesome_new_site.cfg')
except (RuntimeError, IOError):
    # local settings are not found, we can pass
    pass

# Register blueprint and theme
app.register_blueprint(blueprint)
Themes(app, app_identifier='proteus')
