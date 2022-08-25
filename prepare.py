import numpy as np
import pandas as pd
import datetime



def filter_students(df):
    
    # remove staff by cohort name
    std = df.where(df['cohort_name'] != 'Staff').dropna()
    
    # create mask to filter amount of times accessed to 10 or below
    mask = std['user_id'].value_counts()
    std10less = std[std['user_id'].isin(mask.index[mask<11])]
    
    # create mask to filter by times accessed when students were active
    std10less['date_mask'] = std10less.index >= pd.Timestamp('2019-11-04')
    std_final = std10less.mask(std10less['date_mask'] == False).dropna()
    
    # send it
    return std_final