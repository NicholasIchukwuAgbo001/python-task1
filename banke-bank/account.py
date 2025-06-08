class Account:
    def __init__(self, account_number, first_name, last_name, pin):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.pin = pin
        self.balance = 0.0
        self.is_closed = False

    def deposit_money(self, pin, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if self.pin == pin and not self.is_closed:
            self.balance += amount
        elif self.pin != pin:
            raise ValueError("Invalid PIN")
        else:
            raise ValueError("Account closed")

    def withdraw_money(self, pin, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if self.pin == pin and not self.is_closed:
            if amount > self.balance:
                raise ValueError("Insufficient balance")
            self.balance -= amount
        elif self.pin != pin:
            raise ValueError("Invalid PIN")
        else:
            raise ValueError("Account closed")

    def transfer_money(self, account2, amount, pin):
        if self.pin == pin and not self.is_closed and self.balance >= amount:
            self.withdraw_money(pin, amount)
            account2.deposit_money(account2.pin, amount)
        elif self.pin != pin:
            raise ValueError("Invalid PIN")
        elif self.is_closed:
            raise ValueError("Account closed")
        elif self.balance < amount:
            raise ValueError("Insufficient balance")

    def change_pin(self, oldPin, newPin):
        if self.pin == oldPin and not self.is_closed:
            self.pin = newPin
        else:
            raise ValueError("Invalid PIN")

    def close_account(self):
        self.is_closed = True