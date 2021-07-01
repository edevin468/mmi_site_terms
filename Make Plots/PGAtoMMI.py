#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 09:43:38 2020

@author: EmmaDevin
"""


# function for calculating MMI and producing an updated dataset including those values

def getMMI(dataSet): 
    '''
    

    Parameters
    ----------
    dataSet : TYPE: dataframe 
        DESCRIPTION: Contains all earthquake data including magnitude, PGA, hypocentral distance etc.

    Returns
    -------
    newdataSet: TYPE: dataframe
        DESCRIPTION: An updated data frame with a column for MMI.

    '''
    
    