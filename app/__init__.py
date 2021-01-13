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
        routes_list = app.url_map.iter_rules()
        return render_template('index.html', routes_list=routes_list)

    @app.route('/settings')
    def settings():
        return render_template('settings.html')

    return app
