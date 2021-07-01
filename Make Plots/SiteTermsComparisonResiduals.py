#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:58:29 2020

@author: emmadevin
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df1 = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/Compiled_Instrumental_Site_Terms.csv')
df2 = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/SiteResponse.csv')
siteMMI = df2[['StationCode','site']]

df = df1.merge(siteMMI)

# line with a slope of 1
x = np.linspace(-2,3, 20)
y = x

# define a dictionary containing arrays with the MMI site terms and each of the GM site terms
d = { 
    0 : df[['site','Site_Term_PGA']],
    1 : df[['site','Site_Term_PGV']],
    2 : df[['site','Site_Term_PSA_0.01s']],
    3 : df[['site','Site_Term_PSA_0.02s']],
    4 : df[['site','Site_Term_PSA_0.03s']],
    5 : df[['site','Site_Term_PSA_0.05s']],
    6 : df[['site','Site_Term_PSA_0.075s']],
    7 : df[['site','Site_Term_PSA_0.1s']],
    8 : df[['site','Site_Term_PSA_0.15s']],
    9 : df[['site','Site_Term_PSA_0.25s']],
    10 : df[['site','Site_Term_PSA_0.3s']],
    11 : df[['site','Site_Term_PSA_0.4s']],
    12 : df[['site','Site_Term_PSA_0.5s']],
    13 : df[['site','Site_Term_PSA_0.75s']],
    14 : df[['site','Site_Term_PSA_1s']],
    15 : df[['site','Site_Term_PSA_2s']],
    16 : df[['site','Site_Term_PSA_3s']],
    17 : df[['site','Site_Term_PSA_4s']],
    18 : df[['site','Site_Term_PSA_5s']],
    19 : df[['site','Site_Term_PSA_7.5s']],
    20 : df[['site','Site_Term_PSA_10s']] 
    }

# calculate average residual for each site term metric to MII site term
avg_residuals = []
avg_res2s = []
for i in range(21):
    
    m = d[i]
    y1 = m.iloc[:,0]
    x1 = m.iloc[:,1]
    
    b = y1 + x1
    
    x2 = b/2
    y2 = x2

    residual = np.sqrt((x2-x1)**2+(y2-y1)**2)
    res2 = x1-y1
   
    avg_residual = np.mean(residual)
    avg_residuals.append(avg_residual)
    
    avg_res2 = np.mean(res2)
    avg_res2s.append(avg_res2)
    
# print output  
print('------------------------------------------------------------\n'
      'Average Residual for MMI site Term for Instrumental Metrics:\n'
      '------------------------------------------------------------\n')

for i in range(21):
    m = d[i]
    metric = m.columns[1]
    print('For', metric,':\n',
          'Average Residual = ', avg_residuals[i])
    
t = [0.01,0.02,0.03,0.05,0.075,0.1,0.15,0.2,0.25,0.3,0.4,0.5,0.75,1,2,3,4,5,7.5,10]    
plt.scatter(t, avg_residuals[1:], label = 'Calculated as shortest distance to line y = x')
plt.scatter(t, avg_res2s[1:], label= 'Calculated by subtraction')
plt.xscale('log')
plt.xlabel('Period of PSA')
plt.ylabel('Residual')
plt.title('Residuals of MMI Site Terms to PSA Site Terms')
plt.ylim(0.1,0.8)
# plt.legend(loc = 2)

rs = []

for i in range(21):
    
    m = d[i]
    m = m.dropna()
    y1 = m.iloc[:,0]
    x1 = m.iloc[:,1]
    
    r = np.corrcoef(x1, y1)
    R = r[0,1]
    rs.append(R)

fig2 = plt.figure()    
plt.scatter(t, rs[1:], s = 10, edgecolors = 'tab:blue', facecolors = 'tab:blue', label='Correlation Coefficient R vs Period')
plt.xlabel('Period of PSA (s)')
plt.ylabel('Correlation Coefficient')
# plt.title('Correlation Coefficient R vs Period')
# plt.legend()
plt.savefig('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/FinalPlots/RSiteTerms.pdf') 
