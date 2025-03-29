# Json
# import json

# data = {
#     "key":"value",
#     "a":1,
#     "b":2,
#     "c":3
# }

# with open("file.json",'w',) as f:
#     json.dump(data, f, indent=4)


# with open("file.json",'r',) as f:
#     line = json.load(f)



# -----------------------------------

import csv
# data = [
#     ["Name", "Age", "City"],
#     ["Hemant", 25, "Purnia"],
#     ["Alice", 22, "Delhi"],
#     ["Bob", 23, "Mumbai"]
# ]

# with open("file.csv",'r', newline= "") as f:
#     # writer = csv.writer(f)
#     # writer.writerow(data)

#     # csv.writer(f).writerows(data)

#     temp = csv.reader(f)
#     for i in temp:
#         for j in i:
#             print(j)



''' 1. Read a CSV file and count occurrences of each unique
 value in a given column.
 ID,Name,City
 1,Alice,Delhi
 2,Bob,Mumbai
 3,Alice,Pune
 4,Bob,Delhi
 5,Charlie,Mumbai
 Output: Delhi: 2, Mumbai: 2, Pune: 1'''

data = '''ID,Name,City
 1,Alice,Delhi
 2,Bob,Mumbai
 3,Alice,Pune
 4,Bob,Delhi
 5,Charlie,Mumbai'''
temp = []
for i in data.split():
    temp.append(i.split(","))
print(temp)
with open('cv.csv','w',newline="") as file:
    writer = csv.writer(file).writerows(temp)
import os
os.system("cls")

d = {}
with open("cv.csv",'r') as file:
    data = csv.reader(file)
    for line in data:
        if line[2] in d:
            d[line[2]]+=1
        else:
            d[line[2]]=1
print(d)


    



