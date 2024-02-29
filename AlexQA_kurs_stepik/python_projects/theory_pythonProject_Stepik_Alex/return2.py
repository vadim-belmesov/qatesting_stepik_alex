# def identification(name):
#     print("Вы являетесь")
#
#     if(name == "Alex"):
#         print("Автором")
#     else:
#         print("Студентом")
#
# name = input("Введите ваше имя: ")
# identification(name)

# Переписываем функцию с RETURN
def identification(name):
    print("Вы являетесь")
    if(name == "Alex"):
        result = "Автором"
    else:
        result = "Студентом"
    return result

name = input("Введите ваше имя: ")
# print(identification(name))

# Функцию присваиваем переменной
# n = "Alex"
# s = identification(n)
# print(n + s)

# Пишем функцию для печати переменной result из функции identification
def status(res):
    print(res)
status(identification(name))