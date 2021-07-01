#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 21:40:47 2020

@author: EmmaDevin
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

socal = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_filtered.csv')


totalResidual = socal['TotalResidual']
M = socal['EarthquakeMagnitude'] 
df = pd.DataFrame(M)
df.columns = ['magnitude']
df['residual'] = totalResidual

df = df.dropna()

bin_means, bin_edges, binnumber = stats.binned_statistic(df['magnitude'], df['residual'], statistic='mean', bins=20)

bin_width = (bin_edges[1] - bin_edges[0])
bin_centers = bin_edges[1:] - bin_width/2


plt.scatter(M,totalResidual,s=50,edgecolors='lightblue' , facecolors = 'none', label ='Full Dataset')
#plt.hlines(bin_means, bin_edges[:-1], bin_edges[1:], colors='k', lw=5,label='Binned Mean of Data')
plt.scatter(bin_centers, bin_means, c='k', s =9,label='Binned Mean of Data')
plt.xlabel('Magnitude')
#plt.xlim(0,1000)
plt.ylabel('Total Residual')
plt.title('Total MMI Residual vs. Magnitude')
plt.axhline(c ='k', lw=1)
plt.legend()