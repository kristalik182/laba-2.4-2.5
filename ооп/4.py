user_input = input("Введите добавку к газировке (или оставьте пустым для обычной газировки): ")
class Soda:
    def __init__(self, additive=None):
        self.additive = additive
    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")
if __name__ == "__main__":
    drink = Soda(user_input.strip())
    drink.show_my_drink()
