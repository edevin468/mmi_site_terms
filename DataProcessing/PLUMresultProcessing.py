#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:15:55 2020
Compute IDW + Site Terms to compare with ShakeMap
@author: emmadevin
"""
import numpy as np
import pandas as pd


RESULTS_DIR = '/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/PLUM Results/Ridgecrest/'

obs_lines = open(RESULTS_DIR+'/Ridgecrest_event_0000000000000001_plum_station_max_observation.dat').readlines()
pred_lines1 = open(RESULTS_DIR+'/Ridgecrest_event_0000000000000001_plum_station_max_prediction_with_corrections.dat').readlines()
pred_lines2 = open(RESULTS_DIR+'Ridgecrest_event_0000000000000001_plum_station_max_prediction_no_corrections.dat').readlines()

obs_stations = obs_lines[-2].strip().split(':')[1]
obs_mmis = obs_lines[-1].strip().split(':')[1]   

pred_stations1 = pred_lines1[-2].strip().split(':')[1]
pred_mmis1 = pred_lines1[-1].strip().split(':')[1]  

pred_stations2 = pred_lines2[-2].strip().split(':')[1]
pred_mmis2 = pred_lines2[-1].strip().split(':')[1]  

observations = {}
for stat,mmi in zip(obs_stations.split(','), obs_mmis.split(',')):
    observations[stat] = float(mmi)


predictions1 = {}
for stat,mmi in zip(pred_stations1.split(','), pred_mmis1.split(',')):
    predictions1[stat] = float(mmi)
    
predictions2 = {}
for stat,mmi in zip(pred_stations2.split(','), pred_mmis2.split(',')):
    predictions2[stat] = float(mmi)


errors1 = []
errors2 = []
predicted1 = []
predicted2 = []
mmis = []
station = []

for stat,mmi in observations.items():
    pred1 = predictions1[stat]
    print (stat, mmi, pred1)
    errors1.append( pred1-mmi )
    predicted1.append(pred1)
    mmis.append(mmi)
    station.append(stat)
    
for stat,mmi in observations.items():
    pred2 = predictions2[stat]
    print (stat, mmi, pred2)
    errors2.append( pred2-mmi )
    predicted2.append(pred2)

avg1 = np.median(errors1)
stdev1 = np.std(errors1)

avg2 = np.median(errors1)
stdev2 = np.std(errors1)

d = {'observed' : mmis, 'nocorrection' : predicted1, 'withcorrection': predicted2, 'stations': station, 'errorwithout' : errors1, 'errorwith' : errors2}

df = pd.DataFrame(d)

loc = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SiteTermsUpdated.csv')

loc['stations'] = loc['Network']+'.'+loc['StationCode']

df2 = loc.merge(df)

df2.to_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/PLUM Results/Ridgecrest/dMMI/dMMI_Locations2.csv')

