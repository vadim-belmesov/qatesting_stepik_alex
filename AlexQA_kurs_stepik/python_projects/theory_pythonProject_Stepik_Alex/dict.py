# список
family_2 = ["Alex", "Olga", "Semen", "Nasty", "Alex"]
print(family_2)

# множества
family_2 = {"Alex", "Olga", "Semen", "Nasty", "Alex"}
print(family_2)

# словарь (ключ:значение)
family_3 = {"папа":"Alex", "мама":"Nastya"}
print(family_3)

#вывод конкретного значения по ключу
print(family_3["папа"])

#k - key, v - value
for k, v in family_3.items():
    print(k + " - " + v)