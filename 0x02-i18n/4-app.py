#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel

class Config(object):
    """ Configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel()

@babel.localeselector
def get_locale() -> str:
    """
    Select and return best language match based on supported languages.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', method=['GET'])
def index() -> str:
    """Handles index route"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
