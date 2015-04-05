class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.account_history = ["Account was created"]

    def __str__(self):
        message = "Bank account for {} with balance of {}{}"
        return message.format(self.name, self.balance, self.currency)

    def __int__(self):
        int_check = "__int__ check -> {}{}".format(self.balance, self.currency)
        self.account_history.append(int_check)
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount of money")

        self.balance += amount
        current_deposit = "Deposited {}{}".format(amount, self.currency)
        self.account_history.append(current_deposit)

    def get_balance(self):
        balance_check = "Balance check -> {}{}".format(
            self.balance, self.currency)
        self.account_history.append(balance_check)
        return self.balance

    def transfer_to(self, account, amount):
        if self.currency != account.currency or self.balance < amount:
            return False

        self.balance -= amount
        transfer_to_person = "Transfer to {} for {}{}".format(
            account.name, amount, account.currency)
        self.account_history.append(transfer_to_person)

        account.balance += amount
        transfer_from_person = "Transfer from {} for {}{}". format(
            self.name, amount, account.currency)
        account.account_history.append(transfer_from_person)
        return True

    def withdraw(self, amount):
        if amount < 0 or self.balance < amount:
            withdraw_failed = "Withdraw for {}{} failed".format(
                amount, self.currency)
            self.account_history.append(withdraw_failed)
            return False

        self.balance -= amount
        withdrawn_money = "{}{} was withdrawn".format(amount, self.currency)
        self.account_history.append(withdrawn_money)
        return True

    def history(self):
        return self.account_history
