from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import csv

# Function to clean price and extract number from amount sold
def clean_data(data):
    return data.replace('Rs.', '').replace(',', '').strip()

def extract_number(text):
    match = re.search(r'\d+', text)
    return match.group(0) if match else "0"

# Function to clean titles based on punctuation
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
    # The brand name is the part before the query string or the end of the URL
    brand_name = parts[-2]  # Get the second last part
    return brand_name

# List of URLs to scrape
urls = [
    "https://www.daraz.com.np/anker/",
    "https://www.daraz.com.np/xiaomi/",
    "https://www.daraz.com.np/redmi/",
    "https://www.daraz.com.np/fantech/",
    # Add more brand URLs as needed
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

        # Clean the prices
        current_price = clean_data(current_price)
        original_price = clean_data(original_price)

        # Check if the 'Sold' text exists in the product div
        amount_sold_elem = product_div.find_elements(By.XPATH, ".//div[contains(text(), 'Sold')]")
        if amount_sold_elem:
            amount_sold = extract_number(amount_sold_elem[0].text.strip())
        else:
            amount_sold = "0"

        # Clean the title & Extract the brand
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

# Write the data to a CSV file
with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Brand", "Title", "Current Price", "Original Price", "Amount Sold"])
    # Write the product data
    writer.writerows(product_data)

print("Data has been written to products.csv")