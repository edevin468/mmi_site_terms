#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:58:47 2020

@author: emmadevin
"""


import pandas as pd
import numpy as np


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

dMMI1 = wi-oi
dMMI1 = dMMI1.dropna()

dMMI2 = ni-oi
dMMI2 = dMMI2.dropna()

a['dMMI no correction'] = dMMI2
a['dMMI with correction'] = dMMI1

df = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_withMMIpred.csv')

lat,long, network, stationcode = df['StationLatitude'], df['StationLongitude'], df['Network'], df['StationCode']

station = (network + '.' + stationcode)


locations = pd.DataFrame([station, lat, long])
locations = locations.transpose()
locations = locations.rename(columns = {'Unnamed 0': 'stations'})

a = locations.merge(a, how='inner',indicator=False)
a = a.drop_duplicates(subset = ['stations'])
a = a.reset_index()


a.to_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/PLUM Results/dMMI/dMMI_Locations.csv')




