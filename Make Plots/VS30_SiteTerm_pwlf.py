#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:00:26 2020

@author: emmadevin
"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pwlf

## READ AND MANIPULATE DATA

# read in results from linear mixed analysis
bias = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data_Old/LME_SoCal_filtered/bias.csv')
siteTerms = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data_Old/LME_SoCal_filtered/site_terms.csv')
eventTerms = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data_Old/LME_SoCal_filtered/event_terms.csv')

# read in earthquake dataset
dataset = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data_Old/SoCal_filtered.csv')

# define variables and create dataset for VS30 and siteterms 
VS30 = dataset[['StationID','StationLatitude','StationLongitude','VS30']]
VS30 =  VS30.drop_duplicates(subset = 'StationID')    
VS30 = VS30.reset_index()
df = VS30.merge(siteTerms, how='inner',indicator=False)

## STATISTICAL ANALYSIS

# use scipy stats to calculate binned means
bin_means, bin_edges, binnumber = stats.binned_statistic(df['VS30'], df['TotalResidual'], statistic='mean', bins=10)
bin_width = (bin_edges[1] - bin_edges[0])
bin_centers = bin_edges[1:] - bin_width/2

# x = bin_centers[:-1]
# y = bin_means[:-1]

# define x and y for regression
x = df['VS30']
y = df['TotalResidual']
bound = x < 1400
x = x[bound]
y =y[bound]


# piecewise linear least squares fitting


# your desired line segment end locations, instead of forcing fit
#x0 = np.array([min(x), 900, max(x)])

# initialize piecewise linear fit with your x and y data
f = pwlf.PiecewiseLinFit(x, y)

# fit the data with the specified break points
# (ie the x locations of where the line segments will terminate)
#f.fit_with_breaks(x0)

# define points to force fit to, in order to get slope of 0 in second segment
x_c = [951, 1400]
y_c = [-0.253927, -0.253927]

# fit the data using 2 line segments, forcing through x_c and y_c
res = f.fit(2, x_c, y_c)

# predict for the determined points
xHat = np.linspace(min(x), max(x), num=10000)
yHat = f.predict(xHat)

# plot the results
plt.plot(xHat, yHat, c ='r', label='Least squares piecewise fit')

#plot dataset
plt. scatter(df['VS30'],df['TotalResidual'],s = 20, edgecolors = 'gray', facecolors='none', label='Dataset')

# plot binned means, either lines or points
#plt.hlines(bin_means, bin_edges[:-1], bin_edges[1:], colors='k', lw=5,label='Binned Mean of Data')
plt.scatter(bin_centers[:-1], bin_means[:-1], c='k',label='Binned mean of data')

# plot labels
plt.xlabel(r'$V_{S30}$ (m/s)')
plt.ylabel('Site Term (MMI units)')
plt.axhline(y = 0, c ='k', lw = 1)
# plt.title('Site Term vs VS30 (filtered dataset)')
# plt.xscale('log')
plt.xlim(0,1400)
plt.legend()
# plt.savefig('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/FinalPlots/SiteTermvsVS30.pdf') 
# print equations
print('-------------------------------------------\n'
      'Least Squares Model for VS30 and Site Term\n'
      '-------------------------------------------\n')
print('Vc = ',x_c[0], 'm/s \n')
for i in range(len(f.slopes)):

    if i == 0: rel = '<='
    elif i == 1: rel = '>'
    
    print('F(VS30) = ',f.slopes[i],'*VS30 + ',f.intercepts[i],
          'for VS30',rel,' Vc')
    


# calculate residuals from data points to model

vs30 = df['VS30']
siteTerms = df['TotalResidual']

one = vs30 <= 951
two = vs30 > 951

residuals1 = siteTerms[one] - f.slopes[0]*vs30[one]+f.intercepts[0]
residuals2  = siteTerms[two] - f.slopes[1]*vs30[two]+f.intercepts[1]

residuals = np.append(residuals1, residuals2)

df['ModelResidual'] = residuals
  
# df.to_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/SiteResponseModelResiduals.csv')    

std = np.std(residuals)

print('Standard Deviation of Residuals:', std)
