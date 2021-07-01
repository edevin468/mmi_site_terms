#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:03:48 2020

@author: EmmaDevin
"""


import numpy as np
import pandas as pd

def getMMIPredicted(dataset, newdataset):
    '''
    

    Parameters
    ----------
    dataset : dataframe
        current earthquake dataset.
    newdataset : string
        path and file name for updated datset.

    Returns
    -------
    MMI Predicted

    '''
    
    # load magnitudes, and hypocentral distances from input dataset
    M = dataset['EarthquakeMagnitude']
    D = dataset['HypocentralDistance']
    
    # define R and B
    R = np.sqrt(D**2 + 14**2)
    B = []
    for i in range(len(R)):
        b = np.max(np.linspace(0,np.log10(R[i]/50), 500))
        B.append(b)
    B = np.array(B)
       
    # constants from table 1 Atinson et al.
    c = [0,0.309,1.864,-1.672,-0.00219,1.77,-0.383]
    
    # compute the MMI predicted
    MMIp = c[1]+c[2]*M+c[3]*np.log10(R)+c[4]*R+c[5]*B+c[6]*M*np.log10(R)
    
    # add predicted MMI to dataset
    dataset['PredictedMMI']= MMIp

    # compute total residual
    totalResidual = dataset['MMI']-dataset['PredictedMMI']
    
    # add total residual to dataset
    dataset['TotalResidual'] = totalResidual
    
    # save dataset to newdataset
    dataset.to_csv(newdataset)
    
    return MMIp