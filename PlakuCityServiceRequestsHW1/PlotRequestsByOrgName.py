# Plotting requests by organization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x_coord = pd.read_csv('Plaku_City_Service_Requests_in_2018.csv', usecols = [0])
y_coord = pd.read_csv('Plaku_City_Service_Requests_in_2018.csv', usecols = [1])

# Read data in
data = pd.read_csv('Plaku_City_Service_Requests_in_2018.csv')

# Array of all requests handled by DMV
orgDMV = data[data['ORGANIZATIONACRONYM'] == "DMV"]

# Prints all requests handled by DMV
print orgDMV
