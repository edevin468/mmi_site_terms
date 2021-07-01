#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:29:42 2020
John Rekoske's code to apply the statsmodels LME model for crossed effects
@author: emmadevin
"""




import os
import pandas as pd
import statsmodels.api as sm

RESID_FILE = '/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_Synthetic/Synthetic_Total_R.csv'
OUTPUT_DIR = '/Users/emmadevin/Work/USGS Work/USGS PLUM/Data/LME_Synthetic/Synthetic_Total_R.csv/LME_Results'

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

df = pd.read_csv(RESID_FILE)
imt_cols = [col for col in df.columns if 'R' in col]

bias_dict = {}
event_term_dict = {}
site_term_dict = {}
epsilon_dict = {}

# Loop over each IMT (period) for FAS
for col in imt_cols:

    # Select subset of the data and remove NaN values
    df_prd = df[['EarthquakeID', 'StationID', col]].copy().dropna()

    # For crossed-effects, we need to put all of the data into the same "group"
    # and specify the variance components. See discussion at
    # https://stackoverflow.com/questions/50052421/mixed-models-with-two-random-effects-statsmodels
    df_prd['group'] = 1
    vcf = {
        'EarthquakeID': '0 + C(EarthquakeID)',
        'StationID': '0 + C(StationID)'
    }

    # Fit the model
    mdf = sm.MixedLM.from_formula(
        '%s ~ 1' % col, groups='group', vc_formula=vcf, data=df_prd).fit()
    print(mdf.summary())

    # Extract bias information
    table = mdf.summary().tables[1]
    bias = float(table['Coef.'][0])
    bias_dict[col] = {
        'c_ci95l': table['[0.025'][0],
        'c': bias,
        'c_ci95u': table['0.975]'][0]}

    # Extract event terms and site terms
    eqids = []
    stids = []
    for idx in mdf.random_effects[1].index:
        id = idx.split(')[')[1].split(']]')[0]
        if 'EarthquakeID' in idx:
            eqids.append(id)
        else:
            stids.append(id)
    mdf.random_effects[1].index = eqids + stids
    event_term_dict[col] = mdf.random_effects[1][:len(eqids)]
    site_term_dict[col] = mdf.random_effects[1][len(eqids):]

    # Extract epilons terms (residuals)
    epsilon_dict[col] = pd.Series(
        mdf.resid.to_numpy(),
        index=[df.iloc[mdf.resid.index]['EarthquakeID'].to_numpy(),
               df.iloc[mdf.resid.index]['StationID'].to_numpy()])

# Save the results
pd.DataFrame.from_dict(bias_dict).to_csv(os.path.join(
    OUTPUT_DIR, 'bias.csv'))
pd.DataFrame.from_dict(event_term_dict).to_csv(os.path.join(
    OUTPUT_DIR, 'event_terms.csv'), index_label='EarthquakeID')
pd.DataFrame.from_dict(site_term_dict).to_csv(os.path.join(
    OUTPUT_DIR, 'site_terms.csv'), index_label='StationID')
pd.DataFrame.from_dict(epsilon_dict).to_csv(os.path.join(
    OUTPUT_DIR, 'epsilons_terms.csv'),
    index_label=['EarthquakeID', 'StationID'])
