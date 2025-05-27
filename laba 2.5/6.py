input_array = input("Введите числа через пробел: ")
array = list(map(int, input_array.split()))
def change_sign(arr):
    return [-x for x in arr]
result_array = change_sign(array)
print("Массив с противоположными знаками:", result_array)
