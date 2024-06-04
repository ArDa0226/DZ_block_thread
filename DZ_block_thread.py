
import threading

class BankAccount:

    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

account = BankAccount()

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)
        print(f'Deposited 100, new balance is {account.balance}')


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)
        print(f'Withdraw 150, new balance is {account.balance}')

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()


deposit_thread.join()
withdraw_thread.join()
