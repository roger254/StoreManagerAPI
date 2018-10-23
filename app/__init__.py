from flask_api import FlaskAPI

from instance.config import app_config
from app.api.v1.views.products import ProductView


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # Views
    ProductView.register(app, route_base='/products/')

    return app
