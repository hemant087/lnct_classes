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


num = (1,2,3,4)
num2 = (5,6,7,8)
# (6,8,10,12)
ans = ()
temp = (1)
print(f"{temp}----> {type(temp)}")
temp2 = (1,)
print(f"{temp2}----> {type(temp2)}")


for i in range(4):
    ans = ans + (num[i]+num2[i],)

print(ans)

# immutable --> cant change the value