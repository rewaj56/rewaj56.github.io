from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
url = "https://www.daraz.com.np/anker/"
driver.get(url)

# Wait for the dynamic content to load
time.sleep(5)

# Find all product divs using their common class
product_divs = driver.find_elements(By.CLASS_NAME, 'description--H8JN9')

# Check if product divs are found
if product_divs:
    print(f"Found {len(product_divs)} product(s).")
else:
    print("No products found with the class 'description--H8JN9'.")

# Iterate through each product div and extract information
for index, product_div in enumerate(product_divs):
    print(f"Processing product {index + 1}")

    title_div = product_div.find_element(By.CLASS_NAME, 'title-wrapper--IaQ0m').text.strip()
    current_price_div = product_div.find_element(By.CLASS_NAME, 'current-price--Jklkc').text.strip()
    original_price_div = product_div.find_element(By.CLASS_NAME, 'original-price--lHYOH').text.strip()

    # Check if the 'Sold' text exists in the product div
    amount_sold_elem = product_div.find_elements(By.XPATH, ".//div[contains(text(), 'Sold')]")
    if amount_sold_elem:
        amount_sold_div = amount_sold_elem[0].text.strip()
    else:
        amount_sold_div = "Amount sold not found"

    print(f"Product Title: {title_div}")
    print(f"Current Price: {current_price_div}")
    print(f"Original Price: {original_price_div}")
    print(f"Amount Sold: {amount_sold_div}")
    print('-' * 40)

# Close the WebDriver
driver.quit()