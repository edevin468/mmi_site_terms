#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 22:05:12 2020

@author: EmmaDevin
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import convertToMMI as m

socaldata = pd.read_csv('/Users/EmmaDevin/USGS PLUM/Data/SoCal_withMMI.csv')

pga = socaldata['PGA_g']
pga = pga.replace(-999, np.nan)
pga = pga*9.8*100
pgv = socaldata['PGV_cms2']
M = socaldata['EarthquakeMagnitude']
H = socaldata['HypocentralDistance']

aT2 = 4.22
vT2 = 4.56

    # initialize list to store MMI values
A = []
V = []

   # for each index value , call the function getMII and assign its output to peicewise define MMA and MMV 

mma1, mma2, mmv1, mmv2 = m.getMMI(pga,pgv, M, H)

   


MMA1 = np.where(mma1<=aT2, mma1, np.nan)
MMA2 = np.where(mma2>aT2, mma2, np.nan)

MMV1 = np.where(mmv1<=vT2, mmv1, np.nan)
MMV2 = np.where(mmv2>vT2, mmv2, np.nan)


A = pd.DataFrame({'MMA1':MMA1, 'MMA2':MMA2})
V = pd.DataFrame({'MMV1':MMV1, 'MMV2':MMV2})


A['MMA']=A['MMA1'].mask(pd.isnull, A['MMA2'])
V['MMV']=V['MMV1'].mask(pd.isnull, V['MMV2'])

#MMI_final = 0.46*A['MMA']+0.52*V['MMV']
MMI_final = (A['MMA']+V['MMV'])/2

# mmi_1 = 0.46*mma1 + 0.52*mmv1
# mmi_2 = 0.46*mma2 + 0.52*mmv2

# mmiList = pd.DataFrame({'MMI1':mmi_1,'MMI2':mmi_2})

# mmiList['MMI']=mmiList['MMI1'].mask(pd.isnull, mmiList['MMI2'])


plt.scatter(pga, MMI_final, s=1, c='r', label ='MMI vs PGA')
plt.scatter(pga,A['MMA'], s = 1, c = 'c', label = 'MMA vs PGA')
plt.scatter(pgv, V['MMV'], s=1, c = 'b', label= 'MMV vs PGV')


plt.xscale('log')
plt.xlim(1e-4,1e4)

plt.ylim(-2,10)
plt.xlabel('log(Y)')
plt.ylabel('MMI')
plt.legend()

    
    