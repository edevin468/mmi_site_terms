#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:25:04 2020

@author: emmadevin
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

bias = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal_filtered/bias.csv')
siteTerms = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal_filtered/site_terms.csv')
eventTerms = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal_filtered/event_terms.csv')

dataset = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_filtered.csv')

vs30 = dataset[['StationID','VS30']]
vs30 =  vs30.drop_duplicates(subset = 'StationID')    
vs30 = vs30.reset_index()

df = vs30.merge(siteTerms, how='inner',indicator=False)




bin_means, bin_edges, binnumber = stats.binned_statistic(df['VS30'], df['TotalResidual'], statistic='mean', bins=20)

bin_width = (bin_edges[1] - bin_edges[0])
bin_centers = bin_edges[1:] - bin_width/2

plt. scatter(df['VS30'],df['TotalResidual'],s = 20, edgecolors = 'slateblue', facecolors='none', label='Available Data')
plt.hlines(bin_means, bin_edges[:-1], bin_edges[1:], colors='k', lw=5,label='Binned Mean of Data')
plt.xlabel('VS30')
plt.ylabel('Site Term')
plt.axhline(y = 0, c ='k', lw = 1)
plt.title('Site Term vs VS30 filtered by MMI and station frequency')
# plt.xscale('log')
# plt.xlim(1e2,4e3)
plt.legend()