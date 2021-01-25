from flask import render_template

from . import main
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


@main.route('/settings')
def settings():
    return render_template('settings.html')
