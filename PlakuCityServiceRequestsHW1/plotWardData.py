import matplotlib.pyplot as plt

with open('wardData.txt') as f:
    lines = f.readlines()
    wardNum = [int(line.split()[0]) for line in lines]
    amountReq = [int(line.split()[1]) for line in lines]

plt.bar(wardNum, amountReq, align = 'center', alpha = 0.5)
plt.xlabel('Ward Number')
plt.ylabel('Amount of Service Requests')

plt.title('Service Requests Handled in Each Ward')
plt.show()
