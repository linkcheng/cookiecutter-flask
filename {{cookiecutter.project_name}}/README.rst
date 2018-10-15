===============================
{{ cookiecutter.project_name }}
===============================

Quickstart
----------

Run the following commands to bootstrap your environment ::

    cd {{cookiecutter.project_name}}
    {%- if cookiecutter.use_pipenv == "yes" %}
    pipenv install --dev   # if error, try: pipenv run pip install pip==18.0
    {%- else %}
    pip install -r requirements/dev.txt
    {%- endif %}
    cp .env.example .env


Deployment
----------

To deploy::

    export FLASK_ENV=production
    export FLASK_DEBUG=0
    flask run       # start the flask server

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``.


Check
-----

To check the system is running ::

    1. "It works." will get when access http://127.0.0.1:5000/ .
    2. If "SENTRY_DSN" is configured in ".env" file, when access http://127.0.0.1:5000/error , there will raise an error and send a notification to sentry system.

Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests, run ::

    flask test
