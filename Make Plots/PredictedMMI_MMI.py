#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:04:07 2020

@author: EmmaDevin
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

socaldata = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/SoCal_withMMIpred.csv')

D= np.linspace(0,1000,1000)
R = np.sqrt(D**2 + 14**2)
B = []
for i in range(len(R)):
    b = np.max(np.linspace(0,np.log10(R[i]/50), 500))
    B.append(b)
B = np.array(B)


       
# constants from table 1 Atinson et al.
c = [0,0.309,1.864,-1.672,-0.00219,1.77,-0.383]
    
# compute the MMI predicted

fs = 12

mag = socaldata['EarthquakeMagnitude']
intMag = mag.astype(int)


soCal_byMag_9 = socaldata[intMag == 9]
soCal_byMag_8 = socaldata[intMag == 8]
soCal_byMag_7 = socaldata[intMag == 7]   
soCal_byMag_6 = socaldata[intMag == 6]
soCal_byMag_5 = socaldata[intMag == 5]
soCal_byMag_4 = socaldata[intMag == 4]
soCal_byMag_3 = socaldata[intMag == 3]
soCal_byMag_2 = socaldata[intMag == 2]
soCal_byMag_1 = socaldata[intMag == 1]

fig = plt.figure(figsize=(10, 5))
# fig.suptitle('Predicted and Empirical MMI vs Distance', fontsize = 25)

plt.subplot(121)
M = 6
MMIp = c[1]+c[2]*M+c[3]*np.log10(R)+c[4]*R+c[5]*B+c[6]*M*np.log10(R)
plt.plot(D,MMIp,lw=1,c='r', label='Predicted MMI, M6')
plt.scatter(soCal_byMag_6['HypocentralDistance'],soCal_byMag_6['MMI'], s=10,edgecolors='grey',facecolors='none', label='MMI from GM, M6-M7')
plt.xlabel('Distance (km)', fontsize = fs)
plt.ylabel('MMI', fontsize = fs)
plt.xscale('log')
plt.ylim(1,10)
plt.xlim(1e0,1e3)
plt.legend(fontsize = fs)
# plt.title('MMI Predicted/MMI vs Distance for Magnitude 6', fontsize = 20)
#plt.savefig('/Users/emmadevin/Work/USGS Work/USGS PLUM/PDF Plots/PredMMIMMI7.pdf') 

plt.subplot(122)
M = 4
MMIp = c[1]+c[2]*M+c[3]*np.log10(R)+c[4]*R+c[5]*B+c[6]*M*np.log10(R)
plt.plot(D,MMIp,lw=1,c='r', label='Predicted MMI, M4')
plt.scatter(soCal_byMag_4['HypocentralDistance'],soCal_byMag_4['MMI'], s=10,edgecolors='grey',facecolors='none', label='MMI from GM, M4-M5')
plt.xlabel('Distance (km)', fontsize = fs)
plt.ylabel('MMI', fontsize = fs)
plt.xscale('log')
plt.ylim(1,10)
plt.xlim(1e0,1e3)
plt.legend(fontsize = fs)
# plt.title('MMI Predicted/MMI vs Distance for Magnitude 4', fontsize = 20)
plt.savefig('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/FinalPlots/PredMMIMMI.pdf') 
