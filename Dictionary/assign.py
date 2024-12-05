# S = "apple orange apple mango apple"  # string
# lst = S.split(" ")  #splitting the string
# print(lst)
# ans = {}   # declaring new  dictionary

# for i in lst:   # iterating list 
#     ans[i] = lst.count(i)   # assigning count in every elements
# print(ans)



# temp  = input("Enter the key:  ")
# if temp in d:
#     print("It exist already ")
# else:
#     print("Not exist ")


# d = {"c":3,"b":2,"a":1,"d":4}
# ans = dict(sorted(d.items()))
# print(ans)
# temp = d[]
# for key, value in d.items():
#     if temp < value:
#         ans[key] = value
#     else:


# lst = [1,2,3,4,56,54,34,23]
# n = 0
# n1 = 0
# for i in lst:
#     if i>n:
#         n1 = n
#         n = i
# print(n1,n)

# D =  {'a': 1, 'b': 3, 'c': 1}
# n = int(input("Enter the value: "))
# ans = {}
# for k, v in D.items():
#     if v != n:
#         ans[k]=v
# print(ans)

# d1 = {'a': 10, 'b': 20, 'c': 30} 
# d2 =  {'b': 5, 'c': 15, 'd': 25}
# for k, v in d1.items():
#     if k in d2.keys():
#         d2[k] = d2[k]+d1[k]
#     else:
#         d2[k] = v
# print(d2)

# d1 =  {'x': 30, 'y': 10, 'z': 20}
# ans = {}
# for i ,j in d1.items():
#     ans[j] = i
# ans = dict(sorted(ans.items()))
# print(ans)

lst = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
ans ={}
for i in lst:
    if i[0] in ans:
        ans[i[0]] = list(ans[i[0]])+ [i]
    else:
        ans[i[0]] = [i]

print(ans)