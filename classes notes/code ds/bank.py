import getpass
import os
bank = {}

# Create account
def create_acc(bank):
    os.system('cls')
    user_name = input("Enter the user name: ")
    if user_name not in bank:
        temp = []
        password = getpass.getpass("Enter the password ")
        bank[user_name]= temp.append(password)

        amount = int(input("Enter the Amount: "))
        temp.append(amount)

        log_history = []
        log_history.append(f"first Amount {amount}")
        temp.append(log_history)
        bank[user_name] = temp

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
        if bank[user_name][0] == input("Enter the password: "):
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
                    credit_amo(user_name, bank[user_name])
                elif n == 2:
                    withdrawal_amo(user_name,bank[user_name])
                elif n == 3:
                    password_update(user_name,bank[user_name])
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
                os.system('cls')
                

#  credit amount 

def credit_amo(user_name, user_det):
    print(f"{user_name} this is your balance {user_det[1]}")
    amount = int(input("Enter the deposit amount:  "))
    user_det[1] += amount
    user_det[2].append(f"Deposited {amount}")
    print(f"successfully deposited your amount\n this is you current balance {user_det[1]}")
    return bank

#  withdrawal amount 

def withdrawal_amo(user_name, user_det):
    print(f"{user_name} this is your balance {user_det[1]}")
    amount = int(input("Enter the deposit amount:  "))
    if amount <= user_det[1]:
        user_det[1] -= amount
        user_det[2].append(f"Withdraw {amount}")
    else:
        print("insufficient balance")
    print(f"successfully deposited your amount\n this is you current balance {user_det[1]}")
    return bank

# Password Update
def password_update(user_name, user_det):
    print(f"This is you current Password {user_det[0]}")
    password= input("Enter the New password: ")
    conf_pass = getpass.getpass("Re-Enter the password: ")
    if password == conf_pass:
        user_det[0]= conf_pass
        print("Your password Successfully updated ")
    else:
        print(f"{user_name} Oops! your password not matched")


# Balance check
def balance_check(user_name):
    print(f"{user_name} your balance is {bank[user_name][1]}")



# Banking statement
def banking_stat(user_name):
    print(f"{user_name} your Bank Statement: \n")
    for i in bank[user_name][2]:
        print(i)


# Account delete
def delete_acc(user_name):
    del bank[user_name]
    print("Your account is deleted successfully")



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