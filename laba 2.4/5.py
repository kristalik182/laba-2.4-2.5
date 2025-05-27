def read_integer():
    while True:
        try:
            num = int(input("Введите целое число: "))
            return num
        except ValueError:
            print("Ошибка: Это не целое число. Попробуйте снова.")
def divide_numbers():
    while True:
        try:
            print("Введите два числа для деления:")
            a = read_integer()
            b = read_integer()
            result = a / b
            print(f"Результат деления: {result}")
            break
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль! Попробуйте снова.")
def main():
    try:
        divide_numbers()
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
if __name__ == "__main__":
    main()
