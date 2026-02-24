import pytest
import psycopg2


pytest.hookimpl()
def pytest_sessionfinish():
    conn = psycopg2.connect(database="finance_db", user="user",
                        password="password", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM products")
    conn.commit()
    cur.close()
    conn.close()



