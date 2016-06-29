from flask import Flask
from flask_wtf.csrf import CsrfProtect
from config import config

csrf = CsrfProtect()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    csrf.init_app(app)
    from web.demo import demo as demo_blueprint
    app.register_blueprint(demo_blueprint)
    return app
