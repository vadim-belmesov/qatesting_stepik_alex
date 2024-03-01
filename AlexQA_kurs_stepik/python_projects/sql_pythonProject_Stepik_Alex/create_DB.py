import sqlite3

db = sqlite3.connect('testDB.db') #подключение к БД
print("Подключились к БД")
cursor = db.cursor() #переменная для управления БД
#Создание таблицы
cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
    StudentsID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL);
    """)

db.commit() # Сохраниение запроса

cursor.execute("""SELECT * FROM Students""") #запрос для получения содержимого таблицы
result = cursor.fetchall() #результат запроса
#print(result)

# #Заполнение таблицы НЕБЕЗОПАСНЫЙ СПОСОБ
# cursor.execute("""INSERT INTO Students(First_name, Last_name)
#     VALUES('Petr', 'Petrov');""")
# db.commit()
# print(result)

#Заполнение таблицы БЕЗОПАСНЫЙ СПОСОБ
data_students = [('Petr', 'Petrov'), ('Nan', 'Nanov')]
cursor.executemany("""INSERT INTO Students(First_name, Last_name)
    VALUES(?, ?);""", data_students)
db.commit()
print(result)