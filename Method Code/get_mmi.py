#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 09:46:32 2021

@author: emmadevin
"""

import pandas as pd
import MMI_functions as m

working_dir = '/Users/EmmaDevin/Work/USGS Summer 2020/USGS PLUM/Data'


# read data
df = pd.read_csv(working_dir + '/PGA_PGV/Revised_PGA_PGV_data.csv')

mmi, mmi_p, res = m.computeMMI(df)


df['mmi'] = mmi
df['mmi_predicted'] = mmi_p
df['mmi_res'] = res

df.to_csv(working_dir + '/MMI/MMI_data.csv')