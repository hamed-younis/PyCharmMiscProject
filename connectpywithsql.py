import psycopg2

# 1. Credentials config
DB_CONFIG = {
    "dbname": "practising",
    "user": "postgres",
    "password": "Abo12daa",
    "host": "localhost",
    "port": "5432",
}

# 2. Open context, run query, auto-close
try:
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            # Run test query
            cur.execute("SELECT * from customers where customer_id =49;")
            db_version = cur.fetchall()
            print(f"Connected to: {db_version}")

except Exception as e:
    print(f"Database error: {e}")
