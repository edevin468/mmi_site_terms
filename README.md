# mmi_site_terms

To calculate MMI site terms from dataset of PGA/PGV ground motion data
All scripts in Method Code directory

Step 1: 
  fix_stn_codes.py
  Fix issue with upper/lower case station codes

Step 2:
  get_mmi.py
  call functions from MMI_functions.py to compute MMI from PGA and PGV, predicted MMI, and MMI residual
  
Step 3:
  data_filtering.py
  filter data if desired to only include large MMI and stations with certain number of earthquakes
  
Step 4:
  LME.py
  preform linear mixed effects analysis to obtain site, event, and epsilon terms, along with bias values
  
Step 5: 
  site_terms_dataset.py
  put results into pretty dataframe for PLUM team to work with
  
  
