# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except (ValueError, ZeroDivisionError) as e:
#     print("Error occurred:", e)


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except (ValueError, ZeroDivisionError) as a:
#     print("Invalid input!",a)
# else:
#     print("You entered:", num)




# --------------------------

# import json

# try:
#     with open("Bank3.json", 'r') as file:
#         bank = json.load(file)
#     print("file is found")
# except FileNotFoundError as a:
#     print("Error",a)
#     # with open("Bank1.json", 'w') as file:
#     #     # bank = json.load(file)
#     #     pass
# else:
#     print("File is found")

# num = [1,2,3,'a',4,5]
# sum = 0
# while len(num) != 0:
#     try:
#         for i in num:
#             sum += num.pop()
#     except:
#         print("error")
#     finally:
#         num = [1,2,3,'a',4,5]
#     print(num)


# amount = 2000

# if amount < int(input("Enter the amount u wants")):
#     raise ValueError("I'm just show ing")


# ans = 0
# try:
#     num = int(input("Enter the value: "))
#     ans = 10/num
# except (ValueError,ZeroDivisionError) as a:
#     print("Error: ",a)

# import paa as np
# big_list = 100
# print(type(big_list))
# big_list = [1] * (10**10) 

# print(int("12"))
print(ord("A"))