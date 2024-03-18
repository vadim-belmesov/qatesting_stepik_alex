import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

login_standart_user = "standard_user"
password_all = "secret_sauce"


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

''' Один вариант проверки успешной авторизации
### Локатор на первой странице
text_products = driver.find_element(By.XPATH, "//span[@class='title']")
### Сохраняем текст локатора в переменную
value_text_products = text_products.text
print(value_text_products)
### Проверяем значение
assert value_text_products == "Products"
print("Good")
'''

url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
# print(get_url)
assert url == get_url
print("Good URL")

# time.sleep(5)
# driver.close()