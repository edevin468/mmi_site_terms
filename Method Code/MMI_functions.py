#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 09:53:13 2021

convert PGA and PGV values to MMI and compute predicted MMI values from Atkinson IPE, save as  *.csv

@author: emmadevin
"""

import numpy as np
import pandas as pd


def getMMI(PGA,PGV,Magnitude, HypocentralDistance):
    '''
    Calculates MMA and MMV, piecewise 

    Parameters
    ----------
    PGA : array or floating point value
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
    PGAconstants = np.array([0,1.78,1.55,-1.60,3.70,-0.91,1.02,-0.17])
    PGVconstants = np.array([0,3.78,1.47,2.89,3.16,0.90,0.00,-0.18])
    
    
    # computing MMI with PGA and PGV
    MMA_1 =  PGAconstants[1]+PGAconstants[2]*np.log10(PGA) + PGAconstants[5] + PGAconstants[6]*np.log10(HypocentralDistance) + PGAconstants[7]*Magnitude
    
    MMA_2 =  PGAconstants[3]+PGAconstants[4]*np.log10(PGA) + PGAconstants[5] + PGAconstants[6]*np.log10(HypocentralDistance) + PGAconstants[7]*Magnitude
                
    MMV_1 =  PGVconstants[1]+PGVconstants[2]*np.log10(PGV) + PGVconstants[5] + PGVconstants[6]*np.log10(HypocentralDistance) + PGVconstants[7]*Magnitude
    
    MMV_2 =  PGVconstants[3]+PGVconstants[4]*np.log10(PGA) + PGVconstants[5] + PGVconstants[6]*np.log10(HypocentralDistance) + PGVconstants[7]*Magnitude
                
    
    return MMA_1, MMA_2, MMV_1, MMV_2

def computeMMI(dataset):
    '''
    Calculates MMI for all rows in dataset, and creates a new dataset by appending a column for MMI to the 
    original dataset.  
    
    Parameters
    ----------
    dataset : dataframe
        Dataframe containing earthquake data including PGA (in g), PGV (in cm/s), 
        magnitude (Richter scale), and rupture or hypocentral distance (in km).
    newdataset : string
        Name of new file containing old datset plus column for MMI, for example 'DatasetWithMMI.csv'

    Returns
    -------
    None. 
    
    Example
    -------
    getMMIforDataset(SoCalData, 'SoCalDataWithMMI.csv')
    ----> creates new csv file with a column for MMI in current working directory. 
    *specify where the file is saved by adding a file path in the newdataset string

    '''
    
    M = dataset['EarthquakeMagnitude']
    H = dataset['HypocentralDistance']
    
    
    #-------------------------------------------------#
    #  CONVERT PGA/PGV TO MMI                         #
    #-------------------------------------------------#
    
    
    # pull out relavent information from dataset and convert units if necessary (change heading names if necessary)
    pga = dataset['PGA_g']
    pga = pga.replace(-999, None)
    pga = pga*9.8*100
    pgv = dataset['PGV_cms2']
    

    # define constant t2 for both PGA and PGV from Worden et al. Table 1
    aT2 = 4.22
    vT2 = 4.56
    

    # use getMMI to get piecewise values for MMA and MMV 
    mma1, mma2, mmv1, mmv2 = getMMI(pga,pgv,M, H)

    # create boolean arrays to define the parts of the data sets that we need to keep, based on t2 values
    lower_a = mma1<=aT2
    upper_a = mma2>aT2
    lower_v = mma1<=vT2
    upper_v = mma2>vT2

    # use boolean arrays to select the parts we need out of the each array
    mma_lower = mma1[lower_a]
    mma_upper = mma2[upper_a]
    mmv_lower = mma1[lower_v]
    mmv_upper = mma2[upper_v]
    
    # create dataframes
    # PGA/V values must be included here so that the array remains the same length as the dataset
    # MMA/V Lower and MMA/V Upper will be populated with values as determined above where the boolean arrays are true
    # and populated with NaN where boolean arrays are false
    A = pd.DataFrame({'MMA Lower':mma_lower, 'MMA Upper':mma_upper, 'PGA':pga})
    V = pd.DataFrame({'MMV Lower':mmv_lower, 'MMV Upper':mmv_upper, 'PGV':pgv})

    # use mask to merge Lower and Upper into one column
    # take MMA/V Upper column and replace all of its NaN values with corresponding values from MMA/V Lower
    # put this new column into each dataframe as MMA and MMV
    A['MMA']=A['MMA Upper'].mask(pd.isnull, A['MMA Lower'])
    V['MMV']=V['MMV Upper'].mask(pd.isnull, V['MMV Lower'])

    # calculate combined MMI value
    mmi = 0.46*A['MMA'] + 0.52*V['MMV']
        
    # adjust MMI calculated to be less than 1 or greater than 10
    mmi[mmi<1]=1
    mmi[mmi>10]=10

    #-------------------------------------------------#
    #  CALCULATE PREDICTED MMI                        #
    #-------------------------------------------------#
    
    
    
    # define R and B
    R = np.sqrt(H**2 + 14**2)
    B = []
    for i in range(len(R)):
        b = np.max(np.linspace(0,np.log10(R[i]/50), 500))
        B.append(b)
   
    B = np.array(B)
       
    # constants from table 1 Atinson et al.
    c = [0,0.309,1.864,-1.672,-0.00219,1.77,-0.383]
    
    # compute the MMI predicted
    mmi_p = c[1]+c[2]*M+c[3]*np.log10(R)+c[4]*R+c[5]*B+c[6]*M*np.log10(R)
    
    
    #-------------------------------------------------#
    #  COMPUTE RESIDUAL                               #
    #-------------------------------------------------#
    

    # compute total residual
    res = mmi - mmi_p
   
    return mmi, mmi_p, res
   
