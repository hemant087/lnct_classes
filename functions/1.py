# def add(a,b):
#     print(a+b)

# add(1,2)

# def add(a,b):
#     return a+b

# temp = add(1,2)
# print(temp)

# ------------------------------

# num = int(input("Enter the number: "))

# def fact(num):
#     temp = 1
#     for i in range(1,num+1):
#         temp *=i
#     return temp
# print(fact(num))


# def ana(a,b):
#     for i in a:
#         if i not  in b:
#             return "not anagram"
#     else:
#         return "anagram"


# print(ana('listen','houses'))


# def gcd(a,b):
#     for i in range(min(a,b),0,-1):
#         if a%i == 0 and b%i == 0:
#             return i

# print(gcd(12,18))


# armstrong 

# num = 123
# def is_armstrong(num):
#     l = len(str(num))
#     s = 0
#     for i in str(num):
#         s += int(i)**l 
#     if s== num:
#         print("number is Armstrong")
#     else:
#         print("not")
# is_armstrong(num)



#   --------------------
lst = []
num = 5
for i in range(num):
    if i == 0:
        lst.append(0)
    elif i == 1:
        lst.append(1)
    elif i >=2:
        lst.append(lst[i-1]+lst[i-2])
print(lst)