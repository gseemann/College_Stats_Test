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

#creates connection, all functions will start by calling this
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
    results = cursor.fetchall()
    #close out db connection
    cursor.close()
    cnx.close()
    return results


#pass in a SELECT * FROM colleges and it returns results in a pandas dataframe
def query_to_df(query_string):
    connect()
    cursor = cnx.cursor()
    
    cursor.execute(query_string)
    
    df = pd.DataFrame(cursor.fetchall())
    df.columns = [x[0] for x in cursor.description]
    
    cursor.close()
    cnx.close()
    return df

#pass in a create table statement will, if table does not exist it will be created
def create_table(query):
    connect()
    
    try:
        print("Creating a new table")
        cursor.execute(query)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

    cursor.close()
    cnx.close()