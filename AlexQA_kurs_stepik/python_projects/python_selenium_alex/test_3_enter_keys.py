import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

login_standart_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys(login_standart_user)
print("Input login")
password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys(password_all)
password.send_keys(Keys.RETURN)

"""Находим фильтр для сортировки, смещаем курсор на 1 позицию вниз, 
с помощью передачи клавиши DOWN """
filter_obj = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
filter_obj.click()
filter_obj.send_keys(Keys.DOWN)
filter_obj.send_keys(Keys.RETURN)

"""Делаем скриншот"""
timestamp_now = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
driver.save_screenshot('C:\\projects\\projects\\Stepik_Python_Alex\\qatesting_stepik_alex\\AlexQA_kurs_stepik\\python_projects\\python_selenium_alex\\screenshots\\' + 'scr_' + timestamp_now + '.png' )


""" Этот блок перепишем, вводя символы "вручную" (передавая их в ввод)
### enter password
input_password = driver.find_element(By.XPATH, "//*[@id='password']")
input_password.send_keys(password_all)
print("Input password")

### login button
login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")
login_button.click()
print("Click login button")
"""
time.sleep(5)
driver.close()