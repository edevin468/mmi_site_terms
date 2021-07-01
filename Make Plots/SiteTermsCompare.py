#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:48:00 2020

@author: emmadevin
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

dfm1 = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/Compiled_Instrumental_Site_Terms.csv')
dfm2 = pd.read_csv('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/Data/SiteResponse.csv')


siteMMI = dfm2[['StationCode','site']]
df = dfm1.merge(siteMMI)

fs = 12

x = np.linspace(-2,3, 20)
y = x

fig = plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.plot(x,y,'--', c = 'b', label='Line with slope of 1')
plt.scatter(df['site'],df['Site_Term_PGV'],s = 10,edgecolors = 'gray', facecolors ='none', label ='MMI vs PGV Site Term')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms', fontsize = 20)
plt.xlabel('MMI derived site term', fontsize = fs)
plt.ylabel('Ground Motion derived site term', fontsize = fs)
plt.legend(fontsize = fs)

plt.subplot(122)
plt.plot(x,y,'--', c = 'b', label='Line with slope of 1')
plt.scatter(df['site'],df['Site_Term_PGA'],s = 10,edgecolors = 'gray', facecolors ='none', label ='MMI vs PGA Site Term')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms', fontsize = 20)
plt.xlabel('MMI derived site term', fontsize = fs)
plt.ylabel('Ground Motion derived site term', fontsize = fs)
plt.legend( fontsize = fs)
fig.tight_layout()
plt.savefig('/Users/emmadevin/Work/USGS Summer 2020/USGS PLUM/FinalPlots/SiteTermsComparePG.pdf') 
#plt.scatter(siteAll['site'],siteAll['Site_Term_PGV'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PGV Site Term')

# plt.subplot(223)
# plt.plot(x,y,'--', c = 'b', label='Line with m = 1')
# plt.scatter(siteAll['site'],siteAll['Site_Term_PSA_0.01s'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PSA 0.01s Site Term')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms')
# plt.xlabel('MMI derived site term')
# plt.ylabel('Ground Motion derived site term')
# plt.legend()

# plt.subplot(224)
# plt.plot(x,y,'--', c = 'b', label='Line with m = 1')
# plt.scatter(siteAll['site'],siteAll['Site_Term_PSA_10s'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PSA 10s Site Term')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms')
# plt.xlabel('MMI derived site term')
# plt.ylabel('Ground Motion derived site term')
# plt.legend()

# df1  = df[['site','Site_Term_PSA_0.01s']]
# df2  = df[['site','Site_Term_PSA_0.03s']]
# df3  = df[['site','Site_Term_PSA_0.05s']]
# df4  = df[['site','Site_Term_PSA_0.1s']]
# df5  = df[['site','Site_Term_PSA_0.5s']]
# df6  = df[['site','Site_Term_PSA_1s']]
# df7  = df[['site','Site_Term_PSA_3s']]
# df8  = df[['site','Site_Term_PSA_5s']]
# df9  = df[['site','Site_Term_PSA_10s']]

# df1  = df1.dropna()
# df2  = df2.dropna()
# df3  = df3.dropna()
# df4  = df4.dropna()
# df5  = df5.dropna()
# df6  = df6.dropna()
# df7  = df7.dropna()
# df8  = df8.dropna()
# df9  = df9.dropna()



# plt.subplot(331)
# plt.plot(x,y,'--', c = 'b', label='Line with m = 1')
# plt.scatter(df1['site'],df1['Site_Term_PSA_0.01s'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PSA 0.01s Site Term')
# slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(df1['site'],df1['Site_Term_PSA_0.01s'])
# x1 = np.linspace(-3,3, 10)
# y1 = slope1*x1 + intercept1
# plt.plot(x1,y1,'--', c = 'r', label='Least Squares Fit to Data')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms')
# plt.xlabel('MMI derived site term')
# plt.ylabel('Ground Motion derived site term')
# plt.legend()
# plt.savefig('/Users/emmadevin/Work/USGS Work/USGS PLUM/PDF Plots/SiteTermPSACompare.pdf') 

# plt.subplot(332)
# plt.plot(x,y,'--', c = 'b', label='Line with m = 1')
# plt.scatter(df2['site'],df2['Site_Term_PSA_0.03s'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PSA 0.03s Site Term')
# slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(df2['site'],df2['Site_Term_PSA_0.03s'])
# x2 = np.linspace(-3,3, 10)
# y2 = slope2*x2 + intercept2
# plt.plot(x2,y2,'--', c = 'r', label='Least Squares Fit to Data')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms')
# plt.xlabel('MMI derived site term')
# plt.ylabel('Ground Motion derived site term')
# plt.legend()

# #plt.scatter(siteAll['site'],siteAll['Site_Term_PGV'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PGV Site Term')

# plt.subplot(333)
# plt.plot(x,y,'--', c = 'b', label='Line with m = 1')
# plt.scatter(df3['site'],df3['Site_Term_PSA_0.05s'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PSA 0.05s Site Term')
# slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(df3['site'],df3['Site_Term_PSA_0.05s'])
# x3 = np.linspace(-3,3, 10)
# y3 = slope3*x3 + intercept3
# plt.plot(x3,y3,'--', c = 'r', label='Least Squares Fit to Data')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms')
# plt.xlabel('MMI derived site term')
# plt.ylabel('Ground Motion derived site term')
# plt.legend()

