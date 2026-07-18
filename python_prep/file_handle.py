

# file = open('/home/abhishek/projects/python_prep/data/file1.txt','a')
# file.write("This is a new line added to the file.\n")
# file.close()

# file = open('/home/abhishek/projects/python_prep/data/file1.txt','r')
# #file.write("This is a new line added to the file.\n")
# content =file.read()
# print(content)

# try:
#     with open('data/file1.txt','r') as file:
#         content = file.readlines()
#         print(content)
# finally:
#     file.close()

import csv

file = open('/data/sales_data_sample.csv',mode='r')
reader = csv.reader(file)