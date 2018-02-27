import string
import os
import csv
csvpath = os.path.join('election_data_1.csv')

def getAnalysis(candidates):
    
    # Total votes
	totalvotes = len(candidates)

    # Candidates Names
	CandidateNames=[]
	for i in candidates:
		if i not in CandidateNames:
			CandidateNames.append(i)

    # Votes for each Candidates
	votesbycandidate=[]
	for i in CandidateNames:
		counter=0
		for j in candidates:
			if i==j:
				counter+=1
		votesbycandidate.append(counter)
	print("Election Results")
	print("----------------------------")
	print("Total Votes: " + str(totalvotes))
	print("----------------------------")
	for i in range(len(CandidateNames)):
		print(str(CandidateNames[i]) + ": " + str("{0:.0f}%".format((votesbycandidate[i]/totalvotes*100)))+ " (" + str(votesbycandidate[i]) + ")")
	print("----------------------------")
	print("Winner: " + str(CandidateNames[votesbycandidate.index(max(votesbycandidate))]))

	text_file = open("Output.txt", "w")
	text_file.write("Election Results"+'\n')
	text_file.write("---------------------------- \n")
	text_file.write("Total Votes: " + str(totalvotes)+'\n')
	text_file.write("---------------------------- \n")
	for i in range(len(CandidateNames)):
		text_file.write(str(CandidateNames[i]) + ": " + str("{0:.0f}%".format((votesbycandidate[i]/totalvotes*100)))+ " (" + str(votesbycandidate[i]) + ") \n")
	text_file.write("---------------------------- \n")
	text_file.write("Winner: " + str(CandidateNames[votesbycandidate.index(max(votesbycandidate))]))
	text_file.close()

candidate=[]
with open(csvpath, newline='', encoding="utf8") as csvfile:

     #CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')

	print(csvreader)

    #  Each row is read as a row
	firstline = True
	for row in csvreader:
		if firstline:    #skip first line
			firstline = False
			continue
		candidate.append(row[2])

getAnalysis(candidate)
