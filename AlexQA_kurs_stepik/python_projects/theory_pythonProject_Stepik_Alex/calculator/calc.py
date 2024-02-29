first_number = " "
second_number = " "
sign = "a"

while not (first_number.isdigit()):
    first_number = input("Введите первое число: ")
    if not (first_number.isdigit()):
        print("Введите, пожалуйста число!")

while sign not in "+-*/":
    sign = input("Введите арифметический знак: ")
    if sign not in "+-*/":
        print("Вы ввели не арифметический знак!")

while not (second_number.isdigit()):
    second_number = input("Введите второе число: ")
    if not (second_number.isdigit()):
        print("Введите, пожалуйста число!")

if sign == "+":
    sum_of_num = int(first_number) + int(second_number)
    print(f"Сумма чисел {first_number} + {second_number} = {sum_of_num}")
elif sign == "-":
    difference_of_num = int(first_number) - int(second_number)
    print(f"Разница чисел {first_number} - {second_number} = {difference_of_num}")
elif sign == "*":
    product_of_num = int(first_number) * int(second_number)
    print(f"Произведение чисел {first_number} * {second_number} = {product_of_num}")
elif sign == "/":
    try:
        division_of_num = int(first_number) / int(second_number)
        print(f"Деление {first_number} / {second_number} = {division_of_num}")
    except ZeroDivisionError:
        division_of_num = 0
        print("На ноль делить нельзя!")