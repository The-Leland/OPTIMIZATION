


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine = create_engine(os.getenv('DATABASE_URL'), echo=True)
metadata = MetaData()
metadata.reflect(bind=engine)

session = scoped_session(sessionmaker(bind=engine))
