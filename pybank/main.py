import string
import os
import csv
csvpath = os.path.join('Resources', 'budget_data_1.csv')

def getAnalysis(months,revenue):
    
    # Total months
	totalmonths = len(revenue)

    # Total Revenue
	totalrevenue=sum(revenue)

    # Average Change in revenue
	changes=[]
	for i in range(0,len(revenue)-1):
		changes.append(revenue[i+1]-revenue[i])
	averagechange=sum(changes)/len(changes)

    # Greatest Increase in Revenue
	greatestincrease=max(changes)
	greatestincreasemonth=months[changes.index(greatestincrease)+1]
	
	# Greatest Decrease in Revenue
	greatestdecrease=min(changes)
	greatestdecreasemonth=months[changes.index(greatestdecrease)+1]
    # Print out the analysis
	print("Financial Analysis")
	print("----------------------------")
	print("Total Months: " + str(totalmonths))
	print("Total Revenue: " + str(totalrevenue))
	print("Average Revenue Change: " + '${:}'.format(str(averagechange)))
	print("Greatest Increase in Revenue: " + str(greatestincreasemonth)+" " +str(greatestincrease))
	print("Greatest Decrease in Revenue: " + str(greatestdecreasemonth)+" " + str(greatestdecrease))
	text_file = open("Output.txt", "w")
	text_file.write("Financial Analysis"+'\n')
	text_file.write("---------------------------- \n")
	text_file.write("Total Months: " + str(totalmonths)+'\n')
	text_file.write("Total Revenue: " + str(totalrevenue)+'\n')
	text_file.write("Average Revenue Change: " + '${:}'.format(str(averagechange))+'\n')
	text_file.write("Greatest Increase in Revenue: " + str(greatestincreasemonth)+" " +'${:}'.format(str(greatestincrease))+'\n')
	text_file.write("Greatest Decrease in Revenue: " + str(greatestdecreasemonth)+" " +'${:}'.format(str(greatestdecrease))+'\n')
	text_file.close()




# # Method 1: Plain Reading of CSVs
#with open(csvpath, 'r') as file_handler:
# lines = file_handler.read()
# print(lines)
# print(type(lines))

# Method 2: Improved Reading using CSV module
months=[]
revenue=[]
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
		months.append(row[0])
		revenue.append(int(row[1]))

getAnalysis(months,revenue)

