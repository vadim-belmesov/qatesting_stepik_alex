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
# print(result)
#print(lenght_result)

def auth_pass_chek(auth_login, pass1, db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()
    lenght_result = len(result)
    print(lenght_result)

    for i in range(0, lenght_result):
        print(f"{result[i][1]} : {result[i][2]}")
        if auth_login == result[i][1]:
            if pass1 == result[i][2]:
                print(pass1)
                return False
    print("Вы ввели некорректные данные для авторизации!")

auth_pass_chek("888" , "222", db_registration)