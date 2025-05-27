a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
def calculate_expression(a, b):
    result = (a + 4 * b) * (a - 3 * b) + a ** 2
    return result
value = calculate_expression(a, b)
print("Результат выражения:", value)
