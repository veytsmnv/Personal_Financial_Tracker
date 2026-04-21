from modules.user import User
from modules.checking_account import CheckingAccount
from modules.savings_account import SavingsAccount
from storage.file_manager import save_data, load_data


user = User("John", "john@email.com")

checking = CheckingAccount("001", user, 500, 100)
savings = SavingsAccount("002", user, 1000, 3)

user.add_account(checking)
user.add_account(savings)

checking.deposit(200)
checking.withdraw(100)
checking.transfer(savings, 50)
savings.add_interest()

print(user)
for account in user.get_accounts():
    print(account.display_info())
    for t in account.transactions:
        print(t)
        
# save
save_data([user])

# load
loaded_users = load_data()
for user in loaded_users:
    print(user)
    for account in user.get_accounts():
        print(account.display_info())
        for t in account.transactions:
            print(t)