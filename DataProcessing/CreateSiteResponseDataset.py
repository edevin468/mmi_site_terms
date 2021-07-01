#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:02:37 2020

@author: emmadevin
"""


import pandas as pd
import numpy as np

bias = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal/bias.csv')
siteTerms = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal/site_terms.csv')
eventTerms = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal/event_terms.csv')

dataset = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_withMMIpred.csv')

locations = dataset[['Network','StationCode','StationID','StationLatitude','StationLongitude']]
locations =  locations.drop_duplicates(subset = 'StationCode')    
#locations = locations.reset_index()

df = locations.merge(siteTerms, how='inner',indicator=False)


df.to_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SiteTermsUpdated.csv')