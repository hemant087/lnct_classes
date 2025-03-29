'''18. Nested Dictionary Flattening
Flatten a nested dictionary so that the keys are a combination of the nested keys.
Test Cases:
Input: {'a': {'b': {'c': 1}}}
Output: {'a_b_c': 1}
Input: {'x': {'y': 10}, 'z': {'a': 20}}
Output: {'x_y': 10, 'z_a': 20}
'''

# def fun(d): 
#     ans = {}
#     for key, val in d.items():

#         if isinstance(val, dict):
#             nested = fun(val)
#             for k,v in nested.items():
#                 ans[key+"_"+k] = v
#         else:
#             ans[key] = val
        
#     return ans

# d = {'a': {'b': {'c': {'e':1}}}, 'y': {'z': {'c': {'e':9}}}, "mg":34}
# print(fun(d))


# import getpass

# password = getpass.getpass()

# print(password)
# bank = {"hemant":193}

# def fun():
#     print(bank["hemant"])
#     print(bank)
# print(fun())

# if __name__ == 


# ==================================================================


file = open('hemant.txt','a')
print(file.write(input("Enter the text: ")))
file.close()

