import sqlite3

db = sqlite3.connect('testDB.db') #подключение к БД
print("Подключились к БД")
 #переменная для управления БД
#Создание таблицы
# cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
#     StudentsID INTEGER PRIMARY KEY AUTOINCREMENT,
#     First_name TEXT NOT NULL,
#     Last_name TEXT NOT NULL);
#     """)
# db.commit() # Сохраниение запроса

# cursor.execute("""SELECT * FROM Students""") #запрос для получения содержимого таблицы
# result = cursor.fetchall() #результат запроса

#Заполнение таблицы НЕБЕЗОПАСНЫЙ СПОСОБ
# cursor.execute("""INSERT INTO Students(First_name, Last_name)
#     VALUES('Petr', 'Petrov');""")
# db.commit()
# print(result)

#Заполнение таблицы БЕЗОПАСНЫЙ СПОСОБ
data_students = [('Petr', 'Petrov'), ('Nan', 'Nanov')]
cursor.executemany("""INSERT INTO Students(First_name, Last_name)
    VALUES(?, ?);""", data_students)
db.commit()
# print(result)

#отправка несклольких запросов
# cursor.executescript("""CREATE TABLE IF NOT EXISTS Students2(
#     StudentsID INTEGER PRIMARY KEY AUTOINCREMENT,
#     First_name TEXT NOT NULL,
#     Last_name TEXT NOT NULL);
#
#     INSERT INTO Students2(First_name, Last_name)
#     VALUES('Petr', 'Petrov');
#
# """)
# db.commit() # Сохраниение запроса

# #Изменение данных в таблице
# update_parents = ('Sokolova', 4)
# cursor.execute("""UPDATE Students SET Last_name = ? WHERE StudentsID = ?;""", update_parents)
# db.commit() # Сохраниение запроса
# print("Изменение данных в таблице")

#Удаление данных в таблице
delete_params = '3'
cursor.execute("""DELETE FROM Students WHERE StudentsID = ?;""", delete_params)
db.commit()
print("Удаление данных в таблице")

#Удаление таблицы
cursor.execute("""DROP TABLE Students2""")
db.commit()
print("Удаление таблицы")