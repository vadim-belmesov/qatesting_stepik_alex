var1 = 10 #Глобальная переменная
var2 = 20 #Глобальная переменная

print("Вывод для глобальных переменных")
print(var1, var2)
def sum_func():
    var1 = 111 #Локальная
    var2 = 222 #Локальная
    result = var1 + var2
    print(result)

def substruct_func():
    var1 = 111 #Локальная
    var2 = 222 #Локальная
    result = var1 - var2
    print(result)

print("Вывод локальных переменных функции")
sum_func()
substruct_func()