# plt.subplot(334)
# plt.plot(x,y,'--', c = 'b', label='Line with m = 1')
# plt.scatter(df4['site'],df4['Site_Term_PSA_0.1s'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PSA 1s Site Term')
# slope4, intercept4, r_value4, p_value4, std_err4 = stats.linregress(df4['site'],df4['Site_Term_PSA_0.1s'])
# x4 = np.linspace(-3,3, 10)
# y4 = slope4*x4 + intercept4
# plt.plot(x4,y4,'--', c = 'r', label='Least Squares Fit to Data')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms')
# plt.xlabel('MMI derived site term')
# plt.ylabel('Ground Motion derived site term')
# plt.legend()

# plt.subplot(335)
# plt.plot(x,y,'--', c = 'b', label='Line with m = 1')
# plt.scatter(df5['site'],df5['Site_Term_PSA_0.5s'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PSA 1s Site Term')
# slope5, intercept5, r_value5, p_value5, std_err5 = stats.linregress(df5['site'],df5['Site_Term_PSA_0.5s'])
# x5 = np.linspace(-3,3, 10)
# y5 = slope5*x5 + intercept5
# plt.plot(x5,y5,'--', c = 'r', label='Least Squares Fit to Data')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms')
# plt.xlabel('MMI derived site term')
# plt.ylabel('Ground Motion derived site term')
# plt.legend()

# plt.subplot(336)
# plt.plot(x,y,'--', c = 'b', label='Line with m = 1')
# plt.scatter(df6['site'],df6['Site_Term_PSA_1s'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PSA 1s Site Term')
# slope6, intercept6, r_value6, p_value6, std_err6 = stats.linregress(df6['site'],df6['Site_Term_PSA_1s'])
# x6 = np.linspace(-3,3, 10)
# y6 = slope6*x6 + intercept6
# plt.plot(x6,y6,'--', c = 'r', label='Least Squares Fit to Data')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms')
# plt.xlabel('MMI derived site term')
# plt.ylabel('Ground Motion derived site term')
# plt.legend()

# plt.subplot(337)
# plt.plot(x,y,'--', c = 'b', label='Line with m = 1')
# plt.scatter(df7['site'],df7['Site_Term_PSA_3s'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PSA 1s Site Term')
# slope7, intercept7, r_value7, p_value7, std_err7 = stats.linregress(df7['site'],df7['Site_Term_PSA_3s'])
# x7 = np.linspace(-3,3, 10)
# y7 = slope7*x7 + intercept7
# plt.plot(x7,y7,'--', c = 'r', label='Least Squares Fit to Data')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms')
# plt.xlabel('MMI derived site term')
# plt.ylabel('Ground Motion derived site term')
# plt.legend()


# plt.subplot(338)
# plt.plot(x,y,'--', c = 'b', label='Line with m = 1')
# plt.scatter(df8['site'],df8['Site_Term_PSA_5s'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PSA 5s Site Term')
# slope8, intercept8, r_value8, p_value8, std_err8 = stats.linregress(df8['site'],df8['Site_Term_PSA_5s'])
# x8 = np.linspace(-3,3, 10)
# y8 = slope8*x8 + intercept8
# plt.plot(x8,y8,'--', c = 'r', label='Least Squares Fit to Data')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms')
# plt.xlabel('MMI derived site term')
# plt.ylabel('Ground Motion derived site term')
# plt.legend()

# plt.subplot(339)
# plt.plot(x,y,'--', c = 'b', label='Line with m = 1')
# plt.scatter(df9['site'],df9['Site_Term_PSA_10s'],edgecolors = 'gray', facecolors ='none', label ='MMI vs PSA 10s Site Term')
# slope9, intercept9, r_value9, p_value9, std_err9 = stats.linregress(df9['site'],df9['Site_Term_PSA_10s'])
# x9 = np.linspace(-3,3, 10)
# y9 = slope9*x9 + intercept9
# plt.plot(x9,y9,'--', c = 'r', label='Least Squares Fit to Data')
# plt.title('Correspondence of MMI and Ground Motion Derived Site Terms')
# plt.xlabel('MMI derived site term')
# plt.ylabel('Ground Motion derived site term')
# plt.legend()
# plt.savefig('/Users/emmadevin/Work/USGS Work/USGS PLUM/PDF Plots/SiteTermPSACompare.pdf') 

# fig.tight_layout()

# fig2 = plt.figure()

# slopes = [slope1,slope2,slope3,slope4,slope5,slope6,slope7,slope8,slope9]
# t = [0.01,0.03,0.05,0.1,0.5,1,3,5,10]    
# plt.scatter(t, slopes, edgecolors = 'r', facecolors ='none')
# plt.xlabel('Period of PSA')
# plt.ylabel('Slope')
# plt.title('Slope of Fitted Lines vs Period of PSA')
# plt.savefig('/Users/emmadevin/Work/USGS Work/USGS PLUM/PDF Plots/SlopesSiteTerms.pdf') 


# stdDev =[std_err1*np.sqrt(len(df1)),std_err2*np.sqrt(len(df1)),std_err3*np.sqrt(len(df1)),
#          std_err4*np.sqrt(len(df1)),std_err5*np.sqrt(len(df1)),std_err6*np.sqrt(len(df1)),
#          std_err7*np.sqrt(len(df1)),std_err8*np.sqrt(len(df1)),std_err9*np.sqrt(len(df1))]


# fig3 = plt.figure()
# plt.plot(t, stdDev)
# #plt.ylim(0,0.001)
# plt.xscale('log')
# plt.title('Standard Deviation vs Period of PSA')
# plt.xlabel('Period of PSA')
# plt.ylabel('Standard Deviation')



