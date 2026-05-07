import os
import time
import psycopg2

def wait_for_db(max_retries=10, delay=3):
    for attempt in range(max_retries):
        try:
            conn = psycopg2.connect(
                database=os.getenv("DATABASE_NAME"),
                user=os.getenv("DATABASE_USER"),
                password=os.getenv("DATABASE_PASSWORD"),
                host=os.getenv("DATABASE_HOST"),
                port=os.getenv("DATABASE_PORT"),
            )
            print("Database connection successful")
            return conn
        except psycopg2.OperationalError as e:
            print(f"Database not ready, retrying... ({attempt+1}/{max_retries})")
            time.sleep(delay)

    raise Exception("Could not connect to database after multiple attempts")


def init_db():
    conn = wait_for_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id serial PRIMARY KEY,
            category varchar(100),
            product varchar(100),
            price float,
            year int,
            month int
        );
    """)

    conn.commit()  
    cur.close()
    conn.close()
    print("Table ensured.")