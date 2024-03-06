import sqlite3
from User import User

#Подключение к БД
db_registration = sqlite3.connect(r'registration.db')
print("Подключились к БД")
#Управление БД
cursor = db_registration.cursor()
# Запрашиваем весь список из БД чтобы проверить логин
cursor.execute("""SELECT * FROM users_data""")

result = cursor.fetchall()
lenght_result = len(result)

while True:
    new_login = input("Введите логин: ")
    try:
        for i in range(0, lenght_result-1):
            if (new_login == result[0][i]):
                print("Login fail")
                break
            else:
                new_login = result[0][i]
                print(new_login)
    except ValueError:
        print("Ошибка")
