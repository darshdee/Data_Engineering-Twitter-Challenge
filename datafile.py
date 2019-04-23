# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:45:42 2019

@author: Darshil Desai
"""


import json
import pandas as pd
from twython import Twython  
import re
import os, datetime, time

# Loading in the credentials 
with open("twitter_credentials.json", "r") as file:      
    creds = json.load(file)

def get_data(query):  
    """
    Requests and extracts the data twitter. Returns a clean dataframe     
    """
    # Instantiate an object
    python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
    
    # Create our query
    query = {'q': query,  
            'result_type': 'popular',
            'count': 20,
            'lang': 'en',
            'truncated': 'False'
            }    
    
    # Search tweets
    dict_ = {'user': [], 
             'description': [],          
             'date': [], 
             'username': [],
             'location': [],
             'text': [], 
             'favorite_count': []}  
    
    all_tweets = python_tweets.search(**query)['statuses']
    
    for status in all_tweets:    ## Requesting Here
        dict_['user'].append(status['user']['screen_name'])
        dict_['description'].append(status['user']['description'])
        dict_['date'].append(status['created_at'])
        dict_['username'].append(status['user']['name'])    
        dict_['location'].append(status['user']['location'])
        dict_['text'].append(status['text'])
        dict_['favorite_count'].append(status['favorite_count'])
    
    
    # Creating a pandas dataframe to structure the data received
    df = pd.DataFrame(dict_)  
    df.sort_values(by='favorite_count', inplace=True, ascending=False)  
    return df




