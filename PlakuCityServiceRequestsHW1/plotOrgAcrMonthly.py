import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

with open('orgAcrMonthlydata.txt') as f:
    lines = f.readlines()
    month = [int(line.split()[0]) for line in lines]
    amountReqDDOT = [int(line.split()[1]) for line in lines]
    amountReqDPW = [int(line.split()[2]) for line in lines]

plt.plot(month, amountReqDPW, '-o', markersize = 6, label = "DPW")
plt.plot(month, amountReqDDOT, '-o', markersize = 6, label = "DDOT")

xticks = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
plt.xticks(month, xticks)

plt.title('Service Requests by Month')
plt.xlabel('Month')
plt.ylabel('Amount of Service Requests')
plt.legend(bbox_to_anchor = (0.81, .97), loc = 2, borderaxespad = 0.)
plt.grid()
plt.show()
