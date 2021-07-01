#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 09:43:38 2020

@author: EmmaDevin
"""
import pandas as pd
import numpy as np

# function for calculating MMI and producing an updated dataset including those values

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
        