#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:20:40 2020

@author: EmmaDevin
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read full dataset 
soCal_data = pd.read_csv('/Users/EmmaDevin/USGS PLUM/Data/SoCal_EQ_Data_for_Emma.csv')
mag = soCal_data['EarthquakeMagnitude']
intMag = mag.astype(int)


soCal_byMag_9 = soCal_data[intMag == 9]
soCal_byMag_8 = soCal_data[intMag == 8]
soCal_byMag_7 = soCal_data[intMag == 7]   
soCal_byMag_6 = soCal_data[intMag == 6]
soCal_byMag_5 = soCal_data[intMag == 5]
soCal_byMag_4 = soCal_data[intMag == 4]
soCal_byMag_3 = soCal_data[intMag == 3]
soCal_byMag_2 = soCal_data[intMag == 2]
soCal_byMag_1 = soCal_data[intMag == 1]

plt.scatter(np.abs(soCal_byMag_9['HypocentralDistance']), soCal_byMag_9['PGV_cms2'] , s = 2, c = 'black', label ='M9')
plt.scatter(np.abs(soCal_byMag_8['HypocentralDistance']), soCal_byMag_8['PGV_cms2'] , s = 2, c = 'orchid', label ='M8')
plt.scatter(np.abs(soCal_byMag_7['HypocentralDistance']), soCal_byMag_7['PGV_cms2'] , s = 2, c = 'green', label ='M7')
plt.scatter(np.abs(soCal_byMag_6['HypocentralDistance']), soCal_byMag_6['PGV_cms2'] , s = 2, c = 'c', label ='M6')
plt.scatter(np.abs(soCal_byMag_5['HypocentralDistance']), soCal_byMag_5['PGV_cms2'] , s = 2, c = 'b', label ='M5')
plt.scatter(np.abs(soCal_byMag_4['HypocentralDistance']), soCal_byMag_4['PGV_cms2'] , s = 2, c = 'm', label ='M4')
plt.scatter(np.abs(soCal_byMag_3['HypocentralDistance']), soCal_byMag_3['PGV_cms2'] , s = 2, c = 'yellow', label ='M3')
plt.scatter(np.abs(soCal_byMag_2['HypocentralDistance']), soCal_byMag_2['PGV_cms2'] , s = 2, c = 'purple', label ='M2')
plt.scatter(np.abs(soCal_byMag_1['HypocentralDistance']), soCal_byMag_1['PGV_cms2'] , s = 2, c = 'gray', label ='M1')

#plt.plot(np.abs(soCal_byMag['HypocentralDistance']), soCal_byMag['PGA_g'])
plt.ylim(1e-5,1e3)
plt.xlim(8,500)
plt.xlabel('Hypocentral Distance')
plt.ylabel('PGV')
plt.title('PGV vs. Hypocentral Distance for Various Magnitudes')
plt.legend()
plt.xscale('log')
plt.yscale('log')


