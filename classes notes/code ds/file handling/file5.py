import csv
import json


# # print(dir(csv))

# with open("cv.csv","r") as file, open("js.json",'w') as file2:

#     # reader = csv.reader(file)
#     # for lines in reader:
#     #     print(lines)

#     reader = csv.DictReader(file)
    
#     data  = [i for i in reader]
    
#     json.dump(data, file2, indent = 4)



# -------------------------------------


'''5. Remove duplicate rows from a CSV file while keeping the
first occurrence.
 Input (CSV file):
 ID,Name,City
 1,Alice,Delhi
 2,Bob,Mumbai
 3,Alice,Delhi
 4,Bob,Pune

Output:
 ID,Name,City
 1,Alice,Delhi
 2,Bob,Mumbai
 4,Bob,Pune
'''
# lst = []
# lst2 = []
# ans = []
# ans2 = []

# se = set()

# with open("cv.csv",'r') as file, open('cv2.csv', 'w') as file2:
#     reader = csv.reader(file)
#     data = [i for i in reader]

#     for i in data:
#         lst.append([i[0],f"{i[1]} {i[2]}"])
#         lst2.append(f"{i[1]} {i[2]}")
    
#     for i in lst:
#         if i[1] not in ans2:
#             ans.append([i[0],i[1].split(" ")])
#             ans2.append(i[1])



# for i in ans:
#     print(i)



# ------------------------------------------






    
    
    

