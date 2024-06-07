
from time import sleep
import threading


class BankAccount:

    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"ѕополнение на {amount} руб., баланс на данный момент {account.balance} руб.")
            sleep(1)

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"—писание на {amount} руб., баланс на данный момент {account.balance} руб.")
                sleep(1)


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount(1000)

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))
deposit_thread.start()
withdraw_thread.start()
deposit_thread.join()
withdraw_thread.join()
