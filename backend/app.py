from flask import Flask, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="finances_db", user="postgres",
                        password="root", host="localhost", port="5432")
cur = conn.cursor()




@app.route('/')
def get_all_data_from_tables():

    return 'Hello, World!'


@app.route('/add_data', methods=['POST'])
def add_data_to_table():



    conn = psycopg2.connect(database="finances_db",
                            user="postgres",
                            password="root",
                            host="localhost", port="5432")

    cur = conn.cursor()

    category = request.form['category']
    product = request.form['product']
    price = request.form['price']


    cur.execute("INSERT INTO products (category, product, price) VALUES (%s, %s, %s)", (category, product, price))
    conn.commit()
    return 'Data added successfully!'

if __name__ == '__main__':
    app.run()

  