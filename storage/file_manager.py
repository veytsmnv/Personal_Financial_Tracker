import json

from modules.transaction import Transaction
from modules.user import User
from modules.checking_account import CheckingAccount
from modules.savings_account import SavingsAccount

FILE_PATH = 'data.json'

def save_data(data: list[User]):
    data_dicts = [user.to_dict() for user in data]
    with open(FILE_PATH, 'w') as file:
        json.dump(data_dicts, file, indent=4)
def load_data():
    try:
        with open(FILE_PATH, 'r') as file:
            data_dicts = json.load(file)
            users = []
            for user_dict in data_dicts:
                user = User(user_dict['name'], user_dict['email'])
                for account_dict in user_dict.get('accounts', []):
                    if account_dict['type'] == 'checking':
                        account = CheckingAccount(
                            account_dict['account_id'],
                            user,
                            account_dict['balance'],
                            account_dict['overdraft_limit']
                        )
                    elif account_dict['type'] == 'savings':
                        account = SavingsAccount(
                            account_dict['account_id'],
                            user,
                            account_dict['balance'],
                            account_dict['interest_rate']
                        )
                    else:
                        continue
                    user.add_account(account)
                    for t in account_dict.get('transactions', []):
                        account.transactions.append(Transaction(t['sender'], t['recipient'], t['amount']))
                users.append(user)
            return users
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []