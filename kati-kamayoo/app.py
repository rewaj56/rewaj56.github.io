from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",  # Replace with your host
        user="root",       # Replace with your username
        password="",       # Replace with your password
        database="katikamayoo"
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Query to get all unique brands
    cursor.execute("SELECT DISTINCT brand FROM products")
    brands = [row['brand'] for row in cursor.fetchall()]
    
    brand_data = {}
    brand_earnings = {}
    brand_items_sold = {}

    for brand in brands:
        # Query to get products for each brand and calculate totals
        cursor.execute("""
            SELECT id, title, current_price, amount_sold,
                   (current_price * amount_sold) AS total,
                   SUM(amount_sold) OVER() AS total_items_sold
            FROM products
            WHERE brand = %s
        """, (brand,))
        products = cursor.fetchall()
        
        # Calculate total earnings for the brand
        total_earnings = sum(product['total'] for product in products)
        # Get the total items sold for the brand (assuming it's the same for all rows)
        total_items_sold = products[0]['total_items_sold'] if products else 0
        
        brand_data[brand] = products
        brand_earnings[brand] = total_earnings
        brand_items_sold[brand] = total_items_sold
    
    cursor.close()
    connection.close()
    
    # Prepare data for chart
    brand_labels = list(brand_earnings.keys())
    brand_earnings_values = list(brand_earnings.values())
    brand_items_sold_values = list(brand_items_sold.values())
    
    return render_template(
        'product_list.html',
        brand_data=brand_data,
        brand_labels=brand_labels,
        brand_earnings=brand_earnings_values,
        brand_items_sold=brand_items_sold_values
    )

if __name__ == '__main__':
    app.run(debug=True)
