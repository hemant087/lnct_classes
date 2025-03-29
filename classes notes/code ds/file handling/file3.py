import json
data = {
    "name": "Hemant",
    "age": 25,
    "city": "Purnia"
}

# # Writing JSON data to a file
# with open("data.json", "a") as file:
#     json.dump(data, file, indent=4)  # indent=4 for readability


# Reading JSON data from a file
# with open("data.json",'w') as file:
#     # temp = json.load(file)

#     # print(type(temp))

#     json_string = json.dumps(data, indent=4)
#     print(json_string)




# --------------------------------------------------

import csv

data = [
    ["Name", "Age", "City"],
    ["Hemant", 25, "Purnia"],
    ["Alice", 22, "Delhi"],
    ["Bob", 23, "Mumbai"]
]

with open("data.csv",'w') as file:
    writer = csv.writer(file)
    writer.writecolumn(data)

