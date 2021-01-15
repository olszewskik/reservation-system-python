from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    class NameForm(FlaskForm):
        name = StringField('What is your name?', validators=[DataRequired()])
        submit = SubmitField('Submit')

    @app.route('/', methods=['GET', 'POST'])
    def index():
        name = None
        form = NameForm()
        if form.validate_on_submit():
            name = form.name.data
            form.name.data = ''
        return render_template('index.html', form=form, name=name)

    @app.route('/settings')
    def settings():
        return render_template('settings.html')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    return app
