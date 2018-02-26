import string
# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
csvpath = os.path.join('Resources', 'WebDevelopment.csv')


# # Method 1: Plain Reading of CSVs
#with open(csvpath, 'r') as file_handler:
# lines = file_handler.read()
# print(lines)
# print(type(lines))

# Method 2: Improved Reading using CSV module
title=[]
price=[]
sub=[]
rev=[]
leng=[]
percentile=[]
import csv
with open(csvpath, newline='', encoding="utf8") as csvfile:

     #CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')

	print(csvreader)

    #  Each row is read as a row
	for row in csvreader:
		title.append(row[1])
		price.append(row[4])
		sub.append(row[5])
		rev.append(row[6])
		a,b=row[9].split(" ")
		leng.append(a)
		percentile.append(int(row[6])/int(row[5]))
	
	zipped=zip(title, price, sub, rev, leng, percentile)

output_path = os.path.join('output', 'nudemy.csv')
print(output_path)
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    for i in zipped:
	    csvwriter.writerow(i)
    