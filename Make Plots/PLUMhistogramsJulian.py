#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:28:12 2020
Make histograms of PLUM results
@author: Julian Bunn
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


RESULTS_DIR = '/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/PLUM Results/LaHabra/'
# RESULTS_DIR = '/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/PLUM Results/Ridgecrest'


def main():

    obs_lines = open(RESULTS_DIR+'/event_0000000000000001_plum_station_max_observation.dat').readlines()
    pred_lines = open(RESULTS_DIR+'/event_0000000000000001_plum_station_max_prediction_no_corrections.dat').readlines()
    
    # obs_lines = open(RESULTS_DIR+'/Ridgecrest_event_0000000000000001_plum_station_max_observation.dat').readlines()
    # pred_lines = open(RESULTS_DIR+'/Ridgecrest_event_0000000000000001_plum_station_max_prediction_no_corrections.dat').readlines()

    obs_stations = obs_lines[-2].strip().split(':')[1]
    obs_mmis = obs_lines[-1].strip().split(':')[1]   

    pred_stations = pred_lines[-2].strip().split(':')[1]
    pred_mmis = pred_lines[-1].strip().split(':')[1]  

    observations = {}
    for stat,mmi in zip(obs_stations.split(','), obs_mmis.split(',')):
        observations[stat] = float(mmi)


    predictions = {}
    for stat,mmi in zip(pred_stations.split(','), pred_mmis.split(',')):
        predictions[stat] = float(mmi)


    errors = []

    for stat,mmi in observations.items():
        pred = predictions[stat]
        print (stat, mmi, pred)
        errors.append( pred-mmi )

    avg = np.median(errors)
    stdev = np.std(errors)
    
    fig = plt.figure(figsize = (10,5))
    # fig.suptitle('PLUM Predicted Intensity With and Without Site Terms - La Habra', fontsize = 25)
    
    fs = 12
    props = dict(boxstyle='square', facecolor='lightgrey', alpha=1)
    
    plt.subplot(121)
    n, bins, patches = plt.hist(errors, bins=10, color= 'tab:blue', label = 'Median = %5.2f' % (avg))
    plt.grid(True)
    plt.title('WITHOUT station corrections', fontsize=fs)
    plt.xlabel('Predicted minus observed MMI', fontsize = fs)
    # plt.legend(fontsize = fs)  
    plt.text(2.6,28,'median = %5.2f' % (avg),bbox = props)
    # plt.text(1.7,110,'median = %5.2f' % (avg),bbox = props)
    plt.ylim(0,31)
    
    
    obs_lines = open(RESULTS_DIR+'/event_0000000000000001_plum_station_max_observation.dat').readlines()
    pred_lines = open(RESULTS_DIR+'/event_0000000000000001_plum_station_max_prediction_with_corrections.dat').readlines()
    
    # obs_lines = open(RESULTS_DIR+'/Ridgecrest_event_0000000000000001_plum_station_max_observation.dat').readlines()
    # pred_lines = open(RESULTS_DIR+'/Ridgecrest_event_0000000000000001_plum_station_max_prediction_with_corrections.dat').readlines()

    obs_stations = obs_lines[-2].strip().split(':')[1]
    obs_mmis = obs_lines[-1].strip().split(':')[1]   

    pred_stations = pred_lines[-2].strip().split(':')[1]
    pred_mmis = pred_lines[-1].strip().split(':')[1]  

    observations = {}
    for stat,mmi in zip(obs_stations.split(','), obs_mmis.split(',')):
        observations[stat] = float(mmi)


    predictions = {}
    for stat,mmi in zip(pred_stations.split(','), pred_mmis.split(',')):
        predictions[stat] = float(mmi)


    errors = []

    for stat,mmi in observations.items():
        pred = predictions[stat]
        print (stat, mmi, pred)
        errors.append( pred-mmi )

    avg = np.median(errors)
    stdev = np.std(errors)
   
    
    plt.subplot(122)
    n, bins, patches = plt.hist(errors, bins=10, color= 'navy',label = 'Median = %5.2f' % (avg))
    plt.grid(True)
    plt.title('WITH station corrections', fontsize=fs)
    plt.xlabel('Predicted minus observed MMI', fontsize = fs)
    # plt.legend(fontsize = fs)
    plt.text(2.6,28,'median = %5.2f' % (avg),bbox = props)
    # plt.text(1.9,110,'median = %5.2f' % (avg),bbox = props)
    plt.ylim(0,31)
    plt.savefig('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/FinalPlots/HistogramLaHabra.pdf') 
    # plt.savefig('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/FinalPlots/HistogramRidgecrest.pdf') 
    
    
    
    
if __name__ == '__main__':
    main()