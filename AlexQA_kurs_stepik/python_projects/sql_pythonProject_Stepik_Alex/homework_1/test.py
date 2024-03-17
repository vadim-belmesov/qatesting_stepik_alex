import sqlite3
from User import User

#Подключение к БД
db_registration = sqlite3.connect(r'registration.db')
print("Подключились к БД")
#Управление БД
cursor = db_registration.cursor()
# Запрашиваем весь список из БД чтобы проверить логин
# userData = ('Ivan', 'qwer1234', '1234')
# cursor.execute("""DELETE FROM users_data WHERE UserID = '2'""")
# db_registration.commit()
# db_registration.close()