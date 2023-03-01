import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#def NicePlots(data):
#    data.T.plot(kind='scatter', x='Time', y='PowerSetpointmW', s=35, c='green')



# Read file and extract them by columns. 
filename = '/workspaces/codespaces-jupyter/data/PM_vs_PD_Sensitivity_Final_1.txt'
name = filename.split('/')[-1].split('.')[0]
run = pd.read_csv(filename, delimiter ='\t')
print(run)
# Add an index so that it is easy to be parsed when we do a time-fluction study
run.plot(kind='scatter', x='KeithleyMeanV', y='PowerMeterMeanW', s=35, c='green')

isExist = os.path.exists(path)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(path)
   print("The new directory is created!")

plt.savefig(name+'/1.png')

# Do 2D plot of laser power vs. voltage (histograms of each variable)
# NicePlots(run)

# Compute residuals 
