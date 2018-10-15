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
    cp db.yml.default $DATABASE_CONFIG_FILE


Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration ::

    flask db init
    flask db migrate
    flask db upgrade

Deployment
----------

To deploy::

    export FLASK_ENV=production
    export FLASK_DEBUG=0
    flask run       # start the flask server

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``.


Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests, run ::

    flask test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.
