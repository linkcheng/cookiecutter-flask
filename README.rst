cookiecutter-flask-simple
==================

A Flask template for cookiecutter_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter


Use it now
----------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/linkcheng/cookiecutter-flask-simple.git

You will be asked about your basic info (project name, etc.). This info will be used in your new project.

Features
--------

- Configuration in environment variables, as per `The Twelve-Factor App <https://12factor.net/config>`_
- Procfile for deploying to a PaaS (e.g. Heroku)
- pytest and Factory-Boy for testing (example tests included)
- Flask's Click CLI configured with simple commands
- Caching using Flask-Cache
- Utilizes best practices: `Blueprints <http://flask.pocoo.org/docs/blueprints/>`_ and `Application Factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_ patterns

Inspiration
-----------

- `Building Websites in Python with Flask <http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/>`_
- `Getting Bigger with Flask <http://maximebf.com/blog/2012/11/getting-bigger-with-flask/>`_
- `Structuring Flask Apps <http://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/>`_
- `Flask-Foundation <https://github.com/JackStouffer/Flask-Foundation>`_ by `@JackStouffer <https://github.com/JackStouffer>`_
- `flask-bones <https://github.com/cburmeister/flask-bones>`_ by `@cburmeister <https://github.com/cburmeister>`_
- `flask-basic-registration <https://github.com/mjhea0/flask-basic-registration>`_ by `@mjhea0 <https://github.com/mjhea0>`_
- `Flask Official Documentation <http://flask.pocoo.org/docs/>`_

Changelog
---------
0.2 (10/15/2018)
*******************

- Add logging & raven


0.1 (10/12/2018)
*******************

- First iteration
- Based on https://github.com/sloria/cookiecutter-flask

