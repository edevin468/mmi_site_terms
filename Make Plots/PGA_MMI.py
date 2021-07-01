#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 08:16:31 2020

@author: emmadevin
"""


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/SoCal_withMMIpred.csv')


plt.scatter(df['PGA_g'],df['MMI'] , edgecolors = 'tab:red', facecolors = 'none')
plt.xscale('log')
plt.xlim(1e-4,1e1)
plt.ylim(1,10)
plt.xlabel('PGA')
plt.ylabel('MMI')
# plt.title('MMI vs. PGA')
plt.savefig('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/FinalPlots/MMIPGA.pdf') 