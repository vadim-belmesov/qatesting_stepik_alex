from BasePerson import Person

man = Person("Алекс", 30, 180)
# man.description_person()
#здесь мы присваиваем напрямую, но лучше это делать через метод
man.weight = 95
#обновляем вес через метод
man.update_weight(98)
man.get_weight()