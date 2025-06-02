class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
my_car = Car("Toyota", "Camry", 2020)
print("Марка:", my_car.brand)
print("Модель:", my_car.model)
print("Год выпуска:", my_car.year)
