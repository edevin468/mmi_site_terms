#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:52:14 2020

@author: emmadevin
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

noC = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/'
                  'PLUM Results/PLUMData/NoC_2014032904132000.csv')


withC = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/'
                  'PLUM Results/PLUMData/WithC_2014032904132000.csv')

obs = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/'
                  'PLUM Results/PLUMData/Obs_2014032904132000.csv')

oi = pd.DataFrame(obs['intensities'])
ni = pd.DataFrame(noC['intensities'])
wi = pd.DataFrame(withC['intensities'])
a = pd.DataFrame(noC['stations'])
a['observed'] = oi
a['no correction'] = ni
a['with correction'] = wi

dMMI1 = (wi-oi)
dMMI1 = dMMI1.dropna()

dMMI2 = ni-oi
dMMI2 = dMMI2.dropna()

a['dMMI no correction'] = dMMI2
a['dMMI with correction'] = dMMI1

a1 = a.dropna()

slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(a1['with correction'][:20], a1['observed'][:20])
x1 = np.linspace(2,8,20)
y1 = slope1*x1 + intercept1


slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(a1['no correction'][:20], a1['observed'][:20])
x2 = np.linspace(2,8,20)
y2 = slope2*x2 + intercept2

fig = plt.figure(figsize=(21, 12))

plt.subplot(121)
plt.scatter(a['with correction'], a['observed'])
plt.plot(x1,y1)
plt.grid(True)
plt.title('With Site Corrections')
plt.xlabel('with correction')
plt.ylabel('observed')

plt.subplot(122)
plt.scatter(a['no correction'], a['observed'])
plt.plot(x2,y2)
plt.grid(True)
plt.title('Without Site Corrections')
plt.xlabel('no correction')
plt.ylabel('observed')
plt.savefig('/Users/emmadevin/Work/USGS Work/USGS PLUM/PDF Plots/PLUMone-one.pdf') 