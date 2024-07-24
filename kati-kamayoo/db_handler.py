import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your host
            user="root",  # Replace with your username
            password="",  # Replace with your password
            database="katikamayoo"
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def create_table(cursor):
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            brand VARCHAR(255),
            title VARCHAR(255),
            current_price DECIMAL(10, 2),
            original_price DECIMAL(10, 2),
            amount_sold INT
        )
        """)
        print("Table is ready")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_data(cursor, product_data):
    try:
        for product in product_data:
            # brand gets the first value of product tuple and so on...aks tuple unpacking
            brand, title, current_price, original_price, amount_sold = product
            cursor.execute("""
            INSERT INTO products (brand, title, current_price, original_price, amount_sold)
            VALUES (%s, %s, %s, %s, %s)
            """, (brand, title, current_price, original_price, amount_sold))
        print("Data insertion successful")
    except Error as e:
        print(f"Error inserting data: {e}")

def close_db_connection(cursor, db_connection):
    try:
        if db_connection is not None and db_connection.is_connected():
            cursor.close()
            print("Cursor closed")
            db_connection.close()
            print("Database connection closed")
    except Error as e:
        print(f"Error closing the connection: {e}")