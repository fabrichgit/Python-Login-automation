from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
from login import email, password

options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')
time.sleep(2)

# find username and password input fields
email_input = driver.find_element(By.NAME, 'session_key')
password_input = driver.find_element(By.NAME, 'session_password')

email_input.send_keys(email)
password_input.send_keys(password)

password_input.send_keys(Keys.RETURN)

# login_button = driver.find_element(By.XPATH, "//*[@data-litms-control-urn='login-submit']")[1]
# login_button.click()
# time.sleep(5)

connected = driver.current_url
if "feed" in connected :
    print('Login successful!')
else:
    print('Login failed!')

driver.quit()