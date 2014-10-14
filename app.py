import config
from main import app_factory

app = app_factory(config=config.Dev)

from .flaskkeystone import flask_keystone

keystone = flask_keystone.Keystone(app)
keystone.init_app(app)