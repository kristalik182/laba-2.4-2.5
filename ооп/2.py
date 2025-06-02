class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Гав!"
class Cat(Animal):
    def speak(self):
        return "Мяу!"
my_dog = Dog()
my_cat = Cat()
print("Собака говорит:", my_dog.speak())
print("Кошка говорит:", my_cat.speak())
