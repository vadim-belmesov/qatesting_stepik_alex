str_1 = "upper() - все символы в верхний регистр"
print(str_1.upper())

str_1 = "title() - добавить заглавную букву к слову"
print(str_1.title())

str_1 = "lower() - ВСЕ БУКВЫ маленькими"
print(str_1.lower())

str_1 = "capitalize() - ВСЕ БУКВЫ маленькими"
print(str_1.capitalize())

print("В переменную А будет добавлено значение из NAME")
name = "Ivan"
a = "Hello {}"
result = a.format(name)
print(result)

print("### Ещё использование FORMAT ###")
first_name = "Ivan"
last_name = "Ivanov"
a = "{} {}"
result = a.format(first_name, last_name)
print("Меня зовут: " + result)

print("### Ещё одна вариация  ###")
result = f'{first_name} {last_name}'
print(result)