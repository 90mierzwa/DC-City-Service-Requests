import matplotlib.pyplot as plt

with open('wardData.txt') as f:
    lines = f.readlines()
    wardNum = [int(line.split()[0]) for line in lines]
    wardPop = [int(line.split()[2]) for line in lines]

plt.bar(wardNum, wardPop, color = (0.5, 0.1, 0.2, 0.6), align = 'center', alpha = 0.5)
plt.xlabel('Ward Number')
plt.ylabel('Total Population')

plt.title('Population of Each Ward')
plt.show()
