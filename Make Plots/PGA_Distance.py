#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:34:27 2020

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

plt.scatter((soCal_byMag_9['HypocentralDistance']), soCal_byMag_9['PGA_g'] , s = 2, c = 'black', label ='Magnitude 9')
plt.scatter((soCal_byMag_8['HypocentralDistance']), soCal_byMag_8['PGA_g'] , s = 2, c = 'orchid', label ='Magnitude 8')
plt.scatter((soCal_byMag_7['HypocentralDistance']), soCal_byMag_7['PGA_g'] , s = 2, c = 'green', label ='Magnitude 7')
plt.scatter((soCal_byMag_6['HypocentralDistance']), soCal_byMag_6['PGA_g'] , s = 2, c = 'c', label ='Magnitude 6')
plt.scatter((soCal_byMag_5['HypocentralDistance']), soCal_byMag_5['PGA_g'] , s = 2, c = 'b', label ='Magnitude 5')
plt.scatter((soCal_byMag_4['HypocentralDistance']), soCal_byMag_4['PGA_g'] , s = 2, c = 'm', label ='Magnitude 4')
plt.scatter((soCal_byMag_3['HypocentralDistance']), soCal_byMag_3['PGA_g'] , s = 2, c = 'yellow', label ='Magnitude 3')
plt.scatter((soCal_byMag_2['HypocentralDistance']), soCal_byMag_2['PGA_g'] , s = 2, c = 'purple', label ='Magnitude 2')
plt.scatter((soCal_byMag_1['HypocentralDistance']), soCal_byMag_1['PGA_g'] , s = 2, c = 'gray', label ='Magnitude 1')

#plt.plot(np.abs(soCal_byMag['HypocentralDistance']), soCal_byMag['PGA_g'])
plt.ylim(1e-6,1e0)
plt.xlim(8,600)
plt.xlabel('Hypocentral Distance')
plt.ylabel('PGA')
plt.title('PGA vs. Hypocentral Distance for Various Magnitudes')
plt.legend()
plt.xscale('log')
plt.yscale('log')

