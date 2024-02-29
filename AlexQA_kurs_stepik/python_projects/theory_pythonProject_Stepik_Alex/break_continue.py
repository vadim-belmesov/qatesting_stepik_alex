list = [1,4,6,10,12]
for i in list:
    if i == 10:
        print(f"i равно {i}")
        break
    elif i == 4:
        print(f"Ура i равно {i}")
    elif i == 6:
        print(f"Ура i равно {i}")
        continue
    print(i)