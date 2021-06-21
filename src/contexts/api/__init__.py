from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object('src.contexts.api.config')
    app.config['CACHE_TYPE'] = 'simple'

    cors = CORS(app)

    from src.contexts.api.views import bp_views
    app.register_blueprint(bp_views)

    return app
