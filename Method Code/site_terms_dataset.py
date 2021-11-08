#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:02:37 2020

@author: emmadevin
"""


import pandas as pd
import numpy as np

working_dir = '/Users/EmmaDevin/Work/USGS Summer 2020/USGS PLUM/Data'
lme_dir = working_dir + '/LME'
outpath = working_dir + '/Site_Terms'

site_terms = pd.read_csv(lme_dir + '/site_terms.csv')
site_terms = site_terms.rename(columns={'StationCode':'station'})

df = pd.read_csv(working_dir + '/MMI/MMI_data_filtered.csv')

stns = df['StationCode']
ntwks = df['Network']
lat = df['StationLatitude']
lon = df['StationLongitude']

df1 = pd.DataFrame()

df1['network'] = ntwks
df1['station'] = stns
df1['latitude'] = lat
df1['longitude'] = lon
df1 = df1.drop_duplicates(subset = 'station')

df2 = df1.merge(site_terms, how = 'inner', indicator=False)
df2 = df2.rename(columns={'mmi_res':'site_term'})


df2.to_csv(outpath + '/Devin_Parker_MMI_site_terms.csv')

