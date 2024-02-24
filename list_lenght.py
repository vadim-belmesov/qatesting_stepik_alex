personal = ["Alex", "Ivan", "Nasty", "Olga"]
#           0       1       2        3
number = [1, 22, 34, 54]

print("list lenght")
print(len(personal))
print("---")
print("обратиться к последнему объекту personal")
print(personal[-1])
print("---")
print("список от 0 до 2 НЕ включительно")
print(personal[0:2])
print("---")
print("список от 1(не включительно) до конца списка")
print(personal[1:])
print("---")
print("Добавить в конец списка объект (Fedor)")
personal.append("Fedor")
print(personal)
print("---")
print("Добавить оба списка в новый список pn")
pn = []
pn.append(personal)
pn.append(number)
print(pn)