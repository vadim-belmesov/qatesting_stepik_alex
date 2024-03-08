"""Функция проверки логина"""

def login_check(new_login, db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()
    lenght_result = len(result)

    if new_login.isdigit():
        print("Логин не может быть цифрой!")
        return True
    for i in range(0,lenght_result):
        if str(new_login) == str(result[i][1]):
            print(f"Здравствуйте {new_login}")
            return True
        else:
            return False

"""Функция проверки кода"""
def code_check(code):
    if code.isdigit() == True:
        # print("digit")
        if len(code) == 4:
            print(f"Код подходит, его длиина: {len(code)}")
            return False
        else:
            print("Код должен содержать 4 целых числа!")
            return True

"""Функция проверки пароля"""
def password_check(new_pass):
    if len(new_pass) < 1:
        print("Пароль должен быть не пустой!")
        print(len(new_pass))
        return True
    else:
        print("Пароль подходит")
        return False

"""Проверка соответствия пароля логину"""
def auth_pass_chek(auth_login, pass1, db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM users_data""")
    result = cursor.fetchall()
    lenght_result = len(result)
    # print(lenght_result)

    for i in range(0, lenght_result):
        # print(f"{result[i][1]} : {result[i][2]}")
        if auth_login == result[i][1]:
            if pass1 == result[i][2]:
                # print(pass1)
                return True
    print("Вы ввели некорректные данные для авторизации!")