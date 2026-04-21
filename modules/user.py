
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_accounts(self):
        return self.accounts
    
    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            return True
        return False
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "accounts": [account.to_dict() for account in self.accounts]
        }

    def __str__(self):
        return f"User(name={self.name}, email={self.email}, Accounts={len(self.accounts)})"
    