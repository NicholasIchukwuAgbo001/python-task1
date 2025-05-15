import unittest

from account import Account

class TestAtmMachineApp(unittest.TestCase):
    def setUp(self):
        self.account1 = Account("7058705863","Nicholas", "Ichukwu", 1010)
        self.account2 = Account("7058705866","Moses", "Idowu", 2020)

    def test_account1_is_created(self):
        self.assertIsNotNone(self.account1)

    def test_account2_is_created(self):
        self.assertIsNotNone(self.account2)

    def test_deposit(self):
        self.account1.deposit_money(1010, 10000)
        self.assertEqual(10000, self.account1.balance)

    def test_deposit_less_than_1(self):
        with self.assertRaises(ValueError):
            self.account1.deposit_money(1010, 0)

    def test_withdraw(self):
        self.account1.deposit_money(1010, 10000)
        self.account1.withdraw_money(1010, 5000)
        self.assertEqual(5000, self.account1.balance)

    def test_withdraw_using_wrong_pin(self):
        self.account1.deposit_money(1010, 10000)
        with self.assertRaises(ValueError):
            self.account1.withdraw_money(1011, 10000)

    def test_transfer(self):
        self.account1.deposit_money(1010, 10000)
        self.account1.transfer_money(self.account2, 5000, 1010)
        self.assertEqual(5000, self.account1.balance)
        self.assertEqual(5000, self.account2.balance)



if __name__ == '__main__':
    unittest.main()

