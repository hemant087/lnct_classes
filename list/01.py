# num = (1+2j)

# print(type(num))

# st = "Hi my name is "

# for i in st:
#     print(i)

# a= {1,2,3,4}
# b = {5,1,7,8}
# d = a&b
# print(d)


# D = {}

# for i in range(5):
#     key = input("Enter the key: ")
#     temp = []
#     for i in range(4):
#         Val = input("Enter the value: ")
#         temp.append(Val)
#     D[key] = Val 
# print(D)

# print({True:"Hemat",False:"5667"})
# print([1,2,3,4]:[5,6,7,8])



# there is shop i need to buy it,, first check that "A" is available or not,,,
# if Yes: should i buy it or not (Y/N)
# Yes: Ask price 
# print ==> i bought "A"

# a = input("Hello ! will i get A-Product in you shop (Y/N):  ")
# amount = 100

# if a == "Y":
#     print("Yes, its available ")
#     price = int(input(" What will be the price of it:  "))
#     if price <= amount:
#         print("i bought")
# else:
#     print("Sorry A-product is not available")

# if a=="Y" and int(input(" What will be the price of it:  ")) <= amount:
#     print()


# num = (1,2,3,4)
# num2 = (5,6,7,8)
# # (6,8,10,12)
# ans = ()
# temp = (1)
# print(f"{temp}----> {type(temp)}")
# temp2 = (1,)
# print(f"{temp2}----> {type(temp2)}")


# for i in range(4):
#     ans = ans + (num[i]+num2[i],)

# print(ans)

# immutable --> cant change the value


# make a list where you need to append the 3 students details(name,roll,class,phone no)

# lst = []


# condition_1 = True
# condition_2 = True

# # code -1
# if condition_1:
#     print("condition 1 is True")
#     if condition_2:
#         pass


# # code -2 
# if condition_1 and condition_2:
#         pass


# for i in range(10):
#     pass


t = (3,2,7,10)

# num = int(input("enter the number: "))

# print(t + ((t[t.index(10)])+num,))


# for i in t:
#     print(i)

# temp = list(t)    # tuples converted in list
# num = temp.index(max(temp))  
# temp[num] = temp[num] + int(input("enter the number"))
# t = tuple(temp)

# print(t)
# num1 = temp.index(max(t))  
# print(t[num1])


d = {}  # dictionary declare
n = 3
for i in range(n): # loop for the row iteration
    print(i,n)
    temp = []   # temporary list for the column entry
    k = input("Enter the name of Key :  ")
    if k not in d:
        for j in range(4): #loop for the column iteration
            temp.append(input("Enter the value: ")) 
        d[k] = temp  # assigning value(list) in key
    else:
        print("This key is already taken")
        continue
print(d)