# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request, redirect, url_for, flash
from jinja2  import TemplateNotFound

# App modules
from app import app, dbConn, cursor
# from app.models import Profiles

# App main route + generic routing

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/eventScheduling')
def eventScheduling():
    return render_template('createEvent.html')

@app.route('/profile')
def profile():
    return render_template('profileHome.html')