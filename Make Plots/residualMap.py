#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:51:23 2020

@author: emmadevin
"""

import os
import sys
import pandas as pd
import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

#os.environ["CARTOPY_USER_BACKGROUNDS"] = "/home/opt/anaconda3/lib/python3.7/site-packages/cartopy/data/raster/natural_earth"

bias = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal/bias.csv')
siteTerms = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal/site_terms.csv')
eventTerms = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_SoCal/event_terms.csv')

dataset = pd.read_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SoCal_withMMIpred.csv')

locations = dataset[['StationID','StationLatitude','StationLongitude']]
locations =  locations.drop_duplicates(subset = 'StationID')    
locations = locations.reset_index()





df = locations.merge(siteTerms, how='inner',indicator=False)

low = df['TotalResidual']>-1 
high = df['TotalResidual']<1

df1 = df[low]
df1 = df1[high]

lon = df1['StationLongitude']
lat = df1['StationLatitude']
site = df1['TotalResidual']

data_crs = ccrs.PlateCarree()

# s = site
# S = np.array(site)
# S1 = S.reshape(len(lon), len(lat))
# S2 = np.transpose(S1)
SiteTermsCoordinates = pd.DataFrame()

SiteTermsCoordinates['lat']=lat
SiteTermsCoordinates['lon']=lon
SiteTermsCoordinates['site']=site

SiteTermsCoordinates.to_csv('/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/SiteTermsCoord.csv')

ax = plt.axes(projection=ccrs.PlateCarree())
#ax.background_img(name='BM', resolution='low')
#ax.stock_img()
ax.set_global()
ax.coastlines()
ax.set_xticks([-125,-120,-119,-118,-117,-116,-115,-110], crs=ccrs.PlateCarree())
ax.set_yticks([-90, -60, -30, 0, 30,33,34,35,40,45, 60, 90], crs=ccrs.PlateCarree())
ax.set_extent([-119, -117.5, 33.5, 34.5], crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
plt.scatter(lon, lat, s = 4, transform=data_crs, c=site, cmap='seismic')
#plt.contour(lon, lat, S2, cmap='seismic')
cbar = plt.colorbar()
cbar.set_label('Site Term')
#cbar.set_clim(-1.0, 1.0)
plt.title('Map of LA with Site Terms')
plt.scatter(-118.2437, 33.9522, s = 6000, facecolors = 'none', edgecolors = 'k', label = 'LA')

