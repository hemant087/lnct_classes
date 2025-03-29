''' 1. Lambda to Reverse Alternate Words in a String
 Write a lambda function that takes a string and reverses alternate words in it.
 Test Cases:
 Input: "The quick brown fox"
 Output: "The kciuq brown xof"
 Input: "Python is fun"
 Output: "Python si fun"'''

# s = "The quick brown fox"

# temp = list(map(lambda i,a: a[-1::-1] if i%2==0 else a,s.split(" "),0 ))

# print(temp)

# ---------------------------------------------------------------------


''' 2. Lambda to Flatten and Sort Nested Lists
 Write a lambda function to flatten a list of lists and sort it in ascending order.
 Test Cases:
 Input: [[3, 2], [1, 4, 5]]
 Output: [1, 2, 3, 4, 5]
 Input: [[10, -1], [7, 8, 0]]
 Output: [-1, 0, 7, 8, 10]'''

# lst = [[3, 2], [1, 4, 5]]

# # temp = list(map(lambda a: sum([],lst[a]), range(len(lst))))

# temp = lambda a: sorted(sum(a,[]))
# print(temp(lst))


# -------------------------------------------------

''' 3. Lambda for Fibonacci Sequence
 Write a lambda function that returns the nth Fibonacci number using reduce.
 Test Cases:
 Input: 6
 Output: 5
 Input: 10
Output: 34'''


# temp = lambda n: 0 if n==0 else temp(n-1)+temp(n-2) if n>1 else 1

# print(temp(7))



# -------------------------------------------------------------------------------



''' 1. Sum of Digits (Recursion)
 Write a recursive function to find the sum of digits of a given number.
 Test Cases:
 Input: 12345 → Output: 15
 Input: 9876 → Output: 30'''


# n = 12345

# # lst =[1,2,3,4,5,6]

# from functools import reduce
# temp = reduce(lambda s,i: s+i, [int(i) for i in str(n)])
# print(temp)


# ------------------------------------------------------------------



'''4. Fibonacci Sequence (Recursion)
 Write a recursive function to return the nth Fibonacci number.
 Test Cases:
 Programming Challenges
 Input: 7 → Output: 13
 Input: 10 → Output: 55'''



# temp = lambda n: 0 if n==0 else temp(n-1)+temp(n-2) if n >1 else 1

# print(temp(7))


''' 7. Exponentiation using Recursion
 Write a recursive function to calculate a^b.
 Test Cases:
 Input: 2, 5 → Output: 32
 Input: 3, 3 → Output: 27'''


# def fun(n,r):
#     if r == 0:
#         return 1
#     else:
#         return n* fun(n,r-1)
# print(fun(2,5))


# temp = lambda n,r: 1 if r==0 else n*temp(n,r-1)

# print(temp(2,5))


# ----------------------------------------------------------------


''' 15. Lambda Function for Sorting
 Use a lambda function to sort a list of tuples based on the second element.
 Test Cases:
 Input: [(1, 3), (2, 1), (4, 2)] → Output: [(2, 1), (4, 2), (1, 3)]
 Input: [(10, 20), (30, 10), (40, 30)] → Output: [(30, 10), (10, 20), (40, 30)]'''


# lst = [(10, 20), (30, 10), (40, 30)]


# def fun(lst):
#     for i in range(len(lst)):
#         for j in range(i+1,len(lst)):
#             if lst[i][1] > lst[j][1]:
#                 lst[i], lst[j] = lst[j], lst[i]

#     return lst
# print(fun(lst))

        

# i = (10,20)


# temp = list(map(lambda i: (i, lst[j] = lst[j],i) if (i[1]> lst[j][1]) else pass  for j in range(lst.index(i)+1 ,len(lst)) , lst))


# print(temp(lst))


''' 16. Find GCD using Recursion
 Write a recursive function to calculate the GCD of two numbers.
 Test Cases:
 Input: 36, 60 → Output: 12
 Input: 48, 18 → Output: 6'''


# from functools import reduce

# temp = lambda a,b: t if min(a,b) % t == 0 for t in range(min(a,b),0,-1)

# temp = reduce(lambda t, a,b: t if min(a,b) % t == 0 , )

# print(temp(36,60))


# print(12%18)


# def fun(n,i):
#     if i == 0:
#         return 1
#     else:
#         if n%i == 0:
#             return 1 + fun(n,i-1)
#         else:
#             return fun(n,i-1)


# print(fun(7,7))

# if fun(7,7) == 2:
#     print('its a prime')
# else:
#     print('not prime number')


'''Write a lambda function to compress consecutive repeating characters in a string.
Test Cases:
Input: "aaabb"
Output: "a3b2"
Input: "abcd"
Output: "a1b1c1d1"'''
# n="aaabb"
# l=list(n)
# lst=[]
# for num in l:
#     if num not in lst:
#         lst.append(num)
#         lst.append(l.count(num))
# print(lst)'''



# l = "aaabb"
# temp = lambda l,lst: [for i in l lst.append(num) lst.append(l.count(num)) if i not in l ]


# temp = lambda l, lst:[i if i not in lst else l.count(i) for i in l ]

# ans=lambda l:[num if num not in lst else l.count(num) for num in l]

# ans = lambda l: sum([[ch, l.count(ch)] for ch in dict.fromkeys(l)], [])
# print(ans(l))

'''53)Input : arr[] = [4, 2, 7, 9]
Output : 20
Explanation: Here are total 4 combination: (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3).
So, the Sum of these combinations is 13, 15, 20, and 18. The maximum sum is 20.'''


# lst = [4, 2, 7, 9]

# lst = sorted(lst)
# print(lst[-1]+lst[-2]+lst[-3])

''' in the comments in the code editor and complete the functions push() and pop() to implement a stack. The push() method takes one argument, an integer 'x' to be pushed into the stack and pop() which returns an integer present at the top and popped out from the stack. If the stack is empty then return -1 from the pop() method.

Note: The input is given in form of queries. Since there are two operations push() and pop(), there is two types of queries as described below:
(i) 1 x   (a query of this type means  pushing 'x' into the stack)
(ii) 2     (a query of this type means to pop an element from the stack and print the popped element)
Input contains separated by space and as described above. 

Examples :

Input: 1 2 1 3 2 1 4 2 
Output: 3, 4
Explanation: 
push(2)    the stack will be {2}
push(3)    the stack will be {2 3}
pop()      poped element will be 3,
           the stack will be {2}
push(4)    the stack will be {2 4}
pop()      poped element will be 4

Input: Queries = 1 2 1 3 2 1 4 2
Output: 2 3
Explanation: For query 1 2 the queue will be {2} 1 3 the queue will be {2 3} 2   
poped element will be 2 the queue will be {3} 1 4 the queue will be {3 4} 2 poped element 
will be 3 '''

