#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:39:28 2020

@author: EmmaDevin
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import convertToMMI as m

socaldata = pd.read_csv('/Users/EmmaDevin/USGS PLUM/Data/SoCal_withMMI.csv')

pga = socaldata['PGA_g']
pga = pga.replace(-999, 0)
pga = pga*9.8*100
pgv = socaldata['PGV_cms2']
M = socaldata['EarthquakeMagnitude']
H = socaldata['HypocentralDistance']
at2=4.22
vt2=4.56

mma1, mma2, mmv1, mmv2 = m.getMMI(pga,pgv,M, H)


lowera = mma1<=at2
uppera = mma2>at2
lowerv = mma1<=vt2
upperv = mma2>vt2


mma_lower = mma1[lowera]
mma_upper = mma2[uppera]
mmv_lower = mma1[lowerv]
mmv_upper = mma2[upperv]

A = pd.DataFrame({'MMA1':mma_lower, 'MMA2':mma_upper, 'PGA':pga})
V = pd.DataFrame({'MMV1':mmv_lower, 'MMV2':mmv_upper, 'PGA':pga})

A['MMA']=A['MMA1'].mask(pd.isnull, A['MMA2'])
V['MMV']=V['MMV1'].mask(pd.isnull, V['MMV2'])


mmi = 0.46*A['MMA'] + 0.52*V['MMV']




plt.scatter(pga, mmi)
plt.scatter(pgv, mmi)


#plt.scatter(pga, mmaList, s = 2, c = 'm')
#plt.scatter(pgv, mmvList, s = 2, c = 'c')
#plt.scatter(pga[lower], mma1[lower], s=2)
#plt.scatter(pga[upper], mma2[upper], s=2)
#plt.axhline(t2, c= 'k')
plt.xscale('log')
plt.xlim(1e-3, 1e4)
plt.ylim(-2,10)
plt.xlabel('log(Y)')
plt.ylabel('MMI')
plt.legend()
