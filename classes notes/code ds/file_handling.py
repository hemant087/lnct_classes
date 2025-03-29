# f = open(r"C:\Users\ASUS\OneDrive\Desktop\New folder\hemant.txt", 'rb')

# print(f.read())

# f.close()


# with open("hemant.txt", "r") as f:



# f= open("file_handling.txt",'w')
# # f.write(input("Enter the text : "))
# f.write()


# f = open("hemant.txt",'x')

# print(f.read())

# with open("hemant.txt",'r') as f:
#     print(f.read())
#     print("non")
#     print(f.tell())
# path = 
# f = open(r"C:\Users\ASUS\OneDrive\Desktop\Hem.PNG", 'rb')
# f = open(r"C:/Users/ASUS/OneDrive/Desktop/Hem.PNG", 'rb')
# f.write()
# print(f.read())


# 0-255 = 256 = 2^9 =512 = 2^10 = 1024



# ------------------------------------------------------------------------


f = open("hemant.txt","r")

temp = []
for i in f:
    temp.append(f.readline())
# print(f.read())
print(temp)