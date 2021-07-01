#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 08:57:10 2020

@author: EmmaDevin
"""
import pandas as pd
import convertToMMI as m

# read dataset
socaldata = pd.read_csv('/Users/EmmaDevin/USGS PLUM/Data/SoCal_EQ_Data_for_Emma.csv')

# run function on dataset and saves it into Data directory
# will update existing file of that name if there is one
A, V, mmi = m.getMMIforDataset(socaldata, '/Users/EmmaDevin/USGS PLUM/Data/SoCal_withMMI.csv')

