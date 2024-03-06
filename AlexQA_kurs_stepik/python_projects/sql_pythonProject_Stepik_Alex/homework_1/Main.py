import sqlite3
from User import User

def login_check(login, db):
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()
    lenght_result = len(result)

    i = 0
    while i < lenght_result:
        #print(result[i][1])
        if str(login) == result[i][1]:
            print("Login fail")
            i += 1
            continue
        else:
            return str(login)


#Подключение к БД
db_registration = sqlite3.connect(r'registration.db')
print("Подключились к БД")
#Управление БД
cursor = db_registration.cursor()
# Запрашиваем весь список из БД чтобы проверить логин
cursor.execute("""SELECT * FROM users_data""")
result = cursor.fetchall()
lenght_result = len(result)

print(login_check('Ivan', db_registration))

###
print("1 - зарегистрировать нового пользователя")
print("2 - авторизоваться в системе")
print("3 - восстановить пароль")
selector = input('Введите цифру для выбора: ')

#1 - Регистрация нового пользователя
if selector == "1":
    print("Регистрация нового пользователя")

    #проверка логина на повторяемость
    new_login = input("Введите логин: ")

    password = input("Введите пароль: ")
    code = input("Введите кодовое слово: ")

    user_data = (new_login, password, code)
    cursor.execute("""INSERT INTO users_data(Login, Password, Code)
    VALUES(?, ?, ?);""", user_data)
    db_registration.commit()
    print("Создан новый пользователь: ")
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()
    print(result)




#2 - Авторизация
elif selector == "2":
    print("Авторизация")

    new_login = input("Введите логин: ")
    password = input("Введите пароль: ")

    print("ВЫ успешно авторизовались")
    print("Проверьте корректность введённых данных")

#3 - Восстановление пароля
elif selector == "3":
    print("Восстановление пароля")
    print("Для восстановления пароля необходимо ввести логина и кодовое слово")

    new_login = input("Enter login")
    code = input("Enter code")
    print("Проверьте корректность введённых данных")
    new_pass = input("Введите новы пароль")

# Закрываем соединение
db_registration.close()