# # 5. Reverse the Contents of a File
# with open('filehandling.text','r') as f:
#          lines=f.readlines()
#          new_lines=lines[-3:]
#          finel_lines=lines[:2]+new_lines[::-1]
# with open('filecopy','w') as new:
#   new.writelines("\n ".join(finel_lines))
#   print("SUccesfully ")


# with open("file.txt",'r') as f, open("file2.txt",'w') as f2:
#     lines = f.readlines()
#     print(lines[::-1])
#     f2.write(lines[-1])
#     for line in lines[-2::-1]:
#         print(line)
#         f2.write(line)



''' 7. Remove Punctuation from a File
 Remove all punctuation marks from a text file.
 Test Case:
 Input File:
 kotlin
 Copy
 Edit
 Hello, world! Python is fun.
 Output File:
 kotlin
 Copy
 Edit
 Hello world Python is fun'''

import re
import os

with open("file.txt",'r') as f, open("file2.txt",'w') as f2:
    # line = f.readline().split()
    # print(line)
   
    # for i in range(len(line)):
    #     if "!" in line[i]:
    #         line[i] = line[i][:-1]
         #---------------------------- 
    # print(line)
    # lines = f.readline()   #Hello, world! Python is fun
    # temp = ""
    # for i in lines:
    #     if i == "!":
    #         temp = lines[:lines.index(i)] + lines[lines.index(i)+1:]
    # print(temp)

    # --------------------------------
    # lines = f.readline()
    # # for i in lines:
    # line = re.sub("!","",lines)
    # print(line)

    # line = f.read()

    # if line.strip():
    #     print("True")
    # else:
    #     print("False")
    pass


temp = ""

if temp.strip():
    print(True)
else:
    print(False)





