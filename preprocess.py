# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:47:12 2019

@author: Darshil Desai
"""
import json
import pandas as pd


def write_tweets(date, df1):
    
    # appending to the tweets file            
    with open('{d}/texts.txt'.format(d=date), 'a') as file:
        for x in df1.text:
            file.write('Tweet : {} \n'.format(x))        

#--------------------------------------------------
            
def write_texts(date, df1):    
           
    # writing all tweet texts in the txt
    with open('{d}/tweets.txt'.format(d=  date), 'a') as file:
        for index, status in df1.iterrows(): 
            json.dump( {'Text': status['text'] , 'Description': status['description'] }, file, indent=2)

#--------------------------------------------------
            
def write_hashtags(date, df1):                
    # empty list 
    all_hashtags = []
    
    # ALL hashtags into one hashtag column
    df1.all_hashtags = pd.concat([df1.description.str.findall(r'#.*?(?=\s|$)') , df1.text.str.findall(r'#.*?(?=\s|$)')])
        
    for x,y in zip(df1.text.str.findall(r'#.*?(?=\s|$)'),df1.description.str.findall(r'#.*?(?=\s|$)')):  # finding all the hashtags
                                 try:
                                     all_hashtags.append("".join(e for e in x[0] if e.isalpha()))
                                     all_hashtags.append("".join(e for e in y[0] if e.isalpha()))                                 
                                 except:
                                     pass
    
    with open('{d}/hashtags.txt'.format(d=date), 'a') as file:
        for h,x in pd.DataFrame(pd.Series(all_hashtags).value_counts(dropna=True)).iterrows():
            file.write('#{h} : {c} \n'.format(h=h,c =x[0] ))
                             
#--------------------------------------------------
            
def write_username(date, df1):
    # username counts
    with open('{d}/username.txt'.format(d = date), 'a') as file:
        for h,x in pd.DataFrame(df1.username.value_counts(dropna=False)).iterrows():
            file.write('@{h} : {c} \n'.format(h=h,c =x[0] ))               
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            