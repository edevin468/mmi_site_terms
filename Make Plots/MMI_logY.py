#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 09:19:14 2020

@author: EmmaDevin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

socaldata = pd.read_csv('/Users/EmmaDevin/USGS PLUM/Data/SoCal_withMMI.csv')

logPGA = np.log10(socaldata['PGA_g']*9.8*100)
logPGV = np.log10(socaldata['PGV_cms2'])


plt.scatter(socaldata['PGA_g']*980, socaldata['MMI'], s = 5, c = 'maroon', label ='Y = PGA')
plt.scatter(socaldata['PGV_cms2'], socaldata['MMI'], s = 5, c = 'springgreen', label ='Y = PGV')

#plt.scatter(logPGA, socaldata['MMI'], s = 10, c ='r', label = 'Y = PGA')
#plt.scatter(logPGV, socaldata['MMI'], s =10, c ='c', label = 'Y = PGV')

plt.xlim(1e-3,1e4)
#plt.xlim(-3,3)
plt.ylim(1,10)
plt.xlabel('log(Y)')
plt.ylabel('MMI')
plt.xscale('log')
plt.legend(loc='upper left')
plt.title('MMI vs log(Y)') 