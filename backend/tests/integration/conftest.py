import pytest
from testcontainers.postgres import PostgresContainer

postgres = PostgresContainer("postgres:16-alpine")

@pytest.fixture(scope="module", autouse=True)
def setup():
    postgres.start()
    yield postgres
    postgres.stop()

