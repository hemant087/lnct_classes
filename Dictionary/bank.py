

# function for login
def login(bank):
    user_name = input("Enter the user name:  ")
    if user_name in bank:
        password = input(f"{user_name} Enter your password: ")
        if password == bank[user_name]:
            print(f"{user_name} Welcome to the bank, how can i help you sir/ma'am ")
        else:
            print(f"oops! wrong password, {user_name}")
    else:
        print("User not found")
    return bank

# functions for creating accounts
def create_account(bank):
    user_name = input("Create user name: ")
    if user_name not in bank:
        password = input(f"{user_name} create password: ")
        bank[user_name] = password
        print(f"{user_name} your account created")
    else:
        print("user name is already taken")
    return bank

# your main 
bank = {}
print(''' Welcome to --:Appna Bank:--
            How may i help you sir/ma'am:
            press 1: for login to your account
            press 2: for creating new account

''')
key_pressed = int(input("Press the key: "))
if key_pressed == 1:
    login()
elif key_pressed == 2:
    create_account()
    print(bank)