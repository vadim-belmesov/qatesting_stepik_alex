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
print(result)
print(lenght_result)
def login_check(new_login, db):
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()

    if new_login.isdigit():
        print("Логин не может быть цифрой!")
        return True

    for i in range(0,lenght_result):
        # print(result[i][1])
        if str(new_login) == str(result[i][1]):
            print("Login is present, enter new")
            return True
        else:
            print("Login OK")
            return False

print(login_check(str("Vas") ,db_registration))