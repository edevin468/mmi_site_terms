#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:09:28 2021

@author: emmadevin
"""
from progress_bar import progress_bar

l = 100
bar = progress_bar(l)



for i in range(l):
    
    b = 100*999/47*i
    
    bar.get_progress(i)
    
    
    
