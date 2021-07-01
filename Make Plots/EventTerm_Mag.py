#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:53:18 2020

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

M = dataset[['EarthquakeID','EarthquakeMagnitude']]
M = M.drop_duplicates(subset = 'EarthquakeID')    
M = M.reset_index()

df = M.merge(eventTerms, how='inner',indicator=False)




bin_means, bin_edges, binnumber = stats.binned_statistic(df['EarthquakeMagnitude'], df['TotalResidual'], statistic='mean', bins=20)

bin_width = (bin_edges[1] - bin_edges[0])
bin_centers = bin_edges[1:] - bin_width/2

plt. scatter(df['EarthquakeMagnitude'],df['TotalResidual'],s = 20, edgecolors = 'cadetblue', facecolors='none', label='Available Data')
plt.hlines(bin_means, bin_edges[:-1], bin_edges[1:], colors='k', lw=5,label='Binned Mean of Data')
plt.xlabel('Magnitude')
plt.ylabel('Event Term')
plt.axhline(y = 0, c ='k', lw = 1)
plt.title('Event Term vs Magnitude filtered by MMI and station frequency')
# plt.xscale('log')
# plt.xlim(1e2,4e3)
plt.legend()