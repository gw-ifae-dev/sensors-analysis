import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy.stats import linregress
from astropy.time import Time

# Read file and extract them by columns. 
filename = '/workspaces/sensors-analysis/data/PM_vs_PD_Sensitivity_Final_1.txt'
plt.close('all')

run = pd.read_csv(filename, delimiter ='\t')
print(run)

TimenOk=run.loc[run['Time'].str.len() == 10].index #those are not ok we need to change
run.loc[TimenOk,'Time'] = '0'+run['Time']
tt=run['Date'].str[6:10]+'-'+run['Date'].str[3:5]+'-'+run['Date'].str[0:2]+' '+run['Time'].str[:8]+'.000'
t = Time(list(tt.values), format='iso', scale='utc')
#print(t.gps)


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
   print("The new subdirectory is created!")

#Time series plots
plt.plot(t.gps, run['PowerMeterMeanW'].values, linestyle='None', marker='.', label='PowerMeterMeanW')
plt.ylabel('PowerMeterMeanW')
plt.xlabel('GPSTime (s)')
plt.grid()
plt.savefig(nameDir+'/PowerMeterMeanWvsTime.png')
plt.close()

#Time series plots

plt.plot(t.gps-t.gps[0], run['PowerMeterMeanW'].values, linestyle='None', marker='o', label='PowerMeterMeanW', alpha=0.7)
plt.plot(t.gps-t.gps[0], run['KeithleyMeanV'].values, linestyle='None', marker='.', label='KeithleyMeanV', alpha=0.5)
plt.xlabel('seconds (s)')
#plt.plot(t.gps, run['PowerMeterMeanW'].values, linestyle='None', marker='o', label='PowerMeterMeanW', alpha=0.7)
#plt.plot(t.gps, run['KeithleyMeanV'].values, linestyle='None', marker='.', label='KeithleyMeanV', alpha=0.5)
#plt.xlabel('GPSTime (s)')
plt.legend()
plt.grid()
plt.savefig(nameDir+'/quantitiesvsTimeRun1234.png')
plt.close()

#time series divived by run
Firstrun=[0,1234] #GPSrange []
#t.gps[1234]
Secondrun=[1235,5056]
Thirdrun=[5057,8878]
Fourthrun=[8879,10643]
#nfilters= len(np.unique(run["NDFilter"]))
#Filter1idx=run.loc[run['NDFilter']== 1].index 
#Filter2idx=run.loc[run['NDFilter']== 2].index 
#Filter3idx=run.loc[run['NDFilter']== 3].index 

#Day1F1=run['PowerMeterMeanW'].values[0:1234]

#example to filter only first run & first filter
Run1idxini=0
Run1idxend=1234 #we have to obtain those values from the file
Filter1idxRun1=run.loc[(run['NDFilter']== 1) & (run.index<Run1idxend) & (run.index>Run1idxini)].index 
print(run.loc[Filter1idxRun1].head())
plt.plot(t.gps[Filter1idxRun1]-t.gps[0], run['PowerMeterMeanW'].values[Filter1idxRun1], linestyle='None', marker='o', label='PowerMeterMeanW', alpha=0.7)
plt.plot(t.gps[Filter1idxRun1]-t.gps[0], run['KeithleyMeanV'].values[Filter1idxRun1], linestyle='None', marker='.', label='KeithleyMeanV', alpha=0.5)
plt.xlabel('seconds (s)')
plt.ylabel('Filter1')
plt.legend()
plt.grid()
plt.savefig(nameDir+'/quantitiesvsTimeRun1Filter1.png')
plt.close()


plt.plot(t.gps[0:1234]-t.gps[0], run['PowerMeterMeanW'].values[0:1234], linestyle='None', marker='o', label='PowerMeterMeanW', alpha=0.7)
plt.plot(t.gps[0:1234]-t.gps[0], run['KeithleyMeanV'].values[0:1234], linestyle='None', marker='.', label='KeithleyMeanV', alpha=0.5)
plt.xlabel('seconds (s)')
#plt.plot(t.gps, run['PowerMeterMeanW'].values, linestyle='None', marker='o', label='PowerMeterMeanW', alpha=0.7)
#plt.plot(t.gps, run['KeithleyMeanV'].values, linestyle='None', marker='.', label='KeithleyMeanV', alpha=0.5)
#plt.xlabel('GPSTime (s)')
plt.legend()
plt.grid()
plt.savefig(nameDir+'/quantitiesvsTimeRun1.png')
plt.close()

plt.plot(t.gps[1235:5056]-t.gps[0], run['PowerMeterMeanW'].values[1235:5056], linestyle='None', marker='o', label='PowerMeterMeanW', alpha=0.7)
plt.plot(t.gps[1235:5056]-t.gps[0], run['KeithleyMeanV'].values[1235:5056], linestyle='None', marker='.', label='KeithleyMeanV', alpha=0.5)
plt.xlabel('seconds (s)')
#plt.plot(t.gps, run['PowerMeterMeanW'].values, linestyle='None', marker='o', label='PowerMeterMeanW', alpha=0.7)
#plt.plot(t.gps, run['KeithleyMeanV'].values, linestyle='None', marker='.', label='KeithleyMeanV', alpha=0.5)
#plt.xlabel('GPSTime (s)')
plt.legend()
plt.grid()
plt.savefig(nameDir+'/quantitiesvsTimeRun2.png')
plt.close()

