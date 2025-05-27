input_numbers = input("Введите целые числа, разделенные пробелами: ")
array = list(map(int, input_numbers.split()))

def analyze_numbers(numbers):
    positive_sum = sum(num for num in numbers if num > 0)
    min_value = min(numbers)
    max_value = max(numbers)
    min_index = numbers.index(min_value)
    max_index = numbers.index(max_value)
    start_index = min(min_index, max_index)
    end_index = max(min_index, max_index)
    product = 1
    for num in numbers[start_index + 1:end_index]:
        product *= num
    return positive_sum, product

result = analyze_numbers(array)
print("Сумма положительных элементов:", result[0])
print("Произведение чисел между минимальным и максимальным элементами:", result[1])
