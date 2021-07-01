#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:49:07 2020

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

plt.scatter(np.abs(soCal_byMag_9['VS30']), soCal_byMag_9['PGV_cms2'] , s = 2, c = 'black', label ='Magnitude 9')
plt.scatter(np.abs(soCal_byMag_8['VS30']), soCal_byMag_8['PGV_cms2'] , s = 2, c = 'orchid', label ='Magnitude 8')
plt.scatter(np.abs(soCal_byMag_7['VS30']), soCal_byMag_7['PGV_cms2'] , s = 2, c = 'green', label ='Magnitude 7')
plt.scatter(np.abs(soCal_byMag_6['VS30']), soCal_byMag_6['PGV_cms2'] , s = 2, c = 'c', label ='Magnitude 6')
plt.scatter(np.abs(soCal_byMag_5['VS30']), soCal_byMag_5['PGV_cms2'] , s = 2, c = 'b', label ='Magnitude 5')
plt.scatter(np.abs(soCal_byMag_4['VS30']), soCal_byMag_4['PGV_cms2'] , s = 2, c = 'm', label ='Magnitude 4')
plt.scatter(np.abs(soCal_byMag_3['VS30']), soCal_byMag_3['PGV_cms2'] , s = 2, c = 'yellow', label ='Magnitude 3')
plt.scatter(np.abs(soCal_byMag_2['VS30']), soCal_byMag_2['PGV_cms2'] , s = 2, c = 'purple', label ='Magnitude 2')
plt.scatter(np.abs(soCal_byMag_1['VS30']), soCal_byMag_1['PGV_cms2'] , s = 2, c = 'gray', label ='Magnitude 1')

plt.xlabel('VS30')
plt.ylabel('PGV')
plt.title('PGV vs. VS30 for Various Magnitudes')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.ylim(1e-6, 1e3)
#plt.xlim(2.5, 10)