plt.plot(t.gps[5057:8878]-t.gps[0], run['PowerMeterMeanW'].values[5057:8878], linestyle='None', marker='o', label='PowerMeterMeanW', alpha=0.7)
plt.plot(t.gps[5057:8878]-t.gps[0], run['KeithleyMeanV'].values[5057:8878], linestyle='None', marker='.', label='KeithleyMeanV', alpha=0.5)
plt.xlabel('seconds (s)')
#plt.plot(t.gps, run['PowerMeterMeanW'].values, linestyle='None', marker='o', label='PowerMeterMeanW', alpha=0.7)
#plt.plot(t.gps, run['KeithleyMeanV'].values, linestyle='None', marker='.', label='KeithleyMeanV', alpha=0.5)
#plt.xlabel('GPSTime (s)')
plt.legend()
plt.grid()
plt.savefig(nameDir+'/quantitiesvsTimeRun3.png')
plt.close()

plt.plot(t.gps[8879:-1]-t.gps[0], run['PowerMeterMeanW'].values[8879:-1], linestyle='None', marker='o', label='PowerMeterMeanW', alpha=0.7)
plt.plot(t.gps[8879:-1]-t.gps[0], run['KeithleyMeanV'].values[8879:-1], linestyle='None', marker='.', label='KeithleyMeanV', alpha=0.5)
plt.xlabel('seconds (s)')
#plt.plot(t.gps, run['PowerMeterMeanW'].values, linestyle='None', marker='o', label='PowerMeterMeanW', alpha=0.7)
#plt.plot(t.gps, run['KeithleyMeanV'].values, linestyle='None', marker='.', label='KeithleyMeanV', alpha=0.5)
#plt.xlabel('GPSTime (s)')
plt.legend()
plt.grid()
plt.savefig(nameDir+'/quantitiesvsTimeRun4.png')
plt.close()



plt.plot(t.gps, run['PowerMeterStdW'].values, linestyle='None', marker='o', label='PowerMeterStdW', alpha=0.7)
plt.plot(t.gps, run['KeithleyStdV'].values, linestyle='None', marker='.', label='KeithleyStdV', alpha=0.5)
plt.legend()
plt.xlabel('GPSTime (s)')
plt.grid()
plt.savefig(nameDir+'/StDquantitiesvsTime.png')
plt.close()





#analysis by Filters
filters = 3
nfilters= len(np.unique(run["NDFilter"]))

for i in range(nfilters):
   NDF=run.loc[run['NDFilter'] == i+1]
   x=NDF['KeithleyMeanV'].values
   y=NDF['PowerMeterMeanW'].values
   res = linregress(x, y)
   NDF.plot(kind='scatter', figsize=(8, 8), x='KeithleyMeanV', y='PowerMeterMeanW', s=3, c='green')
   plt.plot(x, res.intercept + res.slope*x, 'r', label=str(round(res.intercept,2))+ str(round(res.slope,2))+'x')
   plt.legend()
   plt.grid()
   plt.savefig(nameDir+'/Mean_NDF'+str(i+1)+'.png')
   plt.close()
   ################### Residuals ###################
   fig, axes0 = plt.subplots()
   plt.plot(x, ((res.intercept + res.slope*x)-y)/y, marker ='.', linestyle = 'None', label='(yfit-y)/y')
   axes0.set_yscale('log')
   plt.grid()
   plt.xlabel('KeithleyMeanV')
   plt.ylabel('PowerMeterMeanW residuals')
   plt.savefig(nameDir+'/Residuals_NDF'+str(i+1)+'.png')
   plt.close()
   ################### StdW vs. StdV ###################
   NDF.plot(kind='scatter', figsize=(8, 8), x='KeithleyStdV', y='PowerMeterStdW', s=3, c='green')
   plt.grid()
   plt.savefig(nameDir+'/Std_NDF'+str(i+1)+'.png')
   plt.close()
   ################### MeanW histogram per ND ###################
   NDF.hist(column='PowerMeterMeanW', bins=40, grid=True, figsize=(12,8), color='green', zorder=2, rwidth=0.9, alpha = 0.7)
   plt.grid()
   plt.savefig(nameDir+'/hNDF'+str(i+1)+'_PowerMeterMeanW.png')
   plt.close()
   ################### StdW vs. V ###################
   run.plot(kind='scatter', figsize=(8, 8), x='KeithleyMeanV', y='PowerMeterStdW', s=3, c='green')
   plt.grid()
   plt.savefig(nameDir+'/StdW_MeanV_NDF123.png')
   plt.close()
   
