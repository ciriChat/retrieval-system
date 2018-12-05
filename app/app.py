from flask import Flask

from .config import config_by_name
from .idf.view import blueprint as idf_api
from .subtitle.view import blueprint as sub_api


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(idf_api)
    app.register_blueprint(sub_api)

    from .db import db
    db.init_app(app)

    return app
