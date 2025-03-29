# a = [1,2,3,4,5]
# b = [1,2,3,4,5]

# c = set(a)
# d = set(b)

# print(hax(5))
# print(0101)
# lst = [(1,2),(12,),(),(7,2)]


# for  i in range(len(lst)):
#     print(len(lst[i]))


# '''4)**Remove empty tuples from a list
# a = [(1, 2), (), (3, 4), (), (5,)]
# def remove_tuple(lst):
#     for n in lst:
#         if len(n)==0:
#             print(n)
#             lst.remove(n)
#     return lst
# print(remove_tuple(a))

# ---------------------------------------------------

'''10)*Pair elements with Rear element in Matrix Ro
list  : [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
pairing : [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]'''

# lst = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
# # pairing : [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]

# ans =[]

# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         temp = [lst[i][j]]
#         for k in range(j,len(lst[i])-1):
#             temp.append(lst[i][k])
#             ans.append(temp)

# print(ans)


# s = {2,3,4,9,56,8} # superset
# s2 = {3,8,9}  # subset

# print(s & s2)
# print(s | s2)
# print(s ^ s2)
# print(s-s2)
# print(s.issuperset(s2))
# # for i in s:
# #     print(i)

# s2.update(s)
# print(s2)
# # print(s.add(s2))

# x = ["apple", "banana", "cherry"]
# y = {"google", "microsoft", "apple"}

# temp = y.pop(0)

# print(y)
# print(temp)

# lst = [8,9,4,2,6,5]

# # selection sorting
# for i in range(len(lst)):
#     for j in range(i, len(lst)):
#         if lst[i] > lst[j]:
#             temp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = temp
# print(lst)
# -------------------------------------------


# # bubble sorting
# for i in range(1,len(lst)):
#     for j in range(len(lst)-i):
#         if lst[j]>lst[j+1]:
#             lst[j],lst[j+1] = lst[j+1],lst[j]
# print(lst)
# -------------------------------------------------
# lst = [8,9,4,2,6,5]


# for i in range(1,len(lst)):
#     key = lst[i]
#     j = i-1
#     print(f"         i --> {lst[i]}")

#     print(lst)
#     while j >=0 and key < lst[j]:

#         print(f"{lst[j+1]} <==>  {lst[j]}")
#         lst[j+1] = lst[j]
#         j -=1
#     lst[j+1] = key
#     print(lst)
# # print(lst)

# subset = [[]]

# for i in lst:
#     for j in subset:
#         subset.append(j+[i])
# print(subset)

# s = {5, 8}
# ls = list(s)
# ans = []
# for i in range(len(s)**2):
#     st = set()
#     for j in range(len(s)):
#         if i & (j*2):
#             print(f" {i} --> {j*2}")
#             st.add(ls[j])
#         else:
#             print(f" {i} --> {j*2}")

#         print(st)
#     ans.append(st)
# print(ans)

# print(ans)
# print(ans)

# s = {1, 3, 2, 5, 4}
# k = 3
# output = {(1, 2), (3, 3)}

# lst = list(s)
# ans = set()

# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if (lst[i]+lst[j])% k == 0 and (lst[j],lst[i]) not in ans:
#             ans.add((lst[i],lst[j]))

# print(ans)


# student = {'name': [1,2,38,4], 'age': 23, 'major': 'Computer Science'}
# # print(student['major'])
# # print(student.get('major'))


# # student.update({'key':'value'})

# lst = {1,2,3,4}
# lst.update({9})

# print(student)


# s = "Hello,world"
# lst = ["hemant","my","name","is"]
# # temp = s.split(",")
# temp = "            ".join(lst)


# print(temp)


# given string is Heterogram or not
# s = "the big dwarf only jumps"

# lst = s.split(" ")

# for i in lst:
#     if lst.count(i) > 1:
#         print("Not")
#         break
# else:
#     print("Heterogram")


'''Input : arr[] = {1, 2, 3, 4}
Output :1
Explanation : A single subset can contains all 
values and all values are distinct

Input : arr[] = {1, 2, 3, 3}
Output : 2
Explanation : We need to create two subsets
{1, 2, 3} and {3} [or {1, 3} and {2, 3}] such
that both subsets have distinct elements.'''