################### MeanW histogram per ND ###################
#NDF1.hist(column='PowerMeterMeanW', bins=10, grid=True, figsize=(12,8), color='green', zorder=2, rwidth=0.9, alpha = 0.7)
#plt.savefig(nameDir+'/hNDF1_PowerMeterMeanW.png')
#NDF2.hist(column='PowerMeterMeanW', bins=10, grid=True, figsize=(12,8), color='green', zorder=2, rwidth=0.9, alpha = 0.7)
#plt.savefig(nameDir+'/hNDF2_PowerMeterMeanW.png')
#NDF3.hist(column='PowerMeterMeanW', bins=10, grid=True, figsize=(12,8), color='green', zorder=2, rwidth=0.9, alpha = 0.7)
#plt.savefig(nameDir+'/hNDF3_PowerMeterMeanW.png')

################### More histograms ###################
NDF1=run.loc[run['NDFilter'] == 1]
NDF2=run.loc[run['NDFilter'] == 2]
NDF3=run.loc[run['NDFilter'] == 3]

#fig, axes = plt.subplots()
#NDF1.hist(ax=axes, column='PowerMeterMeanW', bins=100, grid=True, figsize=(12,8), color='green', zorder=2, rwidth=0.9, alpha = 0.7)
#NDF2.hist(ax=axes, column='PowerMeterMeanW', bins=100, grid=True, figsize=(12,8), color='blue', zorder=2, rwidth=0.9, alpha = 0.5)
#NDF3.hist(ax=axes, column='PowerMeterMeanW', bins=100, grid=True, figsize=(12,8), color='magenta', zorder=2, rwidth=0.9, alpha = 0.3)
#axes.gca().set_xscale('log')
#plt.savefig(nameDir+'/h123.png')
#plt.close()


NDF1PMMW=NDF1["PowerMeterMeanW"]
NDF2PMMW=NDF2["PowerMeterMeanW"]
NDF3PMMW=NDF3["PowerMeterMeanW"]
#bins1=np.arange(min(NDF1PMMW), max(NDF1PMMW) + 10**-8, 10**-8)
#bins2=np.arange(min(NDF2PMMW), max(NDF2PMMW) + 10**-6, 10**-6)
#bins3=np.arange(min(NDF3PMMW), max(NDF3PMMW) + 10**-4, 10**-4)
fig, ax = plt.subplots()

plt.hist(NDF1PMMW, bins=np.logspace(np.log10(1e-10),np.log10(10), 100), color='green', alpha = 0.7)
plt.hist(NDF2PMMW, bins=np.logspace(np.log10(1e-10),np.log10(10), 100), color='blue', alpha = 0.7)
plt.hist(NDF3PMMW, bins=np.logspace(np.log10(1e-10),np.log10(10), 100), color='magenta', alpha = 0.7)
plt.grid()
#plt.gca().set_xscale("log")
#plt.show()

#plt.hist(NDF1PMMW, bins1,color='green', alpha = 0.7)
#plt.hist(NDF2PMMW, bins2, color='blue', alpha = 0.5)
#plt.hist(NDF3PMMW, bins3, color='magenta',alpha = 0.3)
#plt.ylim(0,200)
plt.xscale('log')
plt.yscale('log')
plt.savefig(nameDir+'/h123pmm.png')
plt.close()


PowerMeterStdW=run["PowerMeterStdW"]
bins=np.arange(min(PowerMeterStdW), max(PowerMeterStdW) + 10**-6, 10**-6)
fig, ax = plt.subplots()
plt.hist(PowerMeterStdW, bins)
#plt.ylim(0,200)
plt.yscale('log')
plt.grid()
plt.savefig(nameDir+'/h2.png')
plt.close()

#fig, ax = plt.subplots()
#ax = run.hist(column='PowerMeterStdW', bins=10, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
#plt.savefig(nameDir+'/h2.png')

KeithleyMeanV=run["KeithleyMeanV"]
#bins=np.arange(min(KeithleyMeanV), max(KeithleyMeanV) + 10**-4, 10**-4)
fig, ax = plt.subplots()
#n, bins, patches=plt.hist(KeithleyMeanV, bins)
#print(max(KeithleyMeanV)), print(min(KeithleyMeanV))
plt.hist(KeithleyMeanV, bins=np.logspace(np.log10(1e-7),np.log10(1e-3), 100), color='green', alpha = 0.7)
#print(max(n))
#plt.ylim(0,10000)
plt.xscale('log')
plt.grid()
plt.xlabel('KeithleyMeanV')
plt.savefig(nameDir+'/h3.png')
plt.close()

#ax = run.hist(column='KeithleyMeanV', bins=10, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
#plt.savefig(nameDir+'/h3.png')

KeithleyStdV=run["KeithleyStdV"]
bins=np.arange(min(KeithleyStdV), max(KeithleyStdV) + 10**-6, 10**-6)
fig, ax = plt.subplots()
n, bins, patches=plt.hist(KeithleyStdV, bins)
plt.ylim(0,2000)
#plt.yscale('log')
plt.grid()
plt.savefig(nameDir+'/h4.png')
plt.close()

ax = run.hist(column='PowerSetpointmW', bins=10, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
plt.savefig(nameDir+'/h5.png')
ax = run.hist(column='LaserDisplaymW', bins=10, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
plt.savefig(nameDir+'/h6.png') 
plt.close()

plt.close('all')