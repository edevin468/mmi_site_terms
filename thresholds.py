#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:08:30 2021

@author: emmadevin
"""

import pandas as pd

df = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/EEW Example/shakemap_grid.csv')

mmi = df['mmimean'].round(1)
lat = df['lat']
lon = df['lon']

thresh1 = mmi == 3.5 
thresh2 = mmi == 4.5


lat1 = lat[thresh1]
lat2 = lat[thresh2]
lon1 = lon[thresh1]
lon2 = lat[thresh2]

df1=pd.DataFrame()
df2=pd.DataFrame()

df1['lat']=lat1
df1['lon']=lon1

df2['lat']=lat2
df2['lon']=lon2

df1.to_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/EEW Example/thresh1.csv')
df2.to_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/EEW Example/thresh2.csv')
