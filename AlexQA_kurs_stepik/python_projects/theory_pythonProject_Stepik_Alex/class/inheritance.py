class Person():
    """создаём человека"""
    def __init__(self, name, age, height):
        #инициализация атрибутов
        self.name = name
        self.age = age
        self.height = height
        #укажем значение по умолчанию для веса
        self.weight = 100
    def description_person(self):
        #Получение описания
        description = self.name + ", ему " + str(self.age) + ", его рост: " + str(self.height) + ", его вес: " + str(self.weight)
        print("Нового человека зовут: " + description)

    def get_weight(self):
        # Получение веса
        print("Вес нашего человека: " + str(self.weight))

    def update_weight(self, kg):
        # Изменение веса
        self.weight = kg
class Warrior(Person):
    """Создаём класс-потомок воина"""
    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя с помощью super()"""
        super().__init__(name, age, height)
        #добавили атрибут классу потомку
        self.rage = 100
    def get_rage(self):
        # Получение заряда ярости для класса-потомка
        print("Заряд ярости равен: " + str(self.rage))

    def description_person(self):
        #Переопределение метода родителя
        description = self.name + ", ему " + str(self.age) + ", его заряд ярости: " + str(self.rage)
        # print("Нового человека зовут: " + description)

        #переписали с return
        return description

warrior = Warrior("Konan", 32, 200)
# warrior.update_weight(150)
print("Нового человека зовут: " + warrior.description_person())
# warrior.get_rage()