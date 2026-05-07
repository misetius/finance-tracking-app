import pytest
from testcontainers.postgres import PostgresContainer
import os
from analysis.app import app
from analysis.tests.create_database_with_table import init_db




postgres = PostgresContainer("postgres:16-alpine")

@pytest.fixture(autouse=True)
def setup():
    postgres.start()
    os.environ["DB_CONN"] = postgres.get_connection_url()
    os.environ["DATABASE_HOST"] = postgres.get_container_host_ip()
    os.environ["DATABASE_PORT"] = str(postgres.get_exposed_port(5432))
    os.environ["DATABASE_USER"] = postgres.username
    os.environ["DATABASE_PASSWORD"] = postgres.password
    os.environ["DATABASE_NAME"] = postgres.dbname
    init_db()
    yield postgres
    postgres.stop()

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client