from selenium import webdriver
from configparser import ConfigParser
import time
import os

CONFIG = ConfigParser()
CONFIG.read('config.ini')

EMAIL = CONFIG.get('LOGIN DETAILS', 'EMAIL')
PASSWORD = CONFIG.get('LOGIN DETAILS', 'PASSWORD')
PHONE = CONFIG.get('PAYMENT DETAILS', 'PHONE')
WEBSITE = CONFIG.get('URL', 'WEBSITE')
URL = CONFIG.get('URL', 'URL')
ADDRESS = CONFIG.get('ADDRESS', 'ADDRESS')

# For headless browser
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--ignore-ssl-errors')
# driver = webdriver.Chrome(execute_path=os.environ.get("CHROMEDRIVER_PATH"),
#     chrome_options=chrome_options)


# For gui browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe', options=chrome_options)
driver.maximize_window()
#driver.execute_script("window.scrollTo(0, 4500)") 


# Login into Flipkart
def login_fk():
    try:
        login = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[3]/div/div/div/a')
        login.click()
        email_field_element_loc = '/html/body/div[3]/div/div/div/div/div[2]/div/form/div[1]/input'
        password_field_element_loc = '/html/body/div[3]/div/div/div/div/div[2]/div/form/div[2]/input'
        email_field = driver.find_element_by_xpath(email_field_element_loc)
        password_field = driver.find_element_by_xpath(password_field_element_loc)
        email_field.send_keys(EMAIL)
        password_field.send_keys(PASSWORD)
        print("Details entered✅")
        enter = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div/form/div[3]/button')
        enter.click()
        print('Logging in as {}'.format(EMAIL))
    except:
        print('Login Failed. Retrying.')
        time.sleep(0.1) 
        login_fk()

# Adds item to cart for flipkart website
def add_to_cart_fk():
    start_time = time.time()
    add_to_cart_option = False
    while add_to_cart_option is False:
        try:
            time.sleep(0.15)
            driver.execute_script("window.scrollTo(0, 4200)")
            add_to_cart = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/ul/li[1]/button')
            print('Add To Cart button appeared🛒')
            add_to_cart.click()
            add_to_cart_option = True
        except:
            add_to_cart_option = False
            text = 'Add To Cart option is unavailable...retrying: ' + time.ctime()
            print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(255,128,0, text))
            driver.refresh()
    if add_to_cart_option is True:
        text = 'Congratulations, Item added to cart cart successfully. Please checkout as soon as possible!'
        print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(0,255,0, text))
        width = os.get_terminal_size().columns
        text = '        (Took {} seconds)'.format(time.time()-start_time)
        print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(124,252,0, text).center(width))

# Perform a check if the item is acctually added in the cart
def check_cart_fk():
    try:
        item = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div/div[1]/div/div[3]/div/form/button')
        print("Your item is present in the cart.")
    except:
        print("Unable to find the item in the cart.")

if WEBSITE == "FLIPKART":
    add_to_cart_page_url = URL
    print("Logging in...")
    driver.get(add_to_cart_page_url)
    login_fk()

    email_field_element_loc = '/html/body/div[3]/div/div/div/div/div[2]/div/form/div[1]/input'
    while True:
        try:
            driver.find_element_by_xpath(email_field_element_loc)
        except:
            break

    add_to_cart_fk()

    while True:
        print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(255,255,0, '1. Check Cart'))
        print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(255,128,0, '2. Retry add to cart'))
        print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(255,0,0, '3. Exit Script'))
        ans = int(input())
        if ans == 1:
            check_cart_fk()
        elif ans == 2:
            driver.get(add_to_cart_page_url)
            add_to_cart_fk()
        else:
            break

print("Exited Script")