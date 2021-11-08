#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:42:17 2021
example ShakeAlert map product w/ Atkinson et al. IPE and VS30 scaling terms
Northridge event
@author: emmadevin
"""

import numpy as np
import pandas as pd



# event information
M = 6.7
depth = 18.2 #km
eventlat = 34.213
eventlon = -118.537

# grid information
grid_data = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/EEW Example/ShakeAlert_MapProduct_Grid_Northridge_061121.csv')
gridlat = grid_data['lat']
gridlon = grid_data['lon']
gridVS30 = grid_data['VS30']
epidist = grid_data['EpiDist']

hypodist = np.sqrt(depth**2 + epidist**2) 

R = np.sqrt(hypodist**2 + 14**2)
B = []
for i in range(len(R)):
    b = np.max(np.linspace(0,np.log10(R[i]/50), 500))
    B.append(b)
B = np.array(B)
   
# constants from table 1 Atinson et al.
c = [0,0.309,1.864,-1.672,-0.00219,1.77,-0.383]

# calculate site terms using VS30
Vc = 951
siteterm = []

for Vs30 in gridVS30:
    if Vs30 <= Vc:
        st = -0.000499*Vs30 + 0.22
    elif Vs30 > Vc:
        st = 8.49e-16*Vs30 + 2.54
    
    siteterm.append(st)
    
siteterm = np.array(siteterm)

# compute the MMI for each grid cell
gridMMI_st = c[1]+c[2]*M+c[3]*np.log10(R)+c[4]*R+c[5]*B+c[6]*M*np.log10(R) + siteterm
gridMMI = c[1]+c[2]*M+c[3]*np.log10(R)+c[4]*R+c[5]*B+c[6]*M*np.log10(R)


# save data
grid_data['siteterm'] = siteterm
grid_data['MMI_st'] = gridMMI_st
grid_data['MMI'] = gridMMI

grid_data.to_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/EEW Example/ShakeAlert_Northridge_Predicted_MMI.csv')





