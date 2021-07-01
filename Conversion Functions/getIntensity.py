#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 08:33:04 2020

@author: EmmaDevin
"""


import numpy as np

def getMMI(PGA,PGV,Magnitude, HypocentralDistance):
    '''
    

    Parameters
    ----------
    PGA : array or floatin point value
        Peak Ground Accelation (in cm/s).
    PGV : array or floating point value
        Peak Ground Velocity (in cm/s).
    Magnitude : array or floating point value
        Magnitude in Richter scale.
    HypocentralDistance : array or floating point value
        Distance away from hypocenter in cm.

    Returns
    -------
    MMA_1, MMA_2, MMV_1, MMV_2 : arrays or floating point values
        The modified Mercalli intensities calculated with PGA and PGV piecewise 

    '''
    
    # contants from Worden et al. tables 1 and 2
    PGAconstants = np.array([1.78,1.55,-1.60,3.70,-0.91,1.02,-0.17])
    PGVconstants = np.array([3.78,1.47,2.89,3.16,0.90,0.00,-0.18])
    
    
    # computing MMI with PGA and PGV
    MMA_1 =  PGAconstants[0]+PGAconstants[1]*np.log10(PGA) + PGAconstants[4] + PGAconstants[5]*np.log10(HypocentralDistance) + PGAconstants[6]*Magnitude
    
    MMA_2 =  PGAconstants[2]+PGAconstants[3]*np.log10(PGA) + PGAconstants[4] + PGAconstants[5]*np.log10(HypocentralDistance) + PGAconstants[6]*Magnitude
                
    MMV_1 =  PGVconstants[0]+PGVconstants[1]*np.log10(PGV) + PGVconstants[4] + PGVconstants[5]*np.log10(HypocentralDistance) + PGVconstants[6]*Magnitude
    
    MMV_2 =  PGVconstants[2]+PGVconstants[3]*np.log10(PGA) + PGVconstants[4] + PGVconstants[5]*np.log10(HypocentralDistance) + PGVconstants[6]*Magnitude
                
    
    return MMA_1, MMA_2, MMV_1, MMV_2

def getMMIforDataset(dataset):
    
    
    # pull out relavent information from dataset (change heading names if necessary)
    pga = dataset['PGA_g']
    pga = pga.replace(-999, None)
    pga = pga/9.8*100
    pgv = dataset['PGV_cms2']
    M = dataset['EarthquakeMagnitude']
    H = dataset['HypocentralDistance']*100*1000

    # define constant t2 for both PGA and PGV from Worden et al. Table 1
    aT2 = 4.22
    vT2 = 4.56

    # initialize variable to store MMI values
    MMI=[]

    # for each index value , call the function getMII and assign its output to peicewise define MMA and MMV 
    for i in range(len(pga)):
        #for i in range(1):
        mma1, mma2, mmv1, mmv2 = getMMI(pga[i],pgv[i], M[i], H[i])

        # determine, based on t2 values, which of the value to assign to MMA and MMV (eq 6 Worden et al.)
        if (mma1<= aT2):
            MMA = (mma1)
        elif (mma2>aT2):
            MMA = (mma2)

        if (mmv1<= vT2):
            MMV = (mmv1)
        elif (mmv2>vT2):
            MMV = (mmv2)
        
        # compute MMI from MMA and MMV (eq 9 Worden et al)
        mmi = 0.46*MMA + 0.52*MMV
    
        # append MMI value to list to store
        MMI.append(mmi)
    
    # assign list of MMI values to column in dataset
    dataset['MMI']= MMI

