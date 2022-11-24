from flaskr.db import get_db


def data_view():
    db = get_db
    data = db.execute("SELECT * FROM user")