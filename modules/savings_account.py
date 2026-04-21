from modules.account import Account
from modules.transaction import Transaction
class SavingsAccount(Account):
    def __init__(self, account_id, owner, balance, interest_rate):
        super().__init__(account_id, owner, balance)
        self.interest_rate = interest_rate

    def display_info(self):
        return f"Savings Account - {super().display_info()}, Interest Rate: {self.interest_rate}%"

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(None, self.account_id, amount))
            return True
        return False
    def transfer(self, recipient_account, amount):
        if self.withdraw(amount):
            recipient_account.deposit(amount)
            self.transactions.append(Transaction(self.account_id, recipient_account.account_id, amount))
            return True
        return False
    def to_dict(self):
        return {
            "type": "savings",
            "account_id": self.account_id,
            "owner": self.owner.name,
            "balance": self.balance,
            "interest_rate": self.interest_rate
        }
