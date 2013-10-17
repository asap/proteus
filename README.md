=============================
Proteus
=============================

Getting Started
===============

Requirements
++++++++++++

Before you can install the project, make sure ``virtualenvwrapper`` is
installed::

    $ pip install -U virtualenvwrapper

Installation
++++++++++++

After cloning the repository, activate the virtual environment::

    $ mkvirtualenv proteus

Install required packages

    $ pip install -r requirements/development.txt

Run the default site

    $ python runserver.py default_site

Run the second, more awesome, site in a new terminal session

    $ python runserver.py awesome_new_site


Running Tests
=============

To test, (make sure you've installed development requirements) simply::

    $ nosetests -s tests/
