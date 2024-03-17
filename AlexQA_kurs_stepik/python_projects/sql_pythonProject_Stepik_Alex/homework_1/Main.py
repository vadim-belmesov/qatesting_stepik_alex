import sqlite3
"""Подключаем функции из файла (для улучшения читаемости кода)"""
from func import login_check, create_new_password, del_user
from func import password_check
from func import code_check
from func import auth_pass_chek
from func import repair_code_check

"""ВНИМАНИЕ! В коде использованы переменные-флаги с именами типа cnt_s3_2, 
что означает, что это счетчик (cnt), для селектора 3 (s3),
для данного селектора этот флаг под номером 2 (просто порядковый)"""

# Подключение к БД
db_registration = sqlite3.connect(r'registration.db')
print("Подключились к БД")
# Управление БД
cursor = db_registration.cursor()
# Запрашиваем весь список из БД чтобы проверить логин
cursor.execute("""SELECT * FROM users_data""")
result = cursor.fetchall()
lenght_result = len(result)

"""Список команд"""
cnt_0 = 0
while cnt_0 < 1:
    print(" 1 - зарегистрировать нового пользователя\n 2 - авторизоваться в системе\n 3 - восстановить пароль")
    selector = input('Введите цифру для выбора: ')
    if selector.isdigit() == False:
        print("Вы ввели символ, а не цифру!")
        cnt_0 = 0
    else:
        cnt_0 = 1

# 1 - Регистрация нового пользователя
if selector == "1":
    print("Регистрация нового пользователя")
    """Запускаем цикл для получения логина нового пользователя,
    который будет запущен, пока переменная а == True"""
    cnt_s1 = 0
    while cnt_s1 < 1:
# проверка логина на повторяемость
        new_login = str(input("Введите логин: "))
        cnt_s1 = login_check(str(new_login), db_registration)
    """Запускаем цикл для получения пароля,
    который будет запущен, пока переменная cnt_s1_2 < 1"""
    cnt_s1_2 = 0
    while cnt_s1_2 < 1:
        new_password = str(input("Введите пароль: "))
        cnt_s1_2 = password_check(new_password)

    """Запускаем цикл для получения кода,
    который будет запущен, пока переменная b == True"""
    b = 0
    while b < 1:
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

# 2 - Авторизация
elif selector == "2":
    print("Авторизация")

    cnt_s2 = 0
    while cnt_s2 < 1:
        login = input("Введите логин: ")
        cnt_s2 = login_check(login, db_registration)

    cnt_s2_1 = 0
    while cnt_s2_1 < 1:
        pas1 = input("Введите пароль: ")
        cnt_s2_1 = auth_pass_chek(login, pas1, db_registration)
    print(f"{login} ВЫ успешно авторизовались!")

# 3 - Восстановление пароля
elif selector == "3":
    print("Восстановление пароля")
    print("Для восстановления пароля необходимо ввести логин и кодовое слово")

    cnt_s3 = 0
    while cnt_s3 < 1:
        login = input("Введите логин: ")
        cnt_s3 = login_check(login, db_registration)  # 1 для существующего логина

# Получаем пароль для введённого логина
    for i in range(0, lenght_result):
        if login == result[i][1]:
            pas_for_login = result[i][2]
# Получение и проверка кода
    cnt_s3_2 = 0
    while cnt_s3_2 < 1:

# Проверка 4 знаков кода
        code = input("Введите 4х значный код: ")
        code_check(code)

# Проверка соответствия кода логину
        cnt_s3_2 = repair_code_check(code, login, db_registration)
        print(f"Код соответствует логину")

# Просьба ввести новый пароль и запись его в БД
    cnt_s3_3 = 0
    while cnt_s3_3 < 1:
        new_repair_password = input(f"Введите новый пароль для логина {login}: ")
        password_check(new_repair_password)
        cnt_s3_3 = create_new_password(login, new_repair_password, db_registration)
        print(f"Для пользователя {login} назначен новый пароль: {new_repair_password}")

# 33 - Удаление пользователя по ID(скрытая функция)
elif selector == "123333":
    print("Список пользователей выглядит так")
    for i in range(0, lenght_result):
        print(result[i])
    userID = str(input("Введите ID пользователя, которого нужно удалить: "))
    del_user(userID, db_registration)
    print(f"Удалён пользователь с ID = {userID} ")
    print("Текущий список пользователей выглядит так")
    for i in range(0, lenght_result):
        print(result[i])

# Закрываем соединение
db_registration.close()
