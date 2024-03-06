"""Функция проверки логина"""
def login_check(new_login, db):
    cursor = db.cursor()
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

"""Функция проверки кода"""
def code_check(code):
    if code.isdigit() == True:
        print("digit")
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
        print("Pass OK")
        return False