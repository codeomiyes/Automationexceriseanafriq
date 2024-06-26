from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Setup Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the website
driver.get("https://www.automationexercise.com/")

# Locate the Sign-In button and click it
sign_in_button = driver.find_element(By.XPATH, '//*[@href="/login"]')
sign_in_button.click()

# Locate the email input field and enter the email address
email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys('qat@mailinator.com')

# Locate the password input field and enter the password
password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys('123456')

# Locate the login button and click it to submit the login form
login_button = driver.find_element(By.XPATH, '//button[@data-qa="login-button"]')
login_button.click()

# Wait for a moment to ensure the page loads properly after login
time.sleep(5)

# Navigate to the section containing featured items
driver.get("https://www.automationexercise.com/")

# Wait for the featured items to load
time.sleep(5)

# Extract the HTML content of the featured items section
featured_items_section = driver.find_element(By.CLASS_NAME, 'features_items')
html_content = featured_items_section.get_attribute('outerHTML')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all overlay-content divs
items = soup.find_all('div', class_='overlay-content')

# Extract labels and prices
item_list = []
for item in items:
    price_text = item.find('h2').text
    label = item.find('p').text
    price = int(price_text.replace('Rs. ', ''))
    item_list.append((label, price))

# Sort items by price (low to high)
sorted_items = sorted(item_list, key=lambda x: x[1])

# Print sorted items
for label, price in sorted_items:
    print(f'{label}: Rs. {price}')

# Click on the "Women" toggle
women_toggle = driver.find_element(By.CSS_SELECTOR, 'a[data-toggle="collapse"][href="#Women"]')
women_toggle.click()


# Wait for the "Tops" link to be clickable
tops_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Tops")]')))

# Click on the "Tops" link
tops_link.click()


time.sleep(5)


# Find the "Add to cart" button for Fancy Green Top and click it
fancy_green_top_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//p[text()="Fancy Green Top"]/following-sibling::a[@class="btn btn-default add-to-cart"]'))
)
fancy_green_top_button.click()

# Click "Continue Shopping" in the modal popup
continue_shopping_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="modal-footer"]/button[@class="btn btn-success close-modal btn-block" and text()="Continue Shopping"]'))
)
continue_shopping_button.click()

# Find the "Add to cart" button for Summer White Top and click it
summer_white_top_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//p[text()="Summer White Top"]/following-sibling::a[@class="btn btn-default add-to-cart"]'))
)
summer_white_top_button.click()

# Navigate to "View Cart"
view_cart_link = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "/view_cart")]'))
)
view_cart_link.click()


# Proceed to Checkout
proceed_to_checkout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.col-sm-6 a.btn.check_out'))
)
proceed_to_checkout_button.click()

# Enter Comment
comment_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea.form-control'))
)
comment_box.clear()
comment_box.send_keys('This segun cart, for automation exercise')

# Place the Order
place_order_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[@href="/payment" and @class="btn btn-default check_out"]'))
)
place_order_button.click()


# Wait for the payment page to load
time.sleep(4)

# Enter payment details
name_on_card_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="name_on_card"]'))
)
name_on_card_input.send_keys('Test card')

card_number_input = driver.find_element(By.CSS_SELECTOR, 'input[name="card_number"]')
card_number_input.send_keys('4100 0000 0000')

cvc_input = driver.find_element(By.CSS_SELECTOR, 'input[name="cvc"]')
cvc_input.send_keys('123')

expiry_month_input = driver.find_element(By.CSS_SELECTOR, 'input[name="expiry_month"]')
expiry_month_input.send_keys('01')

expiry_year_input = driver.find_element(By.CSS_SELECTOR, 'input[name="expiry_year"]')
expiry_year_input.send_keys('1900')

# Click the "Pay and Confirm Order" button
pay_and_confirm_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="pay-button"]'))
)
pay_and_confirm_button.click()


time.sleep(30)


driver.quit()
