import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#def NicePlots(data):
#    data.T.plot(kind='scatter', x='Time', y='PowerSetpointmW', s=35, c='green')



# Read file and extract them by columns. 
filename = '/workspaces/codespaces-jupyter/data/PM_vs_PD_Sensitivity_Final_1.txt'
nameDir = filename.split('/')[-1].split('.')[0]
run = pd.read_csv(filename, delimiter ='\t')
print(run)
# Add an index so that it is easy to be parsed when we do a time-fluction study

isExist = os.path.exists(nameDir)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(nameDir)
   print("The new directory is created!")

run.plot(kind='scatter', x='KeithleyMeanV', y='PowerMeterMeanW', s=3, c='green')
plt.savefig(nameDir+'/1.png')

# Do 2D plot of laser power vs. voltage (histograms of each variable)
# NicePlots(run)

# Compute residuals 
