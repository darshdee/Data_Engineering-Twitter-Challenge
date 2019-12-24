# Data Engineering Twitter Challenge

This project is a result of a time constrained data-engineering challenge wherein I was tasked with developing a data pipeline, using Twitter data, to satisfy the following challegne requirements:
- 1. __Extract__: Extract tweets pertaining to a certain topic of interest from Twitter. I chose "climate change"
- 2. __Transform__: Clean, wrangle & aggregate the resulting data. This step primarily encompassed extracting key information from the tweets such as author name, hashtag, raw text,etc. Followed by also performing aggregations such as counts.
- 2. __Load__: Lastly, the resulting data is saved in dynamically created directories named after the year-month the tweets are uploaded. Example: Data pertaining to tweets in March 2019 will automatically be loaded in a dir path named "2019/03" and so on

This challenge, as you might have perhaps guessed, represents a simplified version of an production level ETL process. My skillset in "ETLing" is built on this understanding & I have moved on to employ production level data pipelines using Apache Airflow.

Thank you for reading!