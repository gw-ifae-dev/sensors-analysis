import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress

# Read file and extract them by columns. 
filename = '/workspaces/codespaces-jupyter/data/PM_vs_PD_Sensitivity_Final_1.txt'

run = pd.read_csv(filename, delimiter ='\t')
print(run)
# Add an index so that it is easy to be parsed when we do a time-fluction study
plotsDir='Plots/'
isExist = os.path.exists(plotsDir)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(plotsDir)
   print("The new directory is created!")

nameDir = plotsDir+filename.split('/')[-1].split('.')[0]
isExist = os.path.exists(nameDir)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(nameDir)
   print("The new directory is created!")

# Subsets of filters
NDF1=run.loc[run['NDFilter'] == 1]
NDF2=run.loc[run['NDFilter'] == 2]
NDF3=run.loc[run['NDFilter'] == 3]



NDF1.plot(kind='scatter', figsize=(8, 8), x='KeithleyMeanV', y='PowerMeterMeanW', s=3, c='green')
#from sklearn.linear_model import LinearRegression
#linear_regressor = LinearRegression()  # create object for the class
#linear_regressor.fit(run.loc, Y)  # perform linear regression

x=run['KeithleyMeanV'].values
#print(x)
#type(x)
y=run['PowerMeterMeanW'].values
result = linregress(x, y)


plt.savefig(nameDir+'/Mean_NDF1.png')
NDF2.plot(kind='scatter', figsize=(8, 8), x='KeithleyMeanV', y='PowerMeterMeanW', s=3, c='blue')
plt.savefig(nameDir+'/Mean_NDF2.png')
NDF3.plot(kind='scatter', figsize=(8, 8), x='KeithleyMeanV', y='PowerMeterMeanW', s=3, c='magenta')
plt.savefig(nameDir+'/Mean_NDF3.png')
#plt.show()

run.plot(kind='scatter', figsize=(8, 8), x='KeithleyMeanV', y='PowerMeterStdW', s=3, c='green')
plt.savefig(nameDir+'/StdW_MeanV_NDF123.png')

#fig, axes0 = plt.subplots()
NDF1.plot(kind='scatter', figsize=(8, 8), x='KeithleyStdV', y='PowerMeterStdW', s=3, c='green')
plt.savefig(nameDir+'/Std_NDF1.png')
NDF2.plot(kind='scatter', figsize=(8, 8), x='KeithleyStdV', y='PowerMeterStdW', s=3, c='blue')
plt.savefig(nameDir+'/Std_NDF2.png')
NDF3.plot(kind='scatter', figsize=(8, 8), x='KeithleyStdV', y='PowerMeterStdW', s=3, c='magenta')
plt.savefig(nameDir+'/Std_NDF3.png')



NDF1.hist(column='PowerMeterMeanW', bins=10, grid=True, figsize=(12,8), color='green', zorder=2, rwidth=0.9, alpha = 0.7)
plt.savefig(nameDir+'/hNDF1_PowerMeterMeanW.png')
NDF2.hist(column='PowerMeterMeanW', bins=10, grid=True, figsize=(12,8), color='green', zorder=2, rwidth=0.9, alpha = 0.7)
plt.savefig(nameDir+'/hNDF2_PowerMeterMeanW.png')
NDF3.hist(column='PowerMeterMeanW', bins=10, grid=True, figsize=(12,8), color='green', zorder=2, rwidth=0.9, alpha = 0.7)
plt.savefig(nameDir+'/hNDF3_PowerMeterMeanW.png')


# Histograms of all variables
#df['my_column'].plot(kind='hist', logx=True)
fig, axes = plt.subplots()
NDF1.hist(ax=axes, column='PowerMeterMeanW', bins=10, grid=True, figsize=(12,8), color='green', zorder=2, rwidth=0.9, alpha = 0.7)
NDF2.hist(ax=axes, column='PowerMeterMeanW', bins=100, grid=True, figsize=(12,8), color='blue', zorder=2, rwidth=0.9, alpha = 0.5)
NDF3.hist(ax=axes, column='PowerMeterMeanW', bins=100, grid=True, figsize=(12,8), color='magenta', zorder=2, rwidth=0.9, alpha = 0.3)
axes.set_xscale('log')
plt.savefig(nameDir+'/h123.png')

ax = run.hist(column='PowerMeterStdW', bins=10, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
plt.savefig(nameDir+'/h2.png')

ax = run.hist(column='KeithleyMeanV', bins=10, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
plt.savefig(nameDir+'/h3.png')

ax = run.hist(column='KeithleyStdV', bins=10, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
plt.savefig(nameDir+'/h4.png')

ax = run.hist(column='PowerSetpointmW', bins=10, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
plt.savefig(nameDir+'/h5.png')

ax = run.hist(column='LaserDisplaymW', bins=10, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
plt.savefig(nameDir+'/h6.png') 







# Do 2D plot of laser power vs. voltage (histograms of each variable)
# NicePlots(run)

# Compute residuals 
