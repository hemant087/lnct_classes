# with open("file.txt",'w') as f:
#     f.write("Hello world! Python is great.")


# with open('file.txt','r') as f:
#     temp = f.read().split(" ")
#     print(len(temp))

# =============================================


''' 2. Find the Longest Word in a File
 Read a text file and return the longest word.
 Test Case:
 Input File:
 "Artificial Intelligence is fascinating."
 Output: "Intelligence"'''


# with open("file.txt", 'r') as f:
#     temp = f.read().split(' ')
#     s = 0
#     word = temp[0]
#     for i in temp:
#         if s < len(i):
#             s = len(i)
#             word = i

#     print(word)


# ---------------------------------------------------

'''3. Count Occurrences of a Specific Word
 Read a file and count the occurrences of a given word.
 Test Case:
 Input File:
 "Python is fun. Learning Python is great."
 Word to search: "Python"
 Output: 2'''


# with open("file.txt", 'r') as f:
#    temp =  f.read().split(' ')
#    print(temp.count("Python"))



# --------------------------------------------------


''' 4. Remove Blank Lines from a File
 Write a program to remove all blank lines from a text file.
 Test Case:
 Input File:
 nginx
 Copy
 Edit
 Hello
 World
 Python
 Output File:
 nginx
 Copy
 Edit
 Hello
 World
 Python'''


# with open('file.txt','r') as f:
#     lines = f.readlines()


# print(lines)

# with open('file2.txt','w') as f:
#     for line in lines:
#         if line.strip():
#             f.write(line)


# with open('file.txt','r') as f, open('file2.txt','w') as f2:
#     for line in f:
#         # if line.strip():
#         #     f2.write(line)
#         # print(line.strip())
#         print(line)
#         if len(line) > 1:
#             f2.write(line)



#     for i in f:
#         if f.readline().count() == 0:
#             del f.readline()
        
#     print(f)



# --------------------------------------------------


'''5. Reverse the Contents of a File
 Read a file and write its contents in reverse order to another file.
 Test Case:
 Input File:
 scss
 Copy
 Edit
 Line 1
 Line 2
 Line 3
 Output File:
 scss
 Copy
 Edit
 2/8
 Line 3
 Line 2
 Line 1'''

# with open("file.txt","r") as f:
#     line = f.read()


# with open("file2.txt","w") as f2:
#     for i in reversed(line):
#         print(i)
#         f2.write(i)



# ---------------------------------------------------



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
with open("file.txt",'r') as f, open("file2.txt",'w') as f2:
    lines = f.readlines()
    for line in lines:
        clean_line = re.sub('[!\,]','',line)
        f2.writelines(clean_line)



