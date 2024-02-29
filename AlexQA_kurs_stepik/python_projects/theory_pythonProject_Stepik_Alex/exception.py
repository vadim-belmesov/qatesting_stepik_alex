a = int(input("Введите 1е значение"))
b = int(input("Введите 2е значение"))

try:
    result = int(a/b)
except ZeroDivisionError:
    result = 0
    print("На ноль делить нельзя")

print("Результат: "+ str(result))

#ZeroDivisionError
#ValueError: invalid literal for int() with base 10: ' d'