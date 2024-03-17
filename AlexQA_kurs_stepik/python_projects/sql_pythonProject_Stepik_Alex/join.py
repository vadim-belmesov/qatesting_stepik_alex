import sqlite3

db = sqlite3.connect('testDB.db') #подключение к БД
print("Подключились к БД")
cursor = db.cursor()

# cursor.execute("DROP TABLE Persons")

# cursor.executescript("""CREATE TABLE IF NOT EXISTS Persons
#     (PersonID INTEGER PRIMARY KEY AUTOINCREMENT,
#     First_name TEXT NOT NULL,
#     Position TEXT NOT NULL);
#
#     INSERT INTO Persons (First_name, Position)
#     VALUES ('ALEX','QA')
#     """)

person_data = [('PavelA','Developer'),('IvanA', 'PM')]
cursor.executemany("""UPDATE Persons SET First_name = ? Position = ? WHERE PersonID = 1, 2;""", person_data)

# cursor.execute("""SELECT * FROM Persons""")
# print(cursor.fetchall())

db.commit() # Сохраниение запроса
db.close()