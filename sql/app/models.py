from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, Table
from sqlalchemy.orm import mapper
from app.mn_db import metadata, db_session


from app.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'

class MUser(object):
    query = db_session.query_property()

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f'<User {self.name!r}>'

user = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('email', String(120), unique=True)
)
mapper(User, user)


users = Table('users', metadata, autoload=True)