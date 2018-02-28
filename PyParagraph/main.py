import csv
import re
# It is a good idea to store the filename into a variable.
# The variable can later become a function argument when the
# code is converted to a function body.
filename = 'paragraph_1.txt'

# Using the newer with construct to close the file automatically.
with open(filename) as f:
	data = f.readlines()
	reader = csv.reader(data, delimiter=' ')
	wordcounter=0
	sentencecounter=0
	totalwordlength=0
	for i in reader:
		for j in i:
			wordcounter+=1
			if '.' in j:
				sentencecounter+=1
			totalwordlength=totalwordlength+len(j)
	print("Paragraph Analysis")
	print("-----------------")
	print("Approximate Word Count: " + str(wordcounter))
	print("Approximate Sentence Count: " + str(sentencecounter))
	print("Average Letter Count: " + str(totalwordlength/wordcounter))
	print("Average Sentence Length: " + str(wordcounter/sentencecounter))

# You can later iterate through the list for other purpose, for
# example to read them via the csv.reader.



