#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:22:22 2021

@author: emmadevin
"""

import matplotlib.pyplot as plt 
import pandas as pd
from matplotlib.transforms import offset_copy
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt

df = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/EEW Example/ShakeAlert_Northridge_Predicted_MMI.csv')

# Create a Stamen Terrain instance.
stamen_terrain = cimgt.Stamen(style='terrain')

# Create a GeoAxes in the tile's projection.
ax = plt.axes(projection=stamen_terrain.crs)

# Limit the extent of the map to a small longitude/latitude range.
ax.set_extent([-117, -119, 33, 35])

# Add the Stamen data at zoom level 8.
ax.add_image(stamen_terrain, 10)

# Add a marker for the Eyjafjallajökull volcano.
# plt.plot(-19.613333, 63.62, marker='o', color='red', markersize=12,
#          alpha=0.7, transform=ccrs.Geodetic())

# # Use the cartopy interface to create a matplotlib transform object
# # for the Geodetic coordinate system. We will use this along with
# # matplotlib's offset_copy function to define a coordinate system which
# # translates the text by 25 pixels to the left.
# geodetic_transform = ccrs.Geodetic()._as_mpl_transform(ax)
# text_transform = offset_copy(geodetic_transform, units='dots', x=-25)

# # Add text 25 pixels to the left of the volcano.
# plt.text(-19.613333, 63.62, u'Eyjafjallajökull',
#          verticalalignment='center', horizontalalignment='right',
#          transform=text_transform,
#          bbox=dict(facecolor='sandybrown', alpha=0.5, boxstyle='round'))
# plt.show()


am