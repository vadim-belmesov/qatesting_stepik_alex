import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
# time.sleep(5)
# driver.close()

login_standart_user = "standard_userR"
password_all = "secret_sauce"

### enter login
input_user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
input_user_name.send_keys(login_standart_user)
print("Input login")

### enter password
input_password = driver.find_element(By.XPATH, "//*[@id='password']")
input_password.send_keys(password_all)
print("Input password")

### login button
login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")
login_button.click()
print("Click login button")

warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warning_text = warning_text.text
assert value_warning_text == "Epic sadface: Username and password do not match any user in this service"
print("Login incorrect " + "Good negative test")