# Write a Python program that calculates the sum of all elements in a list using a loop.

# lst = [1,2,3,4,5,6,7,8,9]
## print(sum(lst))
# s = 0
# for i in lst:
#     s +=i
# print(s)


# Write a Python program to find the largest element in a given list of integers using a loop. 

# print(max(lst))
# num = MIN_VALUE


# lst = ['1','2','3','4','5']

# print("##".join(lst))

# lst2 = "Hello worlds , I'm programming the software"
# print(lst2.split("a"))


board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


for i in range(3):
    print("|".join(board[i]))
    print('-'*6)