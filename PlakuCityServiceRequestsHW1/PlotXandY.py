# Columns A and B from excel spreadsheet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x_coord = pd.read_csv('Plaku_City_Service_Requests_in_2018.csv', usecols = [0])
y_coord = pd.read_csv('Plaku_City_Service_Requests_in_2018.csv', usecols = [1])
#x_coord = np.squeeze(np.array(x_coord))
#y_coord = np.squeeze(np.array(y_coord))

plt.xlabel('X Coordinate of Service Request Location')
plt.ylabel('Y Coordinate of Service Request Location')
plt.title('Location of Service Request')
plt.scatter(x_coord, y_coord)
plt.show()
