import re
from bank import Bank
def main():
    print("Welcome to BANKE BANK")
    bank = Bank()
    while True:
        print("""
        1. Create account
        2. Close account1
        3. Deposit money
        4. Withdraw money
        5. Check balance
        6. Change PIN
        7. transfer money
        8. Exist....
        """)

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                try:
                    first_name = input("\nEnter your first name: ")
                    validate_name(first_name)
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    last_name = input("\nEnter your last name: ")
                    validate_name(last_name)
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    pin = int(input("\nEnter your PIN: "))
                    validate_pin(pin)
                    confirm_pin = int(input("\nConfirm your PIN: "))
                    if confirm_pin != pin:
                        print("\nPIN do not match. Please try again.")
                    else:
                        break
                except ValueError as e:
                    print(e)

            try:
                account_number = bank.create_account(first_name, last_name, pin)
                print("\nWELCOME TO BANKE BANK ")
                print("\nAccount created successfully. " + first_name + " " + last_name)
                print("Your account number is: " + account_number)
                print("Save your account number for future transactions/use.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            while True:
                try:
                    account_number = input("\nEnter your account number: ")
                    validate_account_number(account_number)
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    pin = int(input("\nEnter your PIN: "))
                    validate_pin(pin)
                    confirm_pin = int(input("\nConfirm your PIN: "))
                    if confirm_pin != pin:
                        print("\nPIN do not match. Please try again.")
                    else:
                        break
                except ValueError as e:
                    print(e)

            try:
                    bank.close_account(account_number, pin)
                    print("Account closed successfully.")
            except ValueError as e:
                    print(e)

        elif choice == "3":
            while True:
                try:
                    account_number = input("\nEnter your account number: ")
                    validate_account_number(account_number)
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    amount = float(input("\nEnter your amount: "))
                    validate_amount(amount)
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    pin = int(input("\nEnter your PIN: "))
                    validate_pin(pin)
                    confirm_pin = int(input("\nConfirm your PIN: "))
                    if confirm_pin != pin:
                        print("\nPIN do not match. Please try again.")
                    else:
                        break
                except ValueError as e:
                    print(e)

            try:
                bank.deposit(account_number, pin, amount)
                print("\nDeposited of ₦", amount, "was successfully.")
            except ValueError as e:
                print(e)

        elif choice == "4":
            while True:
                try:
                    account_number = input("\nEnter your account number: ")
                    validate_account_number(account_number)
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    amount = float(input("\nEnter your amount: "))
                    validate_amount(amount)
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    pin = int(input("\nEnter your PIN: "))
                    validate_pin(pin)
                    confirm_pin = int(input("\nConfirm your PIN: "))
                    if confirm_pin != pin:
                        print("\nPIN do not match. Please try again.")
                    else:
                        break
                except ValueError as e:
                    print(e)

            try:
                bank.withdraw(account_number, pin, amount)
                print("\nWithdraw of ₦", amount, "was successfully.")
            except ValueError as e:
                print(e)

        elif choice == "5":
            while True:
                try:
                    account_number = input("\nEnter your account number: ")
                    validate_account_number(account_number)
                    break
                except ValueError as e:
                    print(e)


            while True:
                try:
                    pin = int(input("\nEnter your PIN: "))
                    validate_pin(pin)
                    confirm_pin = int(input("\nConfirm your PIN: "))
                    if confirm_pin != pin:
                        print("\nPIN do not match. Please try again.")
                    else:
                        break
                except ValueError as e:
                    print(e)

            try:
                balance = bank.get_balance(account_number, pin)
                print("Your balance is", balance)
            except ValueError as e:
                print(e)

        elif choice == "6":
            while True:
                try:
                    account_number = input("\nEnter your account number: ")
                    validate_account_number(account_number)
                    break
                except ValueError as e:
                    print(e)


            while True:
                try:
                    pin = int(input("\nEnter your Old PIN: "))
                    validate_pin(pin)
                    break
                except ValueError as e:
                    print(e)


            while True:
                try:
                    new_pin = int(input("\nEnter your New PIN: "))
                    validate_pin(new_pin)
                    break
                except ValueError as e:
                    print(e)

            try:
                bank.change_pin(account_number, pin, new_pin)
                print("PIN changed successfully.")
            except ValueError as e:
                print(e)

        elif choice == "7":
            while True:
                try:
                    account_number = input("\nEnter your account number: ")
                    validate_account_number(account_number)
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    account_number_receiver = input("\nEnter receiver account number: ")
                    validate_account_number(account_number_receiver)
                    break
                except ValueError as e:
                    print(e)


            while True:
                try:
                    amount = float(input("\nEnter your amount: "))
                    validate_amount(amount)
                    break
                except ValueError as e:
                    print(e)


            while True:
                try:
                    pin = int(input("\nEnter your PIN: "))
                    validate_pin(pin)
                    confirm_pin = int(input("\nConfirm your PIN: "))
                    if confirm_pin != pin:
                        print("\nPIN do not match. Please try again.")
                    else:
                        break
                except ValueError as e:
                    print(e)

            try:
                balance = bank.transfer(account_number, account_number_receiver, pin, amount)
                print("Transfer succeeded.")
                print("Your new balance is", balance)
            except ValueError as e:
                print(e)

        elif choice == "8":
            print("Thank you for using Banke Bank. Goodbye.")
            return

        else:
            print("Invalid choice. Please try again.")





def validate_name(name):
    if not re.match("^[a-zA-Z\\s]+$", name):
        raise ValueError("Invalid name, Name must contain only letters.")

def validate_pin(pin):
    if len(str(pin)) != 4 or not str(pin).isdigit():
        raise ValueError("Invalid PIN. PIN must be a 4-digit number")

def validate_account_number(account_number):
    if not account_number.isdigit():
        raise ValueError("Invalid account number")

def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Invalid amount")




if __name__ == '__main__':
    main()