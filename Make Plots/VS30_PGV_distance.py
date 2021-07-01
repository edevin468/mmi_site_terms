#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:46:19 2020

@author: EmmaDevin
"""



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read full dataset 
soCal_data = pd.read_csv('/Users/EmmaDevin/USGS PLUM/Data/SoCal_EQ_Data_for_Emma.csv')
distance = soCal_data['HypocentralDistance']
mag = soCal_data['EarthquakeMagnitude']
intMag = mag.astype(int)

#distanceBins = np.linspace(0, 1156, 10)
distanceBins = np.logspace(0, 3.1, 10)
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

plt.scatter(soCal_byDist_1['VS30'], soCal_byDist_1['PGV_cms2'], s = 2, c = 'purple', label = '0 to 2 km')
plt.scatter(soCal_byDist_2['VS30'], soCal_byDist_2['PGV_cms2'], s = 2, c = 'b', label = '2 to 5 km')
plt.scatter(soCal_byDist_3['VS30'], soCal_byDist_3['PGV_cms2'], s = 2, c = 'r', label = '5 to 11 km')
plt.scatter(soCal_byDist_4['VS30'], soCal_byDist_4['PGV_cms2'], s = 2, c = 'c', label = '11 to 24 km')
plt.scatter(soCal_byDist_5['VS30'], soCal_byDist_5['PGV_cms2'], s = 2, c = 'black', label = '24 to 53 km')
plt.scatter(soCal_byDist_6['VS30'], soCal_byDist_6['PGV_cms2'], s = 2, c = 'yellow',label = '53 to 116 km')
plt.scatter(soCal_byDist_7['VS30'], soCal_byDist_7['PGV_cms2'], s = 2, c = 'c', label = '116 to 257 km')
plt.scatter(soCal_byDist_8['VS30'], soCal_byDist_8['PGV_cms2'], s = 2, c = 'm', label = '257 to 569 km')
plt.scatter(soCal_byDist_9['VS30'], soCal_byDist_9['PGV_cms2'], s = 2, c = 'green', label = '569 to 1258 km')

plt.xlabel('VS30')
plt.ylabel('PGV')
plt.title('PGV vs. VS30 for Various Distances')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.ylim(1e-6, 1e3)
#plt.xlim(2.5, 10)
