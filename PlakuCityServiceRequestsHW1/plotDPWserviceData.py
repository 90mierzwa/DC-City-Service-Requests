import matplotlib.pyplot as plt

with open('DPWserviceData.txt') as f:
    lines = f.readlines()
    DPWservice = [int(line.split()[1]) for line in lines]

labels = 'Bulk Collection', 'Emergency No-Parking Verification', 'Illegal Dumping', 'Parking Enforcement', 'Residential Parking Permit Violation', 'Sanitation Enforcement', 'Trash Collection Missed'

plt.pie(DPWservice, labels = labels, autopct = '%1.1f%%')
plt.title('Service Requests Handled By DPW')
plt.axis('equal')
plt.tight_layout()
plt.show()
