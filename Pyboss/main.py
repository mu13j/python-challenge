import string
import os
import csv
csvpath = os.path.join('employee_data1.csv')
output_path = os.path.join('ConvertedData.csv')

EMPID=[]
Name=[]
DOB=[]
SSN=[]
State=[]
with open(csvpath, newline='', encoding="utf8") as csvfile:

     #CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')

	print(csvreader)

    #  Each row is read as a row
	firstline = True
	for row in csvreader:
		EMPID.append(row[0])
		Name.append(row[1])
		DOB.append(row[2])
		SSN.append(row[3])
		State.append(row[4])
#Changes Names
firstname=['First Name']
lastname=['Last Name']
for i in Name[1:]:
	a,b = i.split(" ")
	firstname.append(a)
	lastname.append(b)
	
#Changes Date of Birth
FixedDOB=['DOB']
for i in DOB[1:]:
	a=(i[5:7]+"/"+i[8:]+"/"+i[0:4])
	FixedDOB.append(a)

#Changes SSN
FixedSSN=['SSN']
for i in SSN[1:]:
	a="***-**-"
	a=a+(i[-4:])
	FixedSSN.append(a)

#Changes State
FixedState=['State']
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
for i in State[1:]:
	FixedState.append(us_state_abbrev[i])

Zipped=zip(EMPID, firstname, lastname, FixedDOB, FixedSSN, FixedState)



with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
	csvwriter = csv.writer(csvfile, delimiter=',')
	# Write the first row (column headers)
	for i in range(len(EMPID)):
		csvwriter.writerow([EMPID[i],firstname[i],lastname[i],FixedDOB[i],FixedSSN[i],FixedState[i]])