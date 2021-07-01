#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:59:05 2020

@author: EmmaDevin
"""


import conversion as c
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



soCal_data = pd.read_csv('/Users/EmmaDevin/USGS PLUM/Data/SoCal_EQ_Data_for_Emma.csv')

PGa = soCal_data['PGA_g']
PGa = PGa.replace(-999, None)
pga = PGa/9.8*100
pgv = soCal_data['PGV_cms2']
M = soCal_data['EarthquakeMagnitude']
H = soCal_data['HypocentralDistance']*100*1000

aT2 = 4.22
vT2 = 4.56


MMi=[]


for i in range(len(pga)):
#for i in range(1):
    mma1, mma2, mmv1, mmv2 = c.getMMI(pga[i],pgv[i], M[i], H[i])

    if (mma1<= aT2):
        MMA = (mma1)
    elif (mma2>aT2):
        MMA = (mma2)

    if (mmv1<= vT2):
        MMV = (mmv1)
    elif (mmv2>vT2):
        MMV = (mmv2)
        
    mmi = 0.46*MMA + 0.52*MMV
    
    MMi.append(mmi)
    
    
    
soCal_data['MMI']= MMi


logPGA = np.log10(pga)
logPGV = np.log10(pgv)

plt.scatter(logPGA, MMi, s = 5, c = 'm', label ='Y = PGA')
plt.scatter(logPGV, MMi, s = 5, c ='c', label = 'Y = PGV')
plt.title('MMI vs log(Y)')

#plt.scatter(logPGA[lessThanA], mma1[lessThanA], s= 5, c = 'springgreen', label= 'MMA 1')
#plt.scatter(logPGA[greaterThanA], mma2[greaterThanA], s =5, c = 'm', label= 'MMA 2')
#plt.scatter(logPGA[~lessThanA], mma2[~lessThanA], s =5, c = 'm', label= 'MMA 2')

#plt.scatter(logPGA, mma1, s= 5, c = 'springgreen', label= 'MMA 1')
#plt.scatter(logPGA, mma2, s =5, c = 'm', label= 'MMA 2')

#plt.scatter(logPGA, mmv1, s= 5, c = 'dodgerblue', label= 'MMV 1')
#plt.scatter(logPGA, mmv2, s =5, c = 'red', label= 'MMV 2')

#plt.scatter(logPGA, MMI1)

#plt.xscale('log')

plt.xlim(-5,3)
plt.ylim(0,10)
plt.xlabel('log(Y)')
plt.ylabel('MMI')
plt.legend()

plt.show()

