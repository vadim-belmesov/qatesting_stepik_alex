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
        description = self.name + " " + str(self.age) + " " + str(self.height) + " " + str(self.weight)
        print("Нового человека зовут: " + description)

    def get_weight(self):
        # Получение веса
        print("Вес нашего человека: " + str(self.weight))

    def update_weight(self, kg):
        # Изменение веса
        self.weight = kg

man = Person("Алекс", 30, 180)
# man.description_person()

#здесь мы присваиваем напрямую, но лучше это делать через метод
man.weight = 95

#обновляем вес через метод
man.update_weight(98)
man.get_weight()