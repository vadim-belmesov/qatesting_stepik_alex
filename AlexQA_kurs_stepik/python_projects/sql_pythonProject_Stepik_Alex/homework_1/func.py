"""Функция проверки логина"""
def login_check(new_login, db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()
    lenght_result = len(result)
    if new_login.isdigit():
        print("Логин не может быть цифрой!")
        return 0
    for i in range(0, lenght_result):
        if str(new_login) == str(result[i][1]):
            print(f"Введите, пожалуйста, другой логин, логин {new_login} уже существует в базе")
            return 0
        else:
            return 1

"""Функция проверки кода"""
def code_check(code):
    if code.isdigit() == True:
        if len(code) == 4:
            print(f"Код подходит, его длиина: {len(code)}")
            return 1
        else:
            print("Код должен содержать 4 целых числа!")
            return 0
    else:
        return 0
"""Проверка кода восстановления"""
def repair_code_check(code,login,db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()
    lenght_result = len(result)
    for i in range(0, lenght_result):
        if (login == result[i][1]) and (code == result[i][3]):
            return 0
        else:
            return 1

"""Функция проверки пароля"""
def password_check(new_pass):
    if len(new_pass) < 1:
        print("Пароль должен быть не пустой!")
        print(len(new_pass))
        return 0
    else:
        print("Пароль подходит")
        return 1

"""Проверка соответствия пароля логину"""
def auth_pass_chek(auth_login, pass1, db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()
    lenght_result = len(result)
    for i in range(0, lenght_result):
        if auth_login == result[i][1]:
            if pass1 == result[i][2]:
                return 1
            else:
                print("Вы ввели некорректные данные для авторизации!")
                return 0

"""Создание нового пароля"""
def create_new_password(login, new_password,db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()
    lenght_result = len(result)
    for i in range(0, lenght_result):
        if login == result[i][1]:
            # result[i][2] = new_password
            print("Новый пароль установлен")
            user_data = (new_password,login)
            cursor.execute("""UPDATE users_data SET Password = ? WHERE Login = ?;""", user_data)
            db.commit()  # Сохраниение запроса
            return 1

"""Удаление пользователя по ID(скрытая функция)"""
def del_user(user_id,db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()
    lenght_result = len(result)
    for i in range(0, lenght_result):
        print(result[i])
# Удаление данных в таблице
    cursor.execute("""DELETE FROM users_data WHERE UserID = ?;""", user_id)
    db.commit()