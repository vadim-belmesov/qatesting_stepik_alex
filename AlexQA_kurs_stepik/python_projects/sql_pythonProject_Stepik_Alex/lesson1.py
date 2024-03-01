import sqlite3

"""Подключение к БД"""

db = sqlite3.connect(r'/home/balu/PycharmProjects/pythonLessonsAlex/AlexQA_kurs_stepik/DB/qa_testing') #подключение к БД
print("Подключились к БД")
cursor = db.cursor() #переменная для управления БД

cursor.execute("""SELECT * FROM Students""") #запрос для получения содержимого таблицы
result = cursor.fetchall() #результат запроса
print(result)
print(type(result))