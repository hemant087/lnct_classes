#*LoginAccount*******
def login_acc(bank):
    os.system("cls")
    user_name=input("Enter your user name:")
    # *********************READ JSON FILE****************
    with open("Bank.json",'r') as file:
       bank= json.load(file)
       print(bank)
    #***************************************************** 
    if user_name in bank:
        bank[user_name][0]==input("enter your Password:")
        
        print(f"{user_name} SUCCESFULLY LOGIN IN DIGITAL BANK")
        while True:
            print('''
                    Press 1 : Credit
                    Press 2 : Withdrawal
                    Press 3 : Passward Update
                    press 4 : Balance check
                    press 5 : Banking statment
                    press 6 : Account Delete
                    press 7 : View Profile
                    press 8 : Logout
                    ''')
            n=input("Enter the number(1,2,3,4,5,6,7,8,):")
            if int(n)==1:
                credit(user_name)
            elif int(n)==2:
                widthrawal(user_name)
            elif int(n)==3:
                password_change(user_name)
            elif int(n)==4:
                balance_check(user_name)
            elif int(n)==5:
                bank_statment(user_name)
            elif int(n)==6:
                acc_delete(user_name)
            elif int(n)==7:
                view_profile(user_name)    
            elif int(n)==8:
                 break
            else:
                print("pressed invalid key ")
    else:
        print("Invalid user name")