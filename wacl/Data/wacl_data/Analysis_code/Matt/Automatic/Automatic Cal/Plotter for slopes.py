import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import numpy as np
from datetime import datetime

def timeconverter(T):

   	return (datetime.strptime(T,"%Y-%m-%d %H:%M:%S.%f"))

humid_correct = 'Y'


path = 'C:\Users\mat_e_000\Google Drive\Bursary\Data_Analysis'
filename = '\Slopes'
filenamec = '\Slopes Corrected'

dataS = pd.read_csv(path+'\\'+filename+'.txt',sep='\t')

for i in xrange(0,len(dataS['The Time'])):
    if str(dataS['The Time'][i])[-3:] == '999':
        dataS.loc[i,'The Time'] = dataS.loc[i,'The Time'][:-3]


for x in xrange(0,len(dataS)):
    dataS.loc[x,'The Time'] = timeconverter(dataS.loc[x,'The Time'])



if humid_correct == 'Y':
    dataSc = pd.read_csv(path+'\\'+filenamec+'.txt',sep='\t')

for i in xrange(0,len(dataSc['The Time'])):
    if str(dataSc['The Time'][i])[-3:] == '999':
        dataSc.loc[i,'The Time'] = dataSc.loc[i,'The Time'][:-3]
        
for x in xrange(0,len(dataSc)):
    dataSc.loc[x,'The Time'] = timeconverter(dataSc.loc[x,'The Time'])    
        
    
try:
    Slope3_mean = np.nanmean(dataS['Slope 3'][5:])
except:
    pass
    
try:
    Slope4_mean = np.nanmean(dataS['Slope 4'][5:])
except:
    pass
    
try:
    Slope5_mean = np.nanmean(dataS['Slope 5'][5:])
except:
    pass
if humid_correct == 'Y':
    Slope3c_mean = np.nanmean(dataSc['Slope 3'][5:])
    Slope4c_mean = np.nanmean(dataSc['Slope 4'][5:])
    Slope5c_mean = np.nanmean(dataSc['Slope 5'][5:])


fig1 = plt.figure()
plt.title('Raw')
ax1a = fig1.add_subplot(311)
ax1b = fig1.add_subplot(312)
ax1c = fig1.add_subplot(313)

ax1a.errorbar(date2num(dataS['The Time']),dataS['Slope 3'], xerr = 0, yerr = dataS['Slope Error 3'], fmt='bo')
ax1a.axhline(Slope3_mean)


ax1b.errorbar(date2num(dataS['The Time']),dataS['Slope 4'], xerr = 0, yerr = dataS['Slope Error 4'], fmt='ko')
ax1b.axhline(Slope4_mean)


ax1c.errorbar(date2num(dataS['The Time']),dataS['Slope 5'], xerr = 0, yerr = dataS['Slope Error 5'], fmt='mo')
ax1c.axhline(Slope5_mean)


if humid_correct == 'Y':
    fig2 = plt.figure()
    plt.title('Corrected')
    ax2a = fig2.add_subplot(311)
    ax2b = fig2.add_subplot(312)
    ax2c = fig2.add_subplot(313)
    
    ax2a.errorbar(date2num(dataSc['The Time']),dataSc['Slope 3'], xerr = 0, yerr = dataSc['Slope Error 3'], fmt='bo')
    ax2a.axhline(Slope3c_mean)
    
    ax2b.errorbar(date2num(dataSc['The Time']),dataSc['Slope 4'], xerr = 0, yerr = dataSc['Slope Error 4'], fmt='ko')
    ax2b.axhline(Slope4c_mean)
    
    ax2c.errorbar(date2num(dataSc['The Time']),dataSc['Slope 5'], xerr = 0, yerr = dataSc['Slope Error 5'], fmt='mo')
    ax2c.axhline(Slope5c_mean)
    
#    ax1a.set_ylim([-0.0001,0.00015])
#    ax2a.set_ylim([-0.0001,0.00015])
    
#    ax1b.set_ylim([-0.00001,0.00018])
#    ax2b.set_ylim([-0.00001,0.00018])
    
#    ax1c.set_ylim([0,0.00018])
#    ax2c.set_ylim([0,0.00018])

plt.show()
