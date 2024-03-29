import sqlite3
#подключение к БД Win
"""1. Создать базу данных registration.db"""
db = sqlite3.connect(r'registration.db')
print("Подключились к БД")
#переменная для управления БД
cursor = db.cursor()

"""2. Создать таблицу users_data с колонками 
UserID, Login (TEXT), Password (TEXT), Code (INTEGER)"""
# Создание таблицы users_data
cursor.execute("""CREATE TABLE IF NOT EXISTS users_data(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Login TEXT NOT NULL,
    Password TEXT NOT NULL,
    Code INTEGER);
""")
# Сохраниение запроса
db.commit()
# Закрываем соединение
db.close()

"""3. Добавить пользователя с данными Ivan, qwer1234, 1234"""
userData = ('Ivan', 'qwer1234', '1234')
cursor.executemany("""INSERT INTO users_data(Login, Password, Code)
    VALUES(?, ?);""", userData)
db.commit()
db.close()