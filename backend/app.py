from flask import Flask, request, jsonify
import time
import psycopg2
import psycopg2.extras
import os



app = Flask(__name__)


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
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()  
    cur.close()
    conn.close()
    print("Table ensured.")



@app.route('/')
def get_all_data_from_tables():

    conn = psycopg2.connect(database=os.getenv("DATABASE_NAME"), user=os.getenv("DATABASE_USER"),
                        password=os.getenv("DATABASE_PASSWORD"), host=os.getenv("DATABASE_HOST"), port=os.getenv("DATABASE_PORT"))

    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({'data': rows})


@app.route('/add-product', methods=['POST'])
def add_data_to_table():


    conn = psycopg2.connect(database=os.getenv("DATABASE_NAME"), user=os.getenv("DATABASE_USER"),
                        password=os.getenv("DATABASE_PASSWORD"), host=os.getenv("DATABASE_HOST"), port=os.getenv("DATABASE_PORT"))

    cur = conn.cursor()
    data = request.get_json()
    category = data.get("category") 
    product = data.get("product")
    price = data.get("price")


    cur.execute("INSERT INTO products (category, product, price) VALUES (%s, %s, %s)", (category, product, price))
    conn.commit()
    cur.close()
    conn.close()
    return {'message': 'Product added successfully'}, 201


if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=os.getenv("PORT"))

  