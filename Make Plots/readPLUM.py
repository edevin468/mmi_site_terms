#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:04:23 2020

@author: emmadevin
"""


import pandas as pd
import numpy as np
from textwrap import wrap


FILE1 = '/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/PLUM Results/event_0000000000000001_plum_station_max_observation.dat'
FILE2 = '/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/PLUM Results/event_0000000000000001_plum_station_max_prediction_no_corrections.dat'
FILE3 = '/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/PLUM Results/event_0000000000000001_plum_station_max_prediction_with_corrections.dat'

df1 = pd.read_table(FILE1)
df2 = pd.read_table(FILE2)
df3 = pd.read_table(FILE3)

i = 0

timesteps_o = []
stations_o = []
intensities_o = []
timesteps_n = []
stations_n = []
intensities_n = []
timesteps_w = []
stations_w = []
intensities_w = []

obs = pd.DataFrame()
noC = pd.DataFrame()
withC = pd.DataFrame()

while i < 689:
    
    # CREATE ARRAY FOR OBSERVATIONS
    timestep_o = df1.iloc[i]['Results']
    station_o = df1.iloc[i+1]['Results']
    intensity_o = df1.iloc[i+2]['Results']

    timestep_o = timestep_o[13:]
    station_o = station_o[13:]
    intensity_o = intensity_o[7:]
    
    station_o = station_o.replace(',',' ')
    station_o = station_o.split(' ')
    
    
    intensity_o = intensity_o.replace(',',' ')
    intensity_o = wrap(intensity_o, 3)
    intensity_o = np.array(intensity_o)
    intensity_o = intensity_o.astype('float64')
    
    od = {'stations':station_o,'intensities': intensity_o}
    
    obs= pd.DataFrame(od)

    obs.to_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/PLUM Results/PLUMData/Obs_'+str(timestep_o)+'.csv')
    print('obs:',len(obs))
    #obs = np.array([[timestep_o],[stations_o],[intensities_o]])
    
    
    # CREATE AN ARRAY FOR NO CORRECTION
    timestep_n = df2.iloc[i]['Results']
    station_n = df2.iloc[i+1]['Results']
    intensity_n = df2.iloc[i+2]['Results']
     
    timestep_n = timestep_n[13:]
    station_n = station_n[13:]
    intensity_n = intensity_n[8:]
    
    station_n = station_n.replace(',',' ')
    station_n = station_n.split(' ')


    intensity_n = intensity_n.replace(',',' ')
    intensity_n = wrap(intensity_n, 3)
    intensity_n = np.array(intensity_n)
    intensity_n = intensity_n.astype('float64')
    
    nd = {'stations':station_n,'intensities': intensity_n}

    noC = pd.DataFrame(nd)
    
    noC.to_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/PLUM Results/PLUMData/NoC_'+str(timestep_n)+'.csv')
    print('noC:',len(noC))
    #noC = np.array([[timestep_n],[stations_n],[intensities_n]])
    
    # CREATE AN ARRAY FOR WITH CORRECTION
    timestep_w = df3.iloc[i]['Results']
    station_w = df3.iloc[i+1]['Results']
    intensity_w = df3.iloc[i+2]['Results']
    
    timestep_w = timestep_w[13:]
    station_w = station_w[13:]
    intensity_w = intensity_w[8:]

    station_w = station_w.replace(',',' ')
    station_w = station_w.split(' ')
   
    
    intensity_w = intensity_w.replace(',',' ')
    intensity_w = wrap(intensity_w, 3)
    intensity_w = np.array(intensity_w)
    intensity_w = intensity_w.astype('float64')

    wd = {'stations':station_w,'intensities': intensity_w}

    withC = pd.DataFrame(wd)
    
    withC.to_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/PLUM Results/PLUMData/WithC_'+str(timestep_w)+'.csv')
    print('withC:',len(withC))   
    #withC = np.array([[timestep_w],[stations_w],[intensities_w]])
    
    i += 3 
   




