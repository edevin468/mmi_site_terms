#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:26:35 2021

@author: emmadevin
"""

import pandas as pd
import matplotlib.pyplot as plt

working_dir = '/Users/EmmaDevin/Work/USGS Summer 2020/USGS PLUM'

new = pd.read_csv(working_dir + '/Data/Site_Terms/Devin_Parker_MMI_site_terms.csv')
old = pd.read_csv(working_dir + '/Data_Old/Devin_Parker-Site_Terms.csv')

stations =  old['StationCode'].tolist()
n = stations.index('BOM')
bom_old1 = old['SiteTerm'][n]
n = stations.index('bom')
bom_old2 = old['SiteTerm'][n]

df1 = pd.DataFrame()
df1['station'] = new['station']
df1['new_site_term'] = new['site_term']

stations =  df1['station'].tolist()
n = stations.index('BOM')
bom_new = df1['new_site_term'][n]

df2 = pd.DataFrame()
stns = old['StationCode']
old_stns = []
for stn in stns: 
    stn = stn.upper()
    old_stns.append(stn)

df2['station'] = old_stns
df2['old_site_term'] = old['SiteTerm']





df3 = df1.merge(df2, how = 'inner', indicator = False)
new = df3['new_site_term']
stations = df3['station']
# bom_new = stations.index('BOM')

# bom = (df3['new_site_term']['bom'])

plt.scatter(df3['new_site_term'], df3['old_site_term'], s =5)
plt.scatter(bom_new, bom_old1, c = 'r',s =5, label = 'BOM')
plt.scatter(bom_new, bom_old2, c = 'r', s =5,label = 'bom')
plt.xlabel('new site term')
plt.ylabel('old site term')
plt.legend()



