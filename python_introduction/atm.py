# accounts = [
#     {'account_id': 100, 'name': 'lirone', 'pin': '1234', 'balance': 500},
#     {'account_id': 101, 'name': 'Bob', 'pin': '5678', 'balance': 900}
# ]
# ADMIN_USERNAME = "admin"
# ADMIN_PASSWORD = "123456"

# def find_account(account_id):
#     for account in accounts:
#         if account['account_id'] == account_id:
#             return account
#     return None

# user_pin_input = input("Enter your account pin ")
# def verify_pin(account_id, user_pin_input):
#     is_pin_correct = account ["pin"] == user_pin_input
#     return is_pin_correct

# def deposit():
#     account_id = int(input("Enter your account ID: "))
#     account = find_account(account_id)
#     if account:
#         amount = float(input("Enter deposit amount: "))
#         account['balance'] += amount
#         print(f"Deposit successful. New balance: {account['balance']}")
#     else:
#         print("Account not found.")


# def withdraw():
#     pass

# def check_balance():
#     pass

# def show_all_accounts():
#     pass

# def admin_login():
#     username = input("Enter admin username: ")
#     password = input("Enter admin password: ")
    
#     if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
#         return True
#     else:
#         print("Invalid admin credentials")
#         return False
    
# is_admin_in = admin_login()

# print(f"Admin login successful: {is_admin_in}")
accounts = [{
    "account_id": 1001,
    "username": "Yuval",
    "balance": 55000,
    "pin": 3571
},
{
    "account_id": 1002,
    "username": "Mike",
    "balance": 100000,
    "pin": 1234
}]

def auth():
    id = int(input("Enter your account id"))
    pin = int(input("enter your PIN: "))
    
    # Find matching account from id
    for user in accounts:
        if id == user["account_id"] and user["pin"] == pin:
            print(f"Welcome {user["username"]}")
            return user # exists => positive => True => 1
        
    return None # non-exisits => negative => False => 0

def withdraw():
    user_account = auth()
    if user_account:
        amount = float(input("Please type the amount you would like to withdraw: "))
        if amount > user_account["balance"]:
            print("You are poor")
        else:
            user_account["balance"] -= amount
            balance(user_account["balance"])
    else:
        print("Wrong PIN, goodbye")
        exit()

def deposite():
    user_account = auth()
    if user_account:
        amount = float(input("Please type the amount you would like to deposite: "))
        if amount < 0:
            print("You cannot tpye negative numbers")
            exit()
        else:
            user_account["balance"] += amount
            balance(user_account["balance"])
    else:
        print("Wrong PIN, goodbye")
        exit()

def balance(user_balance):
    print(f"Your Balance now is {user_balance}")


while True:
    print("======= Welcome to Python ATM =======")    
    user_choise = int(input("""
        Choose one: 
        1. withdraw Money
        2. Deposite Money
        3. Balance
        0. to exit
    """))
    
    # print(f"User Choosed {user_choise}")
    
    match user_choise:
        case 1:
            withdraw()
        case 2:
            deposite()
        case 3:
            balance()
        case 0:
            print("Ok, Exiting...")
            exit()
    1
    