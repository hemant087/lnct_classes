hemant = {
    "aman":{
        "raj":[1,2,3]
    }
}
# import json

# # with open("Bank.json",'a') as file:
# #     json.dump(hemant,file, indent=4)
# #     json.dump(hemant,file, indent=4)

# with open("Bank.json",'r') as file:
#     bank = json.load(file)
# print(bank)


import json

# while True:
#     user = input("Enter ur name:  ")
#     with open(f"{user}.json",'w') as file:
#         json.dump(hemant,file, indent=4)

with open("Bank.json", 'r') as file:
    bank = json.load(file)
        
