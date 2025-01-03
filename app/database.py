from contextlib import contextmanager
from typing import Generator

from models import Base
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker


def init_db(db_url: str = "sqlite:///./portfolio.db") -> Engine:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    return engine


engine = init_db()
SessionLocal = sessionmaker(bind=engine)


@contextmanager
def get_db_session() -> Generator[Session]:
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
