from flask import Flask, request, jsonify
import time
import psycopg2
import psycopg2.extras
import os

app = Flask(__name__)

env = os.environ.get("DEVELOPMENT_OR_PRODUCTION")

if env == "production":
    app.config["DEBUG"] = False
    secret = os.getenv("SECRET_KEY")
    if not secret:
        raise Exception("SECRET_KEY environment variable is required in production")
else:
    app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def check_health():
    return jsonify({'message': 'API is running'}), 200


@app.route('/sums-by-category', methods=['GET'])
def get_sums_by_category():
    data = request.get_json()
    year = data.get("year")


    conn = psycopg2.connect(database=os.getenv("DATABASE_NAME"), user=os.getenv("DATABASE_USER"),
                        password=os.getenv("DATABASE_PASSWORD"), host=os.getenv("DATABASE_HOST"), port=os.getenv("DATABASE_PORT"))

    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("""
        SELECT category, SUM(price) as total_price FROM products WHERE year = %s GROUP BY category;
    """, (year,))
    rows = cur.fetchall()
    print(f"Calculated sums by category for year {year}: {rows}")
    cur.close()
    conn.close()
    return jsonify({'data': rows})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv("PORT"))