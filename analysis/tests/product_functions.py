import psycopg2
import os
import time

def add_product(category, product, price):
    conn = psycopg2.connect(
        database=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT")
    )

    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO products (category, product, price, year, month)
        VALUES (%s, %s, %s, %s, %s)
    """, (category, product, price, year, month))
    conn.commit()
    cur.close()
    conn.close()