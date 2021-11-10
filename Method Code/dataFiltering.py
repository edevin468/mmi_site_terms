#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:49:13 2020

@author: emmadevin
"""
import pandas as pd
import numpy as np

working_dir = '/Users/EmmaDevin/Work/USGS Summer 2020/USGS PLUM/Data'

df = pd.read_csv(working_dir + '/MMI/MMI_data.csv')

stations = df['StationCode']
counts = stations.value_counts()


count_list = []
for i in range(len(stations)):
    station = stations[i]
    count = counts[station]
    
    count_list.append(count)
    

    
count_list = np.array(count_list)
df['Counts'] = count_list
df_filtered = df[df['Counts']>0]

large = df_filtered['mmi']>0
df1 = df_filtered[large]

vs30= df1['VS30']
df1['VS30'] = vs30.replace(-999, None)

df1.to_csv(working_dir + '/MMI/MMI_data_filtered.csv')

