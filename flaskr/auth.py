# -*- coding: utf-8 -*-

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = "User {} is already registered.".format(username)

            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
''' If the user submitted the form, request.method will be 'POST'. In this case, start validating the input.

request.form is a special type of dict mapping submitted form keys and values. The user will input their username and password.

Validate that username and password are not empty.

If validation succeeds, insert the new user data into the database.'''

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
''' session is a dict that stores data across requests. When validation succeeds, 
the user’s id is stored in a new session. The data is stored in a cookie that is 
sent to the browser, and the browser then sends it back with subsequent requests.
 Flask securely signs the data so that it can’t be tampered with.'''

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
''' The url_for() function generates the URL to a view based on a name and arguments. 
The name associated with a view is also called the endpoint, 
and by default it’s the same as the name of the view function.'''
