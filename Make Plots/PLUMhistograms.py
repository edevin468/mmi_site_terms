#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:57:35 2020

@author: emmadevin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

dMMI2 = (ni-oi)
dMMI2 = dMMI2.dropna()

a['dMMI no correction'] = dMMI2
a['dMMI with correction'] = dMMI1


fig = plt.figure(figsize= (30, 12))

b = np.linspace(0,4.1,11)

plt.subplot(121)
counts, bins = np.histogram(dMMI1, bins = 20)
plt.hist(bins[:-1], bins, weights=counts)
plt.grid(True)
plt.xlim(0,5)
plt.title('With Site Corrections', fontsize = 20)
plt.xlabel('dMMI', fontsize = 20)
print('Median (w/ site corrections:',np.median(dMMI1))

plt.subplot(122)
counts, bins = np.histogram(dMMI2, bins = 20)
plt.hist(bins[:-1], bins, weights=counts)
plt.grid(True)
plt.xlim(0,5)
plt.title('Without Site Corrections', fontsize = 20)
plt.xlabel('dMMI', fontsize = 20 )
print('Median (w/o site corrections:',np.median(dMMI2))


