import sqlite3

import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()



''' g is a special object that is unique for each request.
 It is used to store data that might be accessed by multiple functions during the request.
   The connection is stored and reused instead of creating a new connection if get_db is 
   called a second time in the same request.
   current_app is another special object that points to the Flask application handling the 
   request. Since you used an application factory, there is no application object when writing
     the rest of your code. get_db will be called when the application has been created and is
       handling a request, so current_app can be used'''
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

''' click.command() defines a command line command called init-db that calls the init_db 
function and shows a success message to the user.'''
#Register with the Application
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

''' app.teardown_appcontext() tells Flask to call that function when cleaning up after returning the response.

app.cli.add_command() adds a new command that can be called with the flask command.
Import and call this function from the factory. Place the new code at the end of the factory function before returning the app.

'''