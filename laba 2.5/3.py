import random

size = int(input("Введите размер массива: "))
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

def generate_even_numbers(size, start, end):
    even_numbers = set()
    while len(even_numbers) < size:
        num = random.randint(start, end)
        if num % 2 == 0:
            even_numbers.add(num)
    return sorted(even_numbers)

if start > end:
    print("Ошибка: начало диапазона должно быть меньше конца диапазона.")
else:
    even_array = generate_even_numbers(size, start, end)
    print("Возрастущий массив из случайных четных чисел:", even_array)
