from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Audition, Role

engine = create_engine('sqlite:///theater.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()