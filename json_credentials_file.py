# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:31:16 2019

@author: Darshil Desai
"""

# json credentials file

import json

# Enter your keys/secrets as strings in the following fields
credentials = {}  
credentials['CONSUMER_KEY'] = 'aQC27lWkDHtfIlsAko56i7G9c'  
credentials['CONSUMER_SECRET'] = 'RyQhjqIrmKNLeKhv9fvnXlEILoU0pX9CVwuocqA1btxgcw4rLY'
credentials['ACCESS_TOKEN'] = 'ooiTIlYV9bDRLeY4F2YqB06OUKBCcRlZNTG4lJoz'  
credentials['ACCESS_SECRET'] = 'UmFA2prFV056rxu7tlEa2OHnNlPG7943pIfavAA5Bhlsn'

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:  
    json.dump(credentials, file)
    
    
    
    