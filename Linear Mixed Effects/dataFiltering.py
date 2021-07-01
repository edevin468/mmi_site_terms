#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:49:13 2020

@author: emmadevin
"""
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_withMMIpred.csv')

stations = df['StationID']
counts = stations.value_counts()

countslist =[]
for i in range(len(stations)):
    n = stations[i]
    count = counts[n]
    countslist.append(count)
    
countslist = np.array(countslist)
df['Counts'] = countslist
df_filtered = df[df['Counts']>5]

large = df_filtered['MMI']>2
df1 = df_filtered[large]

vs30= df1['VS30']
df1['VS30'] = vs30.replace(-999, None)

df1.to_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_filtered.csv')

#df_filtered.to_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_filtered_stationFreq.csv')