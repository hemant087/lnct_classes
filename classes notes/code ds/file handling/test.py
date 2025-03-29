''''2. Convert a CSV file into a JSON file with nested data.
ID,Name,Subject,Marks
1,Alice,Math,90
1,Alice,Science,85
2,Bob,Math,78
2,Bob,Science,88
Output:
[
 {"ID": 1, "Name": "Alice", "Subjects": {"Math": 90, "Science
 {"ID": 2, "Name": "Bob", "Subjects": {"Math": 78, "Science":
]
'''


# data = '''ID,Name,Subject,Marks
# 1,Alice,Math,90
# 1,Alice,Science,85
# 2,Bob,Math,78
# 2,Bob,Science,88'''

# data_lst = data.split("\n")

# final_data =[]
# for i in data_lst:
#     final_data.append(i.split(','))

# print(final_data)

# d = {}
# for i in 



# ---------------------------------------

# import csv
# import json

# with open("cv.csv",'r') as file, open("js.json",'w') as file2:
#     reader = csv.DictReader(file)
#     data = [read for read in reader]


#     json.dump(data,file2, indent=4)


# -----------------------------------------------

'''Find the row with the highest sum of numeric values in a
CSV file.
ID,Math,Science,English
1,80,90,85
2,75,95,88
3,85,80,82
3/6/25, 8:55 AM CSV and JSON Problems
127.0.0.1:5500/file handling/file.html 1/7
Output: Row with ID 2 has the highest sum: 258'''


