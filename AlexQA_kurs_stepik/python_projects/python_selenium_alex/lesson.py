import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


driver.get('https://www.saucedemo.com/')
#driver.maximize_window()

# input_user_name = driver.find_element(By.ID, "user-name") #ID
# user_name = driver.find_element_by_id("user-name")
# input_user_name = driver.find_element(By.NAME, "user-name") #NAME
input_user_name = driver.find_element(By.XPATH, "//*[@id='user-name']") #XPATH to ID

input_user_name.send_keys("standard_user")
### enter password
# input_password = driver.find_element(By.ID, "password") #ID
# input_password = driver.find_element(By.CSS_SELECTOR, "#password") #CSS
input_password = driver.find_element(By.XPATH, "//*[@id='password']") #XPATH to class
input_password.send_keys("secret_sauce")

### login button
login_button = driver.find_element(By.XPATH, "//*[@value='Login']")
login_button.click()


time.sleep(5)
driver.close()