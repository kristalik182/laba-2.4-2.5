class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Вы внесли {amount}. Новый баланс: {self.__balance}")
        else:
            print("Сумма депозита должна быть положительной.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Вы сняли {amount}. Остаток на счете: {self.__balance}")
        elif amount > self.__balance:
            print("Недостаточно средств для снятия.")
        else:
            print("Сумма снятия должна быть положительной.")
    def get_balance(self):
        return self.__balance
def main():
    account = BankAccount()
    while True:
        print("\nДоступные операции:")
        print("1. Депозит")
        print("2. Снятие")
        print("3. Проверка баланса")
        print("4. Выход")
        choice = input("Выберите операцию (1/2/3/4): ")
        if choice == '1':
            amount = float(input("Введите сумму для депозита: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        elif choice == '3':
            print("Текущий баланс:", account.get_balance())
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")
if __name__ == "__main__":
    main()
