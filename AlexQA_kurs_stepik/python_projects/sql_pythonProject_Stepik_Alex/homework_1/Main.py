import sqlite3
"""Подключаем функции из файла (для улучшения читаемости кода)"""
from func import login_check
from func import password_check
from func import code_check
from func import auth_pass_chek


#Подключение к БД
db_registration = sqlite3.connect(r'registration.db')
print("Подключились к БД")
#Управление БД
cursor = db_registration.cursor()
# Запрашиваем весь список из БД чтобы проверить логин
cursor.execute("""SELECT * FROM users_data""")
result = cursor.fetchall()
lenght_result = len(result)

"""Список команд"""
print("1 - зарегистрировать нового пользователя")
print("2 - авторизоваться в системе")
print("3 - восстановить пароль")
selector = input('Введите цифру для выбора: ')

#1 - Регистрация нового пользователя
if selector == "1":
    print("Регистрация нового пользователя")
    """Запускаем цикл для получения логина нового пользователя,
    который будет запущен, пока переменная а == True"""
    a = True
    while a == True:
        #проверка логина на повторяемость
        new_login = str(input("Введите логин: "))
        a = login_check(str(new_login), db_registration)
    """Запускаем цикл для получения пароля,
    который будет запущен, пока переменная с == True"""
    c = 1
    while c == True:
        new_password = str(input("Введите пароль: "))
        c = password_check(new_password)

    """Запускаем цикл для получения кода,
    который будет запущен, пока переменная b == True"""
    b = 1
    while b == True:
        code = input("Введите кодовое слово: ")
        b = code_check(code)

    """Записываем в БД данные о пользователе"""
    user_data = (new_login, new_password, code)
    cursor.execute("""INSERT INTO users_data(Login, Password, Code)
    VALUES(?, ?, ?);""", user_data)
    db_registration.commit()
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()
    print(f"Создан новый пользователь: {new_login}")

#2 - Авторизация
elif selector == "2":
    print("Авторизация")

    f = 0
    while f != True:
        login = input("Введите логин: ")
        f = login_check(login, db_registration) #true для существующего логина

    r = 0
    while r != True:
        pas1 = input("Введите пароль: ")
        r = auth_pass_chek(login, pas1, db_registration)
    print(f"{login} ВЫ успешно авторизовались!")

#3 - Восстановление пароля
elif selector == "3":
    print("Восстановление пароля")
    print("Для восстановления пароля необходимо ввести логин и кодовое слово")

    f = 0
    while f != True:
        login = input("Введите логин: ")
        f = login_check(login, db_registration)  # true для существующего логина

    g = 0
    while g != True:
        code = input("Enter code")
        new_pass = input("Введите новы пароль")

# Закрываем соединение
db_registration.close()