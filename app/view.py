
# -*- coding: utf-8 -*-
import os
from flask import (Blueprint, render_template, request, redirect, url_for,
                   session, flash, current_app as app)

import simplejson

views = Blueprint('views', __name__, static_folder='static', template_folder='templates')

from model import *

@views.route('/')
def root():
    app.logger.debug(User.query.count())
    app.logger.debug(os.environ.get('DATABASE_URL'))
    
    return simplejson.dumps([ dict(id = u.id,
                                   user_name = u.user_name,
                                   email = u.email) for u in User.query.all()])

@views.route('/create')
def create():
    db.create_all()
    return 'create_all'

@views.route('/add')
def add():
    admin = User('admin', 'admin@example.com')
    guest = User('guest', 'guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return 'add'

@views.teardown_request
def teardown_request(exception):
    db.session.remove()

@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html', session=session), 404

@views.app_errorhandler(500)
def page_not_found(error):
    """Custom 500 page."""
    # Insert error logging here.
    return render_template('500.html', session=session), 500
