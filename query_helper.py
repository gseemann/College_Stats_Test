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
    
#takes a list of tuples and adds them to the db    
def db_insert_uni(uni_tuple_list):
    connect()
    insert_statement = """INSERT IGNORE INTO payscale_colleges(
                   uni,
                   uni_type,
                   early_car_pay,
                   mid_car_pay,
                   high_meaning,
                   stem_deg)
                   VALUES (%s,%s,%s,%s,%s,%s)"""
    cursor.executemany(insert_statement, uni_tuple_list)
    cnx.commit()
    cursor.close()
    cnx.close()
    
#takes uni_dict and converst to list of tules then inserts into the db
def tuple_payscale_uni(uni_dict):
    list_of_tuples = []
    for uni in uni_dict:
        temp_tuple = ()
        temp_tuple = (uni['university'],
              uni['uni_type'],
              uni['early_car_pay'],
              uni['med_car_pay'],
              uni['high_meaning'],
              uni['stem_deg'])
        list_of_tuples.append(temp_tuple)
    db_insert_uni(list_of_tuples)
    
    