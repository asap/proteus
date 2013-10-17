"""
Views and shared functionality for sites

This is where the magic happens
"""

from flask import Blueprint, current_app

from flask.ext.themes2 import render_theme_template

from ..api import get_shows

blueprint = Blueprint('blueprint', __name__,
                      template_folder='templates',
                      static_folder='s')


@blueprint.route('/')
def index():
    """ This is the index """

    context = {}

    return render_theme_template(get_current_theme(), "index.html", **context)


@blueprint.route('/shows/')
def show_directory():
    """ Renders a list of shows """


    # Assuming you have an API that can return content based on a specific
    # key, this would be a potential usage.  This way, you can filter
    # content specific from your API based on sites or other logical
    # groupings
    context = {
        'shows': get_shows(site_id=get_current_theme())
    }

    return (render_theme_template(get_current_theme(), "shows.html",
            **context))


@blueprint.errorhandler(404)
def page_not_found(e):
    """ Renders 404 Error page """

    context = {}

    return (render_theme_template(get_current_theme(), '404.html', **context),
            404)

def get_current_theme():
    """ returns the name of the current theme """
    return current_app.name