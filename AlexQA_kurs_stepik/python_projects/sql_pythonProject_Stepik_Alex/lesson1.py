import sqlite3

"""Подключение к БД"""

#подключение к БД в Linux
# db = sqlite3.connect(r'/home/balu/PycharmProjects/pythonLessonsAlex/AlexQA_kurs_stepik/DB/qa_testing')

# #подключение к БД Win
db = sqlite3.connect(r'testDB.db')
print("Подключились к БД")
#переменная для управления БД
cursor = db.cursor()

#запрос для получения содержимого таблицы
cursor.execute("""SELECT * FROM Students""")
# result = cursor.fetchall() #результат запроса

#Одно значение
result_one = cursor.fetchone()
#Несколько значение
result_many = cursor.fetchmany(2)
#Все значения
result_all = cursor.fetchall()
#
# print(result_one)
# print(result_many)
print(result_all)
print(result_all[1][1])