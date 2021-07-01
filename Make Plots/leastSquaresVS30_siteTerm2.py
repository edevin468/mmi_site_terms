#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:13:17 2020

@author: emmadevin
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

## READ AND MANIPULATE DATA

# read in results from linear mixed analysis
bias = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal_filtered/bias.csv')
siteTerms = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal_filtered/site_terms.csv')
eventTerms = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal_filtered/event_terms.csv')

# read in earthquake dataset
dataset = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_filtered.csv')

# define variables and create dataset for VS30 and siteterms 
vs30 = dataset[['StationID','VS30']]
vs30 =  vs30.drop_duplicates(subset = 'StationID')    
vs30 = vs30.reset_index()
df = vs30.merge(siteTerms, how='inner',indicator=False)

## STATISTICAL ANALYSIS

# use scipy stats to calculate binned means
bin_means, bin_edges, binnumber = stats.binned_statistic(df['VS30'], df['TotalResidual'], statistic='mean', bins=14)
bin_width = (bin_edges[1] - bin_edges[0])
bin_centers = bin_edges[1:] - bin_width/2


# use scipy stats to perform linear least squares regression on binned means
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(bin_centers[:-5],bin_means[:-5])
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(bin_centers[-6:-2],bin_means[-6:-2])
x1 = np.linspace(0,900, 500)
y1 = slope1*x1 + intercept1
x2 = np.linspace(900,1450,500)
y2 = slope2*x2 + intercept2

# using model from Seyhan et al.


## PLOT



# plot resulting line
plt.plot(x1,y1, c = 'r', label='Least Squares Model')
plt.plot(x2,y2, c = 'r')

#plot dataset
plt. scatter(df['VS30'],df['TotalResidual'],s = 20, edgecolors = 'gray', facecolors='none', label='Dataset')

# plot binned means, either lines or points
#plt.hlines(bin_means, bin_edges[:-1], bin_edges[1:], colors='k', lw=5,label='Binned Mean of Data')
plt.scatter(bin_centers, bin_means, c='k',label='Binned Mean of Data')

# plot labes
plt.xlabel('VS30')
plt.ylabel('Site Term')
plt.axhline(y = 0, c ='k', lw = 1)
plt.title('Site Term vs VS30 (filtered dataset)')
# plt.xscale('log')
# plt.xlim(1e2,4e3)
plt.legend()

# print model

print('\n  ------------------------------------------\n  Linear model of VS30 and Site Term:\n',
      ' ------------------------------------------\n',
      '\n\nF = ',slope1,'* VS30 +',intercept1 ,'for VS30 <= 900',
      '\nF = ',slope2,'* VS30 +',intercept2 ,'for VS30 > 900',
      '\n\nR-Squared = ', r_value1**2, 'for VS30 <= 900',
      '\nR-Squared = ', r_value2**2, 'for VS30 > 900')

