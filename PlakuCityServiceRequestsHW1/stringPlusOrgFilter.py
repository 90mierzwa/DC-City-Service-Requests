import pandas as pd
import csv
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0

f = open('Plaku_City_Service_Requests_in_2018.csv')
csv_f = csv.reader(f)

for row in csv_f:
    if row[4] == 'Bulk Collection' and row[6] == 'DPW':
        count0 = count0 + 1
    elif row[4] == 'Emergency No-Parking Verification' and row[6] == 'DPW':
        count1 = count1 + 1
    elif row[4] == 'Illegal Dumping':
        count2 = count2 + 1
    elif row[4] == 'Parking Enforcement' and row[6] == 'DPW':
        count3 = count3 + 1
    elif row[4] == 'Residential Parking Permit Violation' and row[6] == 'DPW':
        count4 = count4 + 1
    elif row[4] == 'Sanitation Enforcement' and row[6] == 'DPW':
        count5 = count5 + 1
    elif row[4] == 'Trash Collection - Missed' and row[6] == 'DPW':
        count6 = count6 + 1
    else:
        count7 = count7 + 1


print(count0)
print(count1)
print(count2)
print(count3)
print(count4)
print(count5)
print(count6)
print(count7)
