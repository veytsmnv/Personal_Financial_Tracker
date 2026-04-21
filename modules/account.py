from abc import ABC, abstractmethod
from transaction import Transaction
class Account(ABC):
    def __init__(self, account_id, owner, balance):
        self.account_id = account_id
        self.owner = owner
        self.__balance = balance
        self.transactions = []

    @abstractmethod
    def display_info(self):
        return f"Account ID: {self.account_id}, Owner: {self.owner.name}, Balance: {self.balance}"

    @abstractmethod
    def add_interest(self):
        pass

    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(self.account_id, None, amount))
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(None, self.account_id, amount))
            return True
        return False
    
    