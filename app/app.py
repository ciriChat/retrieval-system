from flask import Flask

from .config import config_by_name
from .health_check.view import blueprint as health_check
from .idf.view import blueprint as idf_api
from .subtitle.view import blueprint as sub_api
from .morph.view import blueprint as morph_api
from .engine.view import blueprint as engine_api
from .emotions.view import blueprint as emotions_api


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(health_check)
    app.register_blueprint(idf_api)
    app.register_blueprint(sub_api)
    app.register_blueprint(morph_api)
    app.register_blueprint(engine_api)
    app.register_blueprint(emotions_api)

    from .db import db
    db.init_app(app)

    return app
