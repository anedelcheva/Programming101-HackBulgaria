import unittest
from bankaccount import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.my_account = BankAccount("Aneta", 2000, "levs")

    def test_init(self):
        self.assertTrue(isinstance(self.my_account, BankAccount))
        self.assertEqual(self.my_account.name, "Aneta")
        self.assertEqual(self.my_account.balance, 2000)
        self.assertEqual(self.my_account.currency, "levs")

    def test_str(self):
        needed_result = "Bank account for Aneta with balance of 2000levs"
        self.assertEqual(str(self.my_account), needed_result)

    '''def test_current_balance(self):
        pass'''

    def test_deposit_money(self):
        self.my_account.deposit(50)
        self.assertEqual(self.my_account.balance, 2050)
        with self.assertRaises(ValueError):
            self.my_account.deposit(-20)

        self.assertEqual(self.my_account.balance, 2050)

    def test_transfer_to_different_currency(self):
        your_account = BankAccount("Rado", 10, "$")

        self.assertFalse(self.my_account.transfer_to(your_account, 200))
        self.assertEqual(self.my_account.balance, 2000)
        self.assertEqual(your_account.balance, 10)

    def test_transfer_to_more_money_than_we_have(self):
        your_account = BankAccount("Rado", 10, "levs")

        self.assertFalse(your_account.transfer_to(self.my_account, 300))
        self.assertEqual(self.my_account.balance, 2000)
        self.assertEqual(your_account.balance, 10)

    def test_transfer_to(self):
        your_account = BankAccount("Rado", 10, "levs")
        result = self.my_account.transfer_to(your_account, 300)
        self.assertEqual(your_account.balance, 310)
        self.assertEqual(self.my_account.balance, 2000 - 300)

    def test_balance(self):
        self.assertEqual(
            self.my_account.balance, self.my_account.get_balance())

    def test_withdraw(self):
        self.my_account.withdraw(50)
        self.assertEqual(self.my_account.balance, 1950)
        self.assertFalse(self.my_account.withdraw(3000))
        self.assertFalse(self.my_account.withdraw(-10))

    def test_history(self):
        self.rado = BankAccount("Rado", 1000, "BGN")
        self.ivo = BankAccount("Ivo", 0, "BGN")
        self.rado.transfer_to(self.ivo, 500)
        self.rado.get_balance()
        self.ivo.get_balance()
        rado_history = [
            'Account was created', 'Transfer to Ivo for 500BGN', 'Balance check -> 500BGN']
        self.assertEqual(self.rado.history(), rado_history)
        ivo_history = ['Account was created',
                       'Transfer from Rado for 500BGN', 'Balance check -> 500BGN']
        self.assertEqual(self.ivo.history(), ivo_history)


if __name__ == '__main__':
    unittest.main()
