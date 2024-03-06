import sqlite3

#подключение к БД
db = sqlite3.connect(r'registration.db')
cursor = db.cursor()
class User():
    def __init__(self, login, password, code):
        self.login = login
        self.password = password
        self.code = code

    def add_db(self, login, password, code):
        self.login = login
        self.password = password
        self.code = code
#        self.db_name = db_name
        user_data = (login, password, code)
        cursor.execute("""INSERT INTO users_data(Login, Password, Code)
    VALUES(?, ?, ?);""", user_data)

