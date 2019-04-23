# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:45:29 2019

@author: Darshil Desai
"""

import json
import pandas as pd
from twython import Twython  
import re
import os, datetime, time

from datafile import get_data
from preprocess import write_tweets, write_hashtags, write_texts, write_username

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
"""
Main
"""

all_tweets = get_data('climate change')


def write_each_dir(df,date):        
        
    """
    Creates a project directory for each year and date depending on the file being processed
    
    Parameters
    -----------
    : date: the dates
    
    """
    
    # subset the dataframe
    df1 = df[(df.date.dt.year.isin([int(date[:4])])) & (df.date.dt.month.isin([int(date[5:])]))] 
    
    # Make the main dir frame
    if not os.path.exists("{d}".format(d = date)):

        # Maing all the directories
        os.makedirs("{d}".format(d = date))

        # write all the files        
        write_tweets(date = date, df1=df1)
        write_hashtags(date = date, df1=df1) 
        write_texts(date = date, df1= df1) 
        write_username(date = date, df1=df1)
        
    else:
        # write all the files 
        write_tweets(date = date, df1=df1)
        write_hashtags(date = date, df1=df1) 
        write_texts(date = date, df1= df1) 
        write_username(date = date, df1=df1)
        
                                      

def write_into_folders(df, date_col):
    """
    This is when the files are actually written into

    Parameters
    ------------------
    :df : a dataframe containing the twitter data
    :date_col: specify which column the date is so the directories can be made accordingly     
    """
    
    # Convert into date columns
    df.date = pd.to_datetime(df[date_col])
    all_dates = (df['date'].dt.strftime("%Y/%m").drop_duplicates().tolist())
    
    # Iterate over each unique year/date combination 
    for date in all_dates:    
        write_each_dir(df = df, date=date)
        
write_into_folders(df = all_tweets, date_col = 'date')



