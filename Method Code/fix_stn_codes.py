#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:08:07 2021

@author: emmadevin
"""

import pandas as pd

working_dir = '/Users/EmmaDevin/Work/USGS Summer 2020/USGS PLUM/Data'

df = pd.read_csv(working_dir + '/PGA_PGV/SoCal_EQ_Data_for_Emma.csv')

stn_codes = df['StationCode'].tolist()

stn_codes_upper = []
for stn in stn_codes:
    stn_codes_upper.append(stn.upper())

df['StationCode'] = stn_codes_upper

df.to_csv(working_dir + '/PGA_PGV/Revised_PGA_PGV_data.csv')