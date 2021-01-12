from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from config import config

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/settings')
    def settings():
        return render_template('settings.html')

    return app