# arr = {1, 2, 3, 3}
# lst = list(arr)
# ans = []
# for i in range(2**len(arr)):

#     j = i
#     temp = set()
#     while i > j and i & (1<<j):
#         lst[j+1] = lst[j]
#         temp.add(lst[j+1])
#     lst.append(temp)

# print(lst)


# s = {1,2,3,4}

# s.add(2)
# print(s)

# print("he",1<<0)


# fun = lambda a,b: a+b

# print(fun(4,5))


# lst = [2,4,1,23,64]

# ans = list(map(lambda i: i**2, lst))

# print(ans)
# ans = [0,1]
# def fun():
#     n = 7
#     for i in range(n):
#         ans.append(ans[i]+ans[i+1])
#     return ans

# temp = list(map(fun,ans))

# print(temp(5))

lst = [i for i in range(10)]

# temp = list(filter(lambda i: i%2 ==0, lst))

# ans = list(map(lambda i: i**2, temp))


# print(temp, ans)


# from functools import reduce

# temp = reduce(lambda i,j: i if i>j else j,lst)

# print()

# temp = list(map(lambda i: i%2 == 0, lst))

# print(temp)

# a = [1,2,3,45,5,5,66,6,]
# lst = [i**2 for i in a]

# print(lst)

# for i in range()


# def fun(n):
#     print(n)
#     n=n+1
#     return fun(n)

# print(fun(5))


# lst = [0,1,1,2,3,5,8,13]

# lst = [1,2,3,6,12,24,48....]

# def fun(n, ans):
#     if n >5:
#         return ans
#     else:
#         print(ans)
#         return fun(n+1,ans+ans)

# print(fun(1,3))

'''2. Factorial of a Number
Write a function factorial(n) that returns the factorial of a number.
Test Cases:
print(factorial(5)) # Output: 120
print(factorial(0)) # Output: 1'''

# def fun(n):
#     if n==1:
#         return 1
#     else:
#         return n * fun(n-1)

# print(fun(5))


# def fun(n,ans):
#     if n ==6:
#         return ans
#     else:
#         ans =ans *n
#         return fun(n+1, ans)

# print(fun(1,1))


'''18. Nested Dictionary Flattening
Flatten a nested dictionary so that the keys are a combination of the nested keys.
Test Cases:
Input: {'a': {'b': {'c': 1}}}
Output: {'a_b_c': 1}
Input: {'x': {'y': 10}, 'z': {'a': 20}}
Output: {'x_y': 10, 'z_a': 20}
'''

# def fun(d): #
#     ans = {}
#     if type(d.values()) == dict:
#         for key, val in d.items():
#             ans = d
#             if type(val) != dict:
#                 return ans
#             else:
#                 for k, v in val.items():
#                     ans[key+"_"+k] = v
#                     return fun(ans)


# # {b_c:1} ==> a_b_c:1

# # d = {'x': {'y': 10}, 'z': {'a': 20}}
# d = {'a': {'b': {'c': {'e':1}}}, 'y': {'z': {'c': {'e':9}}}, "mg":34}
# f = {} #a_c_c_e = 1, y_z_c_e = 9
# for key, val in d.items():
#     if type(val) == dict:
#         temp = fun(val)
#         f[key+"_"+temp[0]] = temp[0].values()
#     else:
#         f[key] =val


# def fun(d):
#     ans = {}
#     if isinstance(d, dict):  # Corrected check for dictionary
#         for key, val in d.items():
#             ans = d  # This should be initialized properly, but isn't necessary
#             if not isinstance(val, dict):  # Check if `val` is not a dictionary
#                 return ans
#             else:
#                 for k, v in val.items():
#                     ans[key + "_" + k] = v
#                 return fun(ans)  # Don't return inside the loop

# d = {'a': {'b': {'c': {'e':1}}}, 'y': {'z': {'c': {'e':9}}}, "mg":34}
# f = {}

