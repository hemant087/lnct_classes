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
# lst = []
# num = 5
# for i in range(num):
#     if i == 0:
#         lst.append(0)
#     elif i == 1:
#         lst.append(1)
#     elif i >=2:
#         lst.append(lst[i-1]+lst[i-2])
# print(lst)


# def add(n,s):
#     if n == 10:
#         return s + add(n,s)
#     n += 1
# print(add(0,0))

#----------------------------------------------------------

# def fun(n,s):
#     if n == 0:
#         return s
#     s = s+n%10
#     n = n//10
#     return fun(n,s)
# print(fun(12345,0))

# def fun(n,s):
#     if n == 0:
#         return 
#     s = s+ n%10
#     n = n//10
#     return fun(n,s)
# print(fun(12345,0))

# def fun(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fun(n-1) + fun(n-2)
# print(fun(7))

# -----------------------------------


# def palindrome(s):
#     if len(s)<=1:
#         return "True"
#     elif s[0] != s[-1]:
#         print(s[0],s[-1])
#         return False
#     print(s[0],s[-1])
#     return palindrome(s[1:-1])
# print(palindrome("abccba"))


# --------------------------------

# def rev(s):
#     if len(s) <= 0:
#         return s
#     else:
#         return s[-1]+rev(s[0:-1])
# print(rev("hello"))

# ----------------------------------------

# def sam(lst):
#     if len(lst) <=0:
#         return 0
#     else:
#         return lst[0]+sam(lst[1:])
# print(sam([1,2,3,4,5,6]))

# ---------------------------------------

# count 


# ----------------------------------------

# def check_p(num):
#     if num == 0:
#         return 
#     else:
#         if num %2 ==0:

# def fun(a,n):
#     if n==0:
#         return 1
#     else:
#         return a*fun(a,n-1) 
# print(fun(2,5))

# ------------------------------------


# temp = lambda x: x*x for x in lst:
# print(temp([2,3]))

# -------------------------------------------


# num = [1,2,3,4,5]

# temp = lambda x,y: x+y
# print(temp(5,2))

# print(list(map(lambda x: x**2, num)))

# --------------------------------

# def fun(s):
#     if len(s) <=0:
#         return 0
#     else:
#         if s[0] in ['a','i','o','u','e']:
#             return 1 + fun(s[1:])
#         else:
#             return 0+fun(s[1:])
# print(fun("hello"))

# def count_v(s):
#     if len(s) <=0:
#         return 0
#     else:
#         if s[0] in ['a','i','o','u','e']:
#             return 1+count_v(s[1:])
#         else:
#             return count_v(s[1:])
        
# print(count_v("education"))


# -------------------------------------------

# def fun(n,i):
#     if n == i:
#         return 1
#     elif n % i == 0:
#         return 1 + fun(n,i+1)
#     else:
#         return fun(n,i+1)
# print(fun(7,1))

# if fun(8,1) == 2:
#     print("prime")
# else:
#     print("not prime")

# ----------------------------------------

# def fun(a):
#     return a**2
# lst = [1,2,3,4,5]
# temp = list(map(fun,lst))
# print(temp)

# a = 11
# temp  = lambda a: 18>a == 0
# print(temp(a))

# ----------------------------------------------------

# m = filter(lambda a: mx = a if a>mx else mx = mx )

# Input: [[1, 2], [3, [4, 5]]] → Output: [1, 2, 3, 4, 5]

n = 10
print('even') if n%2 == 0 else print('odd')