import pytest

from app.database import db_config


@pytest.fixture(autouse=True)
def use_test_database():
    db_config.url = "sqlite:///:memory:"
    db_config._engine = None
    db_config._session_local = None
    test_engine = db_config.get_engine()
    yield test_engine
