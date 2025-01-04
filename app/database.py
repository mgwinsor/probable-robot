from contextlib import contextmanager
from typing import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.models import Base


class DatabaseConfig:
    def __init__(self, url="sqlite:///./portfolio.db") -> None:
        self.url = url
        self._engine = None
        self._session_local = None

    def get_engine(self) -> Engine:
        if self._engine is None:
            self._engine = create_engine(db_config.url)
            Base.metadata.create_all(self._engine)
        return self._engine

    def get_session_maker(self) -> sessionmaker[Session]:
        if self._session_local is None:
            self._session_local = sessionmaker(bind=self.get_engine())
        return self._session_local


db_config = DatabaseConfig()


@contextmanager
def get_db_session() -> Generator[Session]:
    session_maker = db_config.get_session_maker()
    db = session_maker()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
