import pytest

from app.models import Session


@pytest.fixture()
def session():
    session = Session()

    # We want the session be flushed and commited after each instance
    # to not violate FK constraints in DB
    def add_all(self, instances):
        for instance in instances:
            self.add(instance)
            self.flush()
            self.expunge(instance)

    # Override the originial add_all for this session
    session.add_all = add_all.__get__(session, Session)
    return session
