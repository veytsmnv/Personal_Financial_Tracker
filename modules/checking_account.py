from account import Account
from transaction import Transaction
class CheckingAccount(Account):
    def __init__(self, account_id, owner, balance, overdraft_limit):
        super().__init__(account_id, owner, balance)
        self.overdraft_limit = overdraft_limit

    def display_info(self):
        return f"Checking Account - {super().display_info()}, Overdraft Limit: {self.overdraft_limit}"

    def add_interest(self):
        pass  

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
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