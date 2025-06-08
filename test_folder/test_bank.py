
import unittest

from bank.bank import Bank


class BankTest(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_create_account1(self):
        account_number = self.bank.create_account("Nichols", "Ichukwu", 1234)
        self.assertIsNotNone(account_number)

    def test_create_account2(self):
        account_number = self.bank.create_account("adah", "john", 1122)
        self.assertIsNotNone(account_number)

    # def test_close_account(self):
    #     account_number = self.bank.create_account("Nichols", "Ichukwu", 1234)
    #     self.bank.close_account(account_number, 1234)
    #     with self.assertRaises(ValueError):
    #         self.bank.get_balance(account_number, 1234)

    def test_deposit(self):
        account_number = self.bank.create_account("idowu", "moses", 1122)
        self.bank.deposit(account_number, 1122, 2000)
        self.assertEqual(self.bank.get_balance(account_number, 1122), 2000)

    def test_deposit_with_wrong_pin(self):
        account_number = self.bank.create_account("idowu", "moses", 1122)
        with self.assertRaises(ValueError):
            self.bank.deposit(account_number, 1111, 1000)

    def test_withdraw(self):
        account_number = self.bank.create_account("idowu", "moses", 1122)
        self.bank.deposit(account_number, 1122, 2000)
        self.bank.withdraw(account_number, 1122, 500)
        self.assertEqual(self.bank.get_balance(account_number, 1122), 1500)

    def test_withdraw_wrong_pin(self):
        account_number = self.bank.create_account("idowu", "moses", 1122)
        self.bank.deposit(account_number, 1122, 2000)
        with self.assertRaises(ValueError):
            self.bank.withdraw(account_number, 1111, 500)

    def test_change_pin(self):
        account_number = self.bank.create_account("adah", "john", 1122)
        account = self.bank.get_account(account_number)
        account.change_pin(1122, 1111)
        self.assertEqual(account.pin, 1111)

    def test_transfer(self):
        account_number1 = self.bank.create_account("adah", "john", 1122)
        account_number2 = self.bank.create_account("idowu", "moses", 1111)
        self.bank.deposit(account_number1, 1122, 2000)
        self.bank.transfer(account_number1, account_number2,1122, 1000)
        self.assertEqual(self.bank.get_balance(account_number1, 1122), 2000)


if __name__ == '__main__':
    unittest.main()
