#!/usr/bin/env python
# coding: utf-8

# In[25]:


import config
import json
import requests
api_key = config.API_key
import time 
import datetime
import mysql.connector
from mysql.connector import errorcode
import pandas as pd



# In[26]:


def connect():
    global cnx
    cnx = mysql.connector.connect(
    host = config.host,
    user = config.user,
    passwd = config.password,
    database = 'colleges')
    global cursor
    cursor = cnx.cursor()


# In[9]:

#pass in a SELECT * FROM colleges and it returns results in a pandas dataframe
def query(query_string):
    connect()
    cursor = cnx.cursor()
    
    cursor.execute(query_string)
    return cursor.fetchall()


#pass in a SELECT * FROM colleges and it returns results in a pandas dataframe
def query_to_df(query_string):
    connect()
    cursor = cnx.cursor()
    
    cursor.execute(query_string)
    
    df = pd.DataFrame(cursor.fetchall())
    df.columns = [x[0] for x in cursor.description]
    return df