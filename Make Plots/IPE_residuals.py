#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:53:39 2020

@author: emmadevin
"""

import numpy as np
from numpy import sin, cos, pi, arccos
import pandas as pd
import matplotlib.pyplot as plt

### Ridgecrest PLUM Results (only for station locations)
# df = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/PLUM Results/Ridgecrest/dMMI/dMMI_Locations2.csv')

### La Habra PLUM Results
df = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/PLUM Results/LaHabra/dMMI/dMMI_Locations2.csv')


df = df.reset_index()
eventTerms = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/LME_SoCal/event_terms.csv')

### event info Ridgecrest ID = ci38457511
# M = 7.1
# depth = 8.0
# eventlat = 35.766
# eventlon = -117.605
# R = eventTerms['EarthquakeID'] == 'ci38457511'
# et = eventTerms[R]
# et = et.reset_index()
# et = et['TotalResidual'][0]

### event info La Habra ID = ci15481673
M = 5.1
depth = 5.1
eventlat = 33.933
eventlon = -117.916
LH = eventTerms['EarthquakeID'] == 'ci15481673'
et = eventTerms[LH]
et = et.reset_index()
et = et['TotalResidual'][0]

### station information
siteterm = np.array(df['SiteTerm'])
statlat = df['StationLatitude']
statlon = df['StationLongitude']
statlon = np.array(statlon)

### calculate distance from each station to hypocenter
e = arccos(sin(pi*eventlat/180)*sin(pi*statlat/180)+cos(pi*eventlat/180)*cos(pi*statlat/180)*cos(pi*eventlon/180-pi*statlon/180))*6378
e = np.array(e)
D = np.sqrt(depth**2 + e**2) 

R = np.sqrt(D**2 + 14**2)
B = []
for i in range(len(R)):
    b = np.max(np.linspace(0,np.log10(R[i]/50), 500))
    B.append(b)
B = np.array(B)
   
# constants from table 1 Atinson et al.
c = [0,0.309,1.864,-1.672,-0.00219,1.77,-0.383]

# compute the MMI predicted
MMIp = c[1]+c[2]*M+c[3]*np.log10(R)+c[4]*R+c[5]*B+c[6]*M*np.log10(R) 
MMIpwithSiteTerm = c[1]+c[2]*M+c[3]*np.log10(R)+c[4]*R+c[5]*B+c[6]*M*np.log10(R)+ siteterm 
reswithout = df['observed'] - MMIp 
reswith = df['observed'] - MMIpwithSiteTerm

df['PredictedMMI'] = MMIp
df['PredictedMMIwithSiteTerms'] = MMIpwithSiteTerm
df['residual-without'] = reswithout
df['residual-with'] = reswith


# we want |reswithout| - |reswith| to be positive

dif = np.abs(reswithout)-np.abs(reswith)

count_pos = 0
count_neg = 0
i = 0
for i in range(len(dif)):
    if dif[i] >= 0:
        count_pos +=1
    elif dif[i] < 0:
        count_neg +=1

print('Positive:', count_pos)
print('Negative:', count_neg)

print('The site terms decreased %5.2f' % (count_pos/332*100),'% of the residuals (Observed - Predicted MMI).')
print('The average difference between the absolute values of the site terms is %5.2f.' % (np.mean(dif)))
print('Mean residual w/: %5.2f.' % np.mean(np.abs(reswith)))
print('Mean residual w/o: %5.2f.' % np.mean(np.abs(reswithout)))
print('Stdev w/: %5.2f.' % np.std(np.abs(reswith)))
print('Stdev  w/o: %5.2f.' % np.std(np.abs(reswithout)))

fs = 12 

fig = plt.figure(figsize=(5, 10))

plt.subplot(211)
plt.scatter(D,np.abs(reswith), edgecolors = 'navy', facecolors = 'none',label='residual with corrections', )
plt.scatter(D,np.abs(reswithout),  edgecolors = 'deepskyblue', facecolors = 'none',label = 'residual without corrections')
plt.axhline(y = np.mean(np.abs(reswith)),c = 'navy', label='average residual with corrections' )
plt.axhline(y = np.mean(np.abs(reswithout)),c ='deepskyblue', label='average residual without corrections' )
# plt.title('|Residuals| vs Hypocentral Distance', fontsize = fs)
plt.xlabel('Hypocentral Distance', fontsize = fs)
plt.ylabel('|Observed MMI - Predicted MMI|', fontsize = fs)
plt.legend(bbox_to_anchor=(0.5, -0.4), loc='lower center', fontsize = 10)
plt.tight_layout()


# plt.savefig('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/FinalPlots/IPESiteTermRidgecrest.pdf') 
plt.savefig('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/FinalPlots/IPESiteTermLaHabra.pdf') 
# df.to_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/IDWandSiteTermsRidgecrest.csv')