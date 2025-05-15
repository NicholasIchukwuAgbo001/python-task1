import random
from account import Account

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, first_name, last_name, pin):
        if not first_name.isalpha() or not last_name.isalpha() or not str(pin).isdigit():
            raise ValueError("Invalid input")
        account_number = str(random.randint(1000000000, 9999999999))
        account = Account(account_number, first_name, last_name, pin)
        self.accounts.append(account)
        return account_number

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
            return None

    def close_account(self, account_number, pin):
        account = self.get_account(account_number)
        if account and account.pin == pin:
            self.accounts.remove(account)
        else:
            raise ValueError("Invalid PIN or account number")

    def deposit(self, account_number, pin, amount):
        account = self.get_account(account_number)
        if account and account.pin == pin:
            account.deposit_money(pin, amount)
        else:
            raise ValueError("Invalid PIN or account number")

    def withdraw(self, account_number, pin, amount):
        account = self.get_account(account_number)
        if account and account.pin == pin:
            account.withdraw_money(pin, amount)
        else:
            raise ValueError("Invalid PIN or account number")

    def get_balance(self, account_number, pin):
        account = self.get_account(account_number)
        if account and account.pin == pin:
            return account.balance
        else:
            raise ValueError("Invalid PIN or account number")

    def change_pin(self, account_number, pin, new_pin):
        account = self.get_account(account_number)
        if account and account.pin != new_pin:
            account.change_pin(pin, new_pin)
        else:
            raise ValueError("Invalid PIN or account number")

    def is_valid_pin(self, account_number, pin):
        account = self.get_account(account_number)
        if account and account.pin == pin:
            return True
        else:
            return False


    def transfer(self, account_number, receiver_account, pin, amount):
        account1 = self.get_account(account_number)
        account2 = self.get_account(receiver_account)
        if account1 and account2 and account1.pin == pin:
            account1.deposit_money(account2, pin, amount)
        else:
            raise ValueError("Invalid PIN or account number")

