from app import app
from info import miembros
from flask import render_template


@app.route('/')
def index():
    """Base URL for website."""

    return render_template('home.html')


@app.route('/about')
def about():
    """URL for about section."""

    return render_template('about.html')

@app.route('/estructura')
def estructura():
    """Descripcion de cada estructura"""

@app.route('/members')
def members():
    """Apartado de miembroos"""
    members = miembros

    return render_template('members.html',miembros=members)