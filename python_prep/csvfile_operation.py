import csv

# with open('/home/abhishek/projects/python_prep/data/sample.csv','r') as csvfile:
#     reader =csv.reader(csvfile)
#     for row in reader:
#         print(row)

# with open('/home/abhishek/projects/python_prep/data/sample.csv','r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['ORDERNUMBER'],row['QUANTITYORDERED'],row['PRICEEACH'])


# with open('/home/abhishek/projects/python_prep/data/output.csv','w',newline='') as csvfile:
#     wrt = csv.writer(csvfile)
#     wrt.writerow(['name','age','city'])
#     wrt.writerow(['abhishek',25,'delhi'])

with open('/home/abhishek/projects/python_prep/data/output.csv','w',newline='') as csvfile:
    wrter =csv.DictWriter(csvfile,fieldnames=['name','age'])
    wrter.writeheader()
    wrter.writerow({'name':'abhishek','age':25})