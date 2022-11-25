from app.db import db_session
from flask import Flask


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()