# for key, val in d.items():
#     if isinstance(val, dict):
#         temp = fun(val)  # temp is a dictionary
#         if isinstance(temp, dict) and temp:  # Check if temp is a valid dictionary
#             first_key = list(temp.keys())[0]  # Get the first key from temp
#             f[key + "_" + first_key] = temp[first_key]  # Assign value correctly
#     else:
#         f[key] = val  # Fixed syntax error

# print(f)


# def fun(d):
#     ans = {}
#     for key, val in d.items():
#         if isinstance(val,dict):
#             nested = fun(val)
#             for k, v in nested.items():
#                 ans[key+"_"+k]=v
#         else:
#             ans[key]=val
#     return ans


# d = {'a': {'b': {'c': {'e': 1}}}, 'y': {'z': {'c': {'e': {'r':34}}}}, "mg": 34}


# # print(fun(d))


# def fun(d,key_name = ""):
#     ans = {}
#     for key,val in d.items():
#         if isinstance(val, dict):
#             key_name = f"{key}_{val.keys()}"
#         else:
#             key_name = key
#         ans.update(fun(ans,key_name))
#     return ans

# print(fun(d))


# 13)Convert Nested dictionary to Mapped Tuple**[('x', (5, 1, 8)), ('y', (6, 4, 3))]
# d = {'gfg': {'x': 5, 'y': 6}, 'is': {'x': 1, 'y': 4}, 'best': {'x':8,'y':3}}

# [('x', (5, 1, 8)), ('y', (6, 4, 3))]

# ans = {}
# lst =[]
# for key, val in d.items():
#     temp = ()
#     for k, v in val.items():
#         if k not in ans:
#             ans[k] = [v]
#         else:
#             ans[k].append(v)
# print(ans)

# for key,val in ans.items():
#     lst.append((key,tuple(val)))
# print(lst)

# # 14)Ways to convert string to dictionary
# s = "{'a': 1, 'b': 2, 'c': 3}"

# ans = {}
# for i in range(len(s)-2):
#     if s[i] == ":":
#         ans[s[i-2]] = int(s[i+2])

# print(ans)


'''15)Given a Dictionary, divide dictionary into K sized different dictionaries list.'''
d={'Gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'geeks': 5, 'CS':6}
# K = 3
# [{'Gfg': 1, 'is': 2, 'best': 3},['for': 4, 'geeks': 5, 'CS': 6]]
# lst = []
# for i in range(,len(d),3):
# lst = []
# count = 0
# new_d = {}
# for key, val in d.items():
#     new_d[key]=val
#     count+=1
#     if count == 3:
#         lst.append(new_d)
#         count = 0
#         new_d = {}
# print(lst)


# print([{:d[i],i}for i in range(len(d))])
    

# 17)Create Nested Dictionary using given List****** {8: {‘Gfg’: 4}, 2: {‘best’: 9}} 
# test_dict = {'Gfg' : 4, 'is' : 5, 'best' : 9} 
# test_list = [8, 3, 2]


# [0,1,1,2,3,5,8,13.....]


# def fun(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         return fun(n-2) + fun(n-1)


# lst = []
# for i in range(7):
#     lst.append(fun(i))
# print(lst)





''' 1. Lambda to Reverse Alternate Words in a String
 Write a lambda function that takes a string and reverses alternate words in it.
 Test Cases:
 Input: "The quick brown fox"
 Output: "The kciuq brown xof"
 Input: "Python is fun"
 Output: "Python si fun"'''

'''13. Count Vowels using Recursion
 Write a recursive function to count the number of vowels in a string.
 Test Cases:
 Input: "education" → Output: 5
 Input: "rhythm" → Output: 0'''

# def fun(word):
#     if len(word) ==0:
#       return 0
#     else:
#         return (1 if word[0] in ['a','e','i','o','u'] else 0) + fun(word[1:])


# print(fun('edu'))

from functools import reduce

word = "education"
s = 0
ans = reduce(lambda s,i: s+1 if i in ['a','e','i','o','u'] else s, word,s)
print(ans)



# lst = [1,2,3,4,5,6]
# temp = reduce(lambda i, s: i+s , lst)

# print(temp)


# numbers = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, numbers)
# print(product) 