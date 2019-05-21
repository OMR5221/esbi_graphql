# Establish and define our database connections using SQLAlchemy:
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from sqlalchemy.orm import scoped_session, sessionmaker

#Define our various connection strings
conn_str = 'oracle://SCHEMA:password@DB'

engine = create_engine(conn_str)

# Create a sesion for the connection to the DB to use to run queries:
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))

# Will be used as an inheritance class to our defined Models:
# DeferredRefection: Allows us to reflect db table and just define primary and foreign keys
Base = declarative_base(cls=DeferredReflection)
Base.query = db_session.query_property()
Base.metadata.create_all(bind=engine)
