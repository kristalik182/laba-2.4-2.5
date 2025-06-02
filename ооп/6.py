name_input = input("Введите имя: ")
age_input = int(input("Введите возраст: "))
class Nikola:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.age = age
        if name == "Николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай"
    def __setattr__(self, key, value):
        if key not in Nikola.__slots__:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")
        object.__setattr__(self, key, value)
if __name__ == "__main__":
    person = Nikola(name_input, age_input)
    print(f"Имя: {person.name}")
    print(f"Возраст: {person.age}")
    try:
        person.отчество = "Иванович"
    except AttributeError as e:
        print(f"Ошибка: {e}")