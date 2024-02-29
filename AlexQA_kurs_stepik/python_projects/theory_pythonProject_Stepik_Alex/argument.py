def description_user(name, age, gender):
    print(f"Имя пользователся: {name}, возраст: {age}, пол: {gender}")

n = "Vas"
a = 12
g = "M"


#позиционный аргумент
description_user("Ann", 30, "W")
#именованный аргумент
description_user(name="Max", age=15, gender="M")
#заранее определённые переменные
description_user(n,a,g)
