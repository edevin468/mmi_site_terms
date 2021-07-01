#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:08:20 2020

@author: EmmaDevin
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read full dataset 
soCal_data = pd.read_csv('/Users/EmmaDevin/USGS PLUM/Data/SoCal_EQ_Data_for_Emma.csv')
distance = soCal_data['HypocentralDistance']

distanceBins = np.linspace(0, np.max(distance), 10)
binLabels = [1,2,3,4,5,6,7,8,9]

soCal_data['DistanceBins'] = pd.cut(soCal_data['HypocentralDistance'], bins = distanceBins, labels = binLabels)

bins = soCal_data['DistanceBins']

soCal_byDist_1 = soCal_data[bins == 1]
soCal_byDist_2 = soCal_data[bins == 2]
soCal_byDist_3 = soCal_data[bins == 3]
soCal_byDist_4 = soCal_data[bins == 4]
soCal_byDist_5 = soCal_data[bins == 5]
soCal_byDist_6 = soCal_data[bins == 6]
soCal_byDist_7 = soCal_data[bins == 7]
soCal_byDist_8 = soCal_data[bins == 8]
soCal_byDist_9 = soCal_data[bins == 9]

#print(np.max(soCal_byDist_2['HypocentralDistance']))

plt.scatter(soCal_byDist_1['EarthquakeMagnitude'], soCal_byDist_1['PGA_g'], s = 2, c = 'r', label = '0 to 128 km')
plt.scatter(soCal_byDist_2['EarthquakeMagnitude'], soCal_byDist_2['PGA_g'], s = 2, c = 'b', label = '128 to 257 km')
plt.scatter(soCal_byDist_3['EarthquakeMagnitude'], soCal_byDist_3['PGA_g'], s = 2, c = 'yellow', label = '257 to 385 km')
plt.scatter(soCal_byDist_4['EarthquakeMagnitude'], soCal_byDist_4['PGA_g'], s = 2, c = 'm', label = '385 to 514 km')
plt.scatter(soCal_byDist_5['EarthquakeMagnitude'], soCal_byDist_5['PGA_g'], s = 2, c = 'c', label = '514 to 642 km')
plt.scatter(soCal_byDist_6['EarthquakeMagnitude'], soCal_byDist_6['PGA_g'], s = 2, c = 'black',label = '642 to 771 km')
plt.scatter(soCal_byDist_7['EarthquakeMagnitude'], soCal_byDist_7['PGA_g'], s = 2, c = 'green', label = '771 to 899 km')
plt.scatter(soCal_byDist_8['EarthquakeMagnitude'], soCal_byDist_8['PGA_g'], s = 2, c = 'purple', label = '899 to 1028 km')
plt.scatter(soCal_byDist_9['EarthquakeMagnitude'], soCal_byDist_9['PGA_g'], s = 2, c = 'gray', label = '1028 to 1156 km')

plt.xlabel('Earthquake Magnitude')
plt.ylabel('PGA')
plt.title('PGA vs. Magnitude for Various Distances')
plt.legend()
plt.yscale('log')
#plt.xscale('log')
plt.ylim(1e-8, 1e2)
plt.xlim(2.5, 10)
