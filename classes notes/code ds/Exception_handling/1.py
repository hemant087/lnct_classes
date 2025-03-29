import getpass
import os
import json
    


with open("Bank.json", 'r') as file:
    bank = json.load(file)

def updated_file(bank):
    with open("Bank.json","w") as app_file:
            json.dump(bank, app_file, indent=4)
    return

# Create account
def create_acc(bank):
    os.system('cls')
    user_name = input("Enter the user name: ")
    if user_name not in bank.keys():
        password = getpass.getpass("Enter the password ")

        amount = int(input("Enter the Amount: "))

        log_history = []
        log_history.append(f"first Amount {amount}")


        bank[user_name]= {
            "password" : password,
            "balance" :amount,
            "log_history" : log_history

        }
        updated_file(bank)

        os.system('cls')
        print(f"{user_name} your account Successfully created\n here is your details {bank[user_name]}")
    else:
        print("user already exist")
    return bank

# User login

def login(bank):
    os.system('cls')
    user_name = input("Enter the user name: ")
    if user_name in bank:
        if bank[user_name]["password"] == input("Enter the password: "):
            print(f"__ {user_name} Successfully login to your Digital Bank__")
            while True:
                print('''
                    Press 1 : Deposit
                    Press 2 : withdrawal
                    Press 3 : Password Update
                    press 4 : Balance check
                    press 5 : Banking statement
                    press 6 : Account delete
                    press 7 : LogOut
                    ''')
                n = int(input("Enter the number (1,2,3,4) :  "))
                if n == 1:
                    credit_amo(user_name)
                    pass
                elif n == 2:
                    withdrawal_amo(user_name)
                elif n == 3:
                    password_update(user_name)
                elif n == 4:
                    balance_check(user_name)
                elif n == 5:
                    banking_stat(user_name)
                elif n == 6:
                    delete_acc(user_name)
                elif n == 7:
                    break
                else:
                    print("pressed invalid key ")

    updated_file(bank)           






#  credit amount 

def credit_amo(user_name):
    temp = bank[user_name]["balance"]
    print(f"{user_name} this is your balance {temp}")
    amount = int(input("Enter the deposit amount:  "))
    bank[user_name]["balance"] += amount
    bank[user_name]["log_history"].append(f"Deposited {amount}")
    temp2 = bank[user_name]["balance"]
    print(f"successfully deposited your amount\n this is you current balance {temp2}")
    updated_file(bank)
    return

#  withdrawal amount 

def withdrawal_amo(user_name):
    temp = bank[user_name]["balance"]
    print(f"{user_name} this is your balance {temp}")
    amount = int(input("Enter the deposit amount:  "))
    if amount <= temp:
        bank[user_name]["balance"] -= amount
        bank[user_name]["log_history"].append(f"Withdraw {amount}")
    else:
        print("insufficient balance")
    temp2 = bank[user_name]["balance"]
    print(f"successfully deposited your amount\n this is you current balance {temp2}")
    updated_file(bank)
    return

# Password Update
def password_update(user_name):
    temp = bank[user_name]["password"]
    print(f"This is you current Password {temp}")
    password= input("Enter the New password: ")
    conf_pass = getpass.getpass("Re-Enter the password: ")
    if password == conf_pass:
        bank[user_name]["password"] = conf_pass
        print("Your password Successfully updated ")
    else:
        print(f"{user_name} Oops! your password not matched")
    updated_file(bank)


# Balance check
def balance_check(user_name):
    temp = bank[user_name]["balance"]
    print(f"{user_name} your balance is {temp}")



# Banking statement
def banking_stat(user_name):
    temp = bank[user_name]["log_history"]
    print(f"{user_name} your Bank Statement: \n")
    for i in temp:
        print(i)


# Account delete
def delete_acc(user_name):
    del bank[user_name]
    print("Your account is deleted successfully")
    updated_file(bank)





def main():
    while True:
        print("__Welcome to Digital Bank__")
        print('''
            Press 1 : For Creating Acc.
            Press 2 : For Login Acc.
            Press 3 : For Exit 
            ''')
        n = int(input("Enter the number (1,2,3) :  "))
        if n == 1:
            create_acc(bank)
        elif n == 2:
            login(bank)
        elif n == 3:
            break
        else:
            print("pressed invalid key ")


if __name__ == "__main__":
    print(__name__)
    main()