from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import csv
import db_handler

def clean_data(data):
    return data.replace('Rs.', '').replace(',', '').strip()

def extract_number(text):
    match = re.search(r'(\d+(\.\d+)?)([Kk])?', text)
    if match:
        number = float(match.group(1))
        if match.group(3) and match.group(3).lower() == 'k':
            number *= 1000
        return int(number)
    return 0

def clean_title(title):
    if ',' in title:
        return title.split(',')[0].strip()
    elif '|' in title:
        return title.split('|')[0].strip()
    else:
        return title.strip()

def extract_brand_from_url(url):
    # Split the URL by '/' and get the last part
    parts = url.split('/')
    brand_part = parts[-2]  # Get the second last part
    
    # Remove any suffix like '-brand'
    brand_name = re.sub(r'-brand$', '', brand_part)
    return brand_name

# List of URLs to scrape
urls = [
    "https://www.daraz.com.np/anker/",
    "https://www.daraz.com.np/xiaomi/",
    "https://www.daraz.com.np/redmi/",
    "https://www.daraz.com.np/fantech/",
    "https://www.daraz.com.np/erke/",
    "https://www.daraz.com.np/smartphones/samsung-brand/",
    "https://www.daraz.com.np/apple/",
    "https://www.daraz.com.np/midea/",
    "https://www.daraz.com.np/fashion-jewellery/masala-beads/",
    "https://www.daraz.com.np/home-appliances/philips/",
    "https://www.daraz.com.np/realme/",
]

# Initialize WebDriver
driver = webdriver.Firefox()

# List to store product data
product_data = []

for url in urls:
    driver.get(url)

    # Wait for the dynamic content to load
    time.sleep(5)

    # Find all product divs using their common class
    product_divs = driver.find_elements(By.CLASS_NAME, 'description--H8JN9')

    # Check if product divs are found
    if product_divs:
        print(f"Found {len(product_divs)} product(s) for {url}.")
    else:
        print(f"No products found with the class 'description--H8JN9' for {url}.")

    # Iterate through each product div and extract information
    for index, product_div in enumerate(product_divs):
        print(f"Processing product {index + 1} for {url}")

        title = product_div.find_element(By.CLASS_NAME, 'title-wrapper--IaQ0m').text.strip()
        current_price = product_div.find_element(By.CLASS_NAME, 'current-price--Jklkc').text.strip()
        original_price = product_div.find_element(By.CLASS_NAME, 'original-price--lHYOH').text.strip()

        current_price = clean_data(current_price)
        original_price = clean_data(original_price)

        # Check if the 'Sold' text exists in the product div
        amount_sold_elem = product_div.find_elements(By.XPATH, ".//div[contains(text(), 'Sold')]")
        if amount_sold_elem:
            amount_sold = extract_number(amount_sold_elem[0].text.strip())
        else:
            amount_sold = 0

        cleaned_title = clean_title(title)
        brand = extract_brand_from_url(url)

        # Store the data in the list
        product_data.append([brand, cleaned_title, current_price, original_price, amount_sold])

        print(f"Product Title: {cleaned_title}")
        print(f"Current Price: {current_price}")
        print(f"Original Price: {original_price}")
        print(f"Amount Sold: {amount_sold}")
        print(f"Brand: {brand}")
        print('-' * 40)

# Close the WebDriver
driver.quit()

db_connection = db_handler.connect_to_db()
if db_connection is not None:
    cursor = db_connection.cursor()

    db_handler.create_table(cursor)
    db_handler.truncate_table(cursor)
    db_handler.insert_data(cursor, product_data)
    db_connection.commit()

    db_handler.close_db_connection(cursor, db_connection)
else:
    print("Failed to connect to the database. Data not inserted.")
