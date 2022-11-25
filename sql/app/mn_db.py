from sqlalchemy import MetaData, Table
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////tmp/test.db')
metadata = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

def init_db():
    metadata.create_all(bind=engine)