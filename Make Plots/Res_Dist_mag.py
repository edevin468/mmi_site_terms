#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 20:58:04 2020

@author: EmmaDevin
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

socal = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_withMMIpred.csv')

M = socal['EarthquakeMagnitude'] 

D = socal['EpicentralDistance']

totalResidual = socal['TotalResidual']

mag = socal['EarthquakeMagnitude']
intMag = mag.astype(int)


soCal_byMag_9 = socal[intMag == 9]
soCal_byMag_8 = socal[intMag == 8]
soCal_byMag_7 = socal[intMag == 7]   
soCal_byMag_6 = socal[intMag == 6]
soCal_byMag_5 = socal[intMag == 5]
soCal_byMag_4 = socal[intMag == 4]
soCal_byMag_3 = socal[intMag == 3]
soCal_byMag_2 = socal[intMag == 2]
soCal_byMag_1 = socal[intMag == 1]

plt.scatter(np.abs(soCal_byMag_9['HypocentralDistance']), soCal_byMag_9['TotalResidual'] , s = 10, edgecolors = 'black', facecolors ='none',label ='Magnitude 9')
plt.scatter(np.abs(soCal_byMag_8['HypocentralDistance']), soCal_byMag_8['TotalResidual'] , s = 10, edgecolors = 'orchid', facecolors ='none',label ='Magnitude 8')
plt.scatter(np.abs(soCal_byMag_7['HypocentralDistance']), soCal_byMag_7['TotalResidual'] , s = 10, edgecolors = 'green', facecolors ='none',label ='Magnitude 7')
plt.scatter(np.abs(soCal_byMag_6['HypocentralDistance']), soCal_byMag_6['TotalResidual'] , s = 10, edgecolors = 'c',facecolors ='none', label ='Magnitude 6')
plt.scatter(np.abs(soCal_byMag_5['HypocentralDistance']), soCal_byMag_5['TotalResidual'] , s = 10, edgecolors = 'b',facecolors ='none', label ='Magnitude 5')
plt.scatter(np.abs(soCal_byMag_4['HypocentralDistance']), soCal_byMag_4['TotalResidual'] , s = 10, edgecolors = 'm',facecolors ='none', label ='Magnitude 4')
plt.scatter(np.abs(soCal_byMag_3['HypocentralDistance']), soCal_byMag_3['TotalResidual'] , s = 10, edgecolors = 'yellow',facecolors ='none', label ='Magnitude 3')
plt.scatter(np.abs(soCal_byMag_2['HypocentralDistance']), soCal_byMag_2['TotalResidual'] , s = 10, edgecolors = 'purple',facecolors ='none', label ='Magnitude 2')
plt.scatter(np.abs(soCal_byMag_1['HypocentralDistance']), soCal_byMag_1['TotalResidual'] , s = 10, edgecolors = 'gray', facecolors ='none',label ='Magnitude 1')

plt.xlabel(' HypocentralDistance')
plt.xlim(1e0,1e4)
plt.xscale('log')
plt.ylabel('Total Residual')
plt.title('Total MMI Residual vs. Hypocentral Distance for Various Magnitudes')
plt.axhline(c ='k')
plt.legend()
