import getpass

# Bank database (in-memory dictionary)
bank_data = {}

# Register a new account
def register_account():
    username = input("Enter Username: ")
    if username in bank_data:
        print("Username already exists! Try a different one.")
        return
    password = getpass.getpass("Enter Password: ")
    name = input("Enter Full Name: ")
    balance = float(input("Enter Initial Deposit: "))
    bank_data[username] = {
        "name": name, 
        "password": password, 
        "balance": balance, 
        "transactions": []
    }
    print("Account created successfully!")

# Login authentication
def login():
    username = input("Enter Username: ")
    if username not in bank_data:
        print("User does not exist!")
        return None
    password = getpass.getpass("Enter Password: ")
    if bank_data[username]["password"] != password:
        print("Incorrect password!")
        return None
    print(f"Welcome, {bank_data[username]['name']}!")
    return username

# Deposit money
def deposit(username):
    amount = float(input("Enter Amount to Deposit: "))
    bank_data[username]["balance"] += amount
    bank_data[username]["transactions"].append(f"Deposited: {amount}")
    print(f"Amount {amount} deposited successfully!")

# Withdraw money
def withdraw(username):
    amount = float(input("Enter Amount to Withdraw: "))
    if amount > bank_data[username]["balance"]:
        print("Insufficient balance!")
        return
    bank_data[username]["balance"] -= amount
    bank_data[username]["transactions"].append(f"Withdrawn: {amount}")
    print(f"Amount {amount} withdrawn successfully!")

# Check account balance
def check_balance(username):
    print(f"Account Balance: {bank_data[username]['balance']}")

# View account statement
def account_statement(username):
    print("\nTransaction History:")
    for transaction in bank_data[username]["transactions"]:
        print(transaction)
    print(f"Current Balance: {bank_data[username]['balance']}")

# Close an account
def close_account(username):
    del bank_data[username]
    print("Account closed successfully!")

# Menu-driven interface
def main():
    while True:
        print("\n*** Digital Bank System ***")
        print("1. Register Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_account()
        elif choice == "2":
            username = login()
            if username:
                while True:
                    print("\n*** Banking Menu ***")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Check Balance")
                    print("4. Account Statement")
                    print("5. Close Account")
                    print("6. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        deposit(username)
                    elif user_choice == "2":
                        withdraw(username)
                    elif user_choice == "3":
                        check_balance(username)
                    elif user_choice == "4":
                        account_statement(username)
                    elif user_choice == "5":
                        close_account(username)
                        break
                    elif user_choice == "6":
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid choice! Please try again.")
        elif choice == "3":
            print("Thank you for using the Digital Bank System!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    # main()
    print(__name__)




# bank_data = {}

# # Register a new account
# def register_account():
#     username = input("Enter Username: ")
#     if username in bank_data:
#         print("Username already exists!")
#         return
#     name = input("Enter Full Name: ")
#     balance = float(input("Enter Initial Deposit: "))
#     bank_data[username] = {"name": name, "balance": balance, "transactions": []}
#     print("Account created successfully!")

# # Deposit money
# def deposit():
#     username = input("Enter Username: ")
#     if username not in bank_data:
#         print("User does not exist!")
#         return
#     amount = float(input("Enter Amount to Deposit: "))
#     bank_data[username]["balance"] += amount
#     bank_data[username]["transactions"].append(f"Deposited: {amount}")
#     print(f"Amount {amount} deposited successfully!")

# # Withdraw money
# def withdraw():
#     username = input("Enter Username: ")
#     if username not in bank_data:
#         print("User does not exist!")
#         return
#     amount = float(input("Enter Amount to Withdraw: "))
#     if amount > bank_data[username]["balance"]:
#         print("Insufficient balance!")
#         return
#     bank_data[username]["balance"] -= amount
#     bank_data[username]["transactions"].append(f"Withdrawn: {amount}")
#     print(f"Amount {amount} withdrawn successfully!")

# # Check account balance
# def check_balance():
#     username = input("Enter Username: ")
#     if username not in bank_data:
#         print("User does not exist!")
#         return
#     print(f"Account Balance for {username}: {bank_data[username]['balance']}")

# # View account statement
# def account_statement():
#     username = input("Enter Username: ")
#     if username not in bank_data:
#         print("User does not exist!")
#         return
#     print(f"\nTransaction History for {username}:")
#     for transaction in bank_data[username]["transactions"]:
#         print(transaction)
#     print(f"Current Balance: {bank_data[username]['balance']}")

# # Close an account
# def close_account():
#     username = input("Enter Username: ")
#     if username not in bank_data:
#         print("User does not exist!")
#         return
#     del bank_data[username]
#     print("Account closed successfully!")

# # Menu-driven interface
# def main():
#     while True:
#         print("\n*** Bank Management System ***")
#         print("1. Register Account")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Check Balance")
#         print("5. Account Statement")
#         print("6. Close Account")
#         print("7. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             register_account()
#         elif choice == "2":
#             deposit()
#         elif choice == "3":
#             withdraw()
#         elif choice == "4":
#             check_balance()
#         elif choice == "5":
#             account_statement()
#         elif choice == "6":
#             close_account()
#         elif choice == "7":
#             print("Thank you for using the Bank Management System!")
#             break
#         else:
#             print("Invalid choice! Please try again.")

# # Run the program
# if __name__ == "__main__":
#     main()
