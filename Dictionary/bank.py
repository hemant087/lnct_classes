bank = {}
# function for filling details in the bank


def details(bank, user_name):
    det = {}
    det["password"] = input(f"{user_name} Enter your password: ")
    det["name"] = input(f"{user_name} Enter your Name: ")
    det["address"] = input(f"{user_name} Enter your Address: ")
    det["id"] = input(f"{user_name} Enter your ID Number: ")
    det["contact"] = input(f"{user_name} Enter your Contact Number: ")
    bank[user_name] = det
    return bank
# function for updating the details


def update(bank,user_name):
    # status = login(bank)
    # if status == True:
    bank = details(bank, bank[user_name])


# function for login
def login(bank):
    user_name = input("Enter the user name:  ")
    if user_name in bank:
        password = input(f"{user_name} Enter your password: ")
        if password == bank[user_name]['password']:
            print(f"{user_name} Welcome to the bank, how can I help you, sir/ma'am?")
            return True
        else:
            print(f"Oops! Wrong password, {user_name}.")
    else:
        print("User not found.")
    return bank

# function for creating accounts


def create_account(bank):
    user_name = input("Create user name: ")
    if user_name not in bank:
        bank = details(bank, user_name)
        print(f"{user_name}, your account is created.")
    else:
        print("User name is already taken.")
    return bank


# main
while True:
    print(''' 
    Welcome to --:Appna Bank:--
    How may I help you, sir/ma'am:
    Press 1: for login to your account
    Press 2: for creating a new account
    Press 3: for updating your details
    Press 4: for Exit the bank

    ''')

    key_pressed = int(input("Press the key: "))
    if key_pressed == 1:
        login(bank)  # Pass the bank dictionary
    elif key_pressed == 2:
        create_account(bank)  # Pass the bank dictionary
        print(bank)
    elif key_pressed == 3:
        user_name = input("Enter the user name:  ")
        if user_name in bank:
            pas = input(f"{user_name} Enter your password: ")
            if pas == bank[user_name]['password']:
                print(f"{user_name}, your account ready for update")
                update(bank, user_name)
            else:
                print(f"Oops! Wrong password, {user_name}.")
        else:
            print("User not found.")
    elif key_pressed == 4:
        break
