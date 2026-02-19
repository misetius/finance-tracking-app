from flask import Flask, request
import psycopg2
import os



app = Flask(__name__)


conn = psycopg2.connect(database=os.getenv("DATABASE_NAME"), user=os.getenv("DATABASE_USER"),
                        password=os.getenv("DATABASE_PASSWORD"), host=os.getenv("DATABASE_HOST"), port=os.getenv("DATABASE_PORT"))
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS products (id serial  PRIMARY KEY, category  varchar(100), product varchar(100) , price float, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')

cur.close()
conn.close()



@app.route('/')
def get_all_data_from_tables():

    conn = psycopg2.connect(database=os.getenv("DATABASE_NAME"), user=os.getenv("DATABASE_USER"),
                        password=os.getenv("DATABASE_PASSWORD"), host=os.getenv("DATABASE_HOST"), port=os.getenv("DATABASE_PORT"))

    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {'data': rows}


@app.route('/add_data', methods=['POST'])
def add_data_to_table():


    conn = psycopg2.connect(database=os.getenv("DATABASE_NAME"), user=os.getenv("DATABASE_USER"),
                        password=os.getenv("DATABASE_PASSWORD"), host=os.getenv("DATABASE_HOST"), port=os.getenv("DATABASE_PORT"))

    cur = conn.cursor()

    category = request.form['category']
    product = request.form['product']
    price = request.form['price']


    cur.execute("INSERT INTO products (category, product, price) VALUES (%s, %s, %s)", (category, product, price))
    conn.commit()
    cur.close()
    conn.close()
    return {'message': 'Data added successfully'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv("PORT"))

  