weight_input = float(input("Введите количество килограммов: "))
new_weight_input = float(input("Введите новое количество килограммов: "))
class KgToPounds:
    def __init__(self, kg):
        self._kg = kg
    @property
    def kg(self):
        return self._kg
    @kg.setter
    def kg(self, value):
        if value < 0:
            raise ValueError("Вес не может быть отрицательным")
        self._kg = value
    def to_pounds(self):
        return self._kg * 2.20462
if __name__ == "__main__":
    try:
        weight = KgToPounds(weight_input)
        print(f"{weight.kg} кг это {weight.to_pounds()} фунтов")
        weight.kg = new_weight_input
        print(f"{weight.kg} кг это {weight.to_pounds()} фунтов")
    except ValueError as e:
        print(e)
