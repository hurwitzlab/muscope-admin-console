import os

import pytest
import sqlalchemy


@pytest.fixture
def session_class():
    return sqlalchemy.orm.sessionmaker(
        bind=sqlalchemy.create_engine(
            os.environ.get('MUSCOPE_DB_URI'), echo=False))
