from flaskr import create_app
from flaskr.db import init_db

app = create_app()

with app.app_context():
    init_db()
    print("Database initialized.")
