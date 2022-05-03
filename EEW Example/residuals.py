#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 10:58:58 2022

@author: emmadevin
"""

import pandas as pd

df1 = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS Plum/EEW Example/FinalData/ShakeAlert_Northridge_Predicted_MMI.csv')
df2 = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS Plum/EEW Example/FinalData/shakemap_grid.csv')

S = df2['mmimean']
MMIwo = df1['MMI']
MMIw = df1['MMI_st']

res_wo = S - MMIwo
res_w = S - MMIw

res = abs(res_w) - abs(res_wo)

df2['Delta_R'] = res

df2.to_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS Plum/EEW Example/FinalData/shakemap_grid_res.csv')