from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

Base=declarative_base()
from settings import s
DB="sqlite:///mobilelitebackend.db"

engine=create_engine(s.database_url)


SessionFactory=sessionmaker(bind=engine,autocommit=False,autoflush=False)


def connect():
    db=SessionFactory()
    try:
        yield db 
    finally:
        db.close()