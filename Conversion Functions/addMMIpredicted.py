#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:08:26 2020

@author: EmmaDevin
"""


import pandas as pd
import MMI_Predicted as mp

socal = pd.read_csv('/Users/EmmaDevin/USGS PLUM/Data/SoCal_withMMI.csv')

mp.getMMIPredicted(socal, '/Users/EmmaDevin/USGS PLUM/Data/SoCal_withMMIpred.csv')