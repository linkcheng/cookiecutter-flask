# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from werkzeug.utils import find_modules, import_string
from flask import Flask

from .utils import commands
from .util.error_track import client as sentry
from .extensions import cache, db, migrate


def create_app(config_object='app.settings'):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    if sentry:
        sentry.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    for name in find_modules('app.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'public_pb'):
            app.register_blueprint(mod.public_pb)

    return None


def register_shellcontext(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
        }

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
