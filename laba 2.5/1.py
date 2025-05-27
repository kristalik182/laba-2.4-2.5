def sum_between_one_and_n(N):
    return sum(range(1, N + 1))

N = int(input("Введите число N: "))
result = sum_between_one_and_n(N)
print("Сумма целых чисел от 1 до", N, "равна", result)
