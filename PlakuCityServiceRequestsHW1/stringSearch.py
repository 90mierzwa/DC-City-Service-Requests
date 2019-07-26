import csv

f = open('Plaku_City_Service_Requests_in_2018.csv')
csv_f = csv.reader(f)

userString = raw_input("Enter string to be searched for: ")
type(userString)

i = input("Enter the column number you would like to search: ")
type(i)

count = 0
for row in csv_f:
    if row[i] == userString :
        count = count + 1

print userString, " appeared in ", count, " requests in column number ", i

# Append data to text file
with open('serviceCodeData.txt', 'a') as f:
    f.write('%s' % userString + " ")
    f.write('%d' % count + " \n")
