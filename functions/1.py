# def add(a,b):
#     print(a+b)

# add(1,2)

# def add(a,b):
#     return a+b

# temp = add(1,2)
# print(temp)

# ------------------------------

num = int(input("Enter the number: "))

def fact(num):
    temp = 1
    for i in range(1,num+1):
        temp *=i
    return temp
print(fact(num))

