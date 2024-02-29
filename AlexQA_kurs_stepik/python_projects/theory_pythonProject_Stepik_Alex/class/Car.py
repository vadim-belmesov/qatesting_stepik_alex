class Car():
    """класс Car и инициализация его атрибутов"""
    def __init__(self, model, start_year, engine_volume, price, mileage):
        self.model = model
        self.start_year = start_year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.wheels_number = 4
    def description_car(self):
        description = "Модель: "+ str(self.model) + ", год выпуска: " + str(self.start_year) + ", объём двигателя(л): " + str(self.engine_volume) + ", цена(руб): " + str(self.price) + ", пробег(км): " + str(self.mileage) + ", количество колёс: " + str(self.wheels_number)
        print(f"Новый авто: {description}")

class Truck(Car):
    """класс наследник Truck, с полным наследованием атрибутов, кроме количества колёс(wheels_number)"""
    def __init__(self,model, start_year, engine_volume, price, mileage):
        super().__init__(model, start_year, engine_volume, price, mileage)
        self.wheels_number = 8

