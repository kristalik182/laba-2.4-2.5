x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
radius = float(input("Введите радиус круга: "))
def is_point_in_circle(x, y, radius):
    return x**2 + y**2 <= radius**2
if is_point_in_circle(x, y, radius):
    print("Точка принадлежит кругу.")
else:
    print("Точка не принадлежит кругу.")
