from app import app

from flask import render_template


@app.route('/')
def index():
    """Base URL for website."""

    return render_template('home.html')


@app.route('/about')
def about():
    """URL for about section."""

    return render_template('about.html')
