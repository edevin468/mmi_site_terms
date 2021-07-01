#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:37:46 2020

@author: emmadevin
"""


import pandas as pd

df = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_withMMIpred.csv')

large = df['MMI']>3

df1 = df[large]

df1.to_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_largeMMI.csv')