from flask import Blueprint, render_template

"""
    Note that in the below code,
    some arguments are specified when creating the Blueprint object
    The first argument, 'site', is the Blueprint's name,
    which is used by FLask's routing mechanism.

    The Second argument, __name__, is the Blueprint's import name,
    which Flask uses to locate the Blueprint's resources.
"""

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/history')
def history():
    return render_template('history.html')