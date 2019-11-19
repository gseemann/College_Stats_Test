#imports personal details to connect to db
import config
#import our function files
import query_helper
import payscale_uni_webscrape


import json
import requests
from bs4 import BeautifulSoup
api_key = config.API_key
import time 
import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import statistics
import math
import scipy.stats as stats
from scipy import stats
from statsmodels.stats.power import TTestIndPower

db_name = 'colleges'
## Connect to DB server on AWS
## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
cnx = mysql.connector.connect(
    host = config.host,
    user = config.user,
    passwd = config.password,
    database = "colleges"       #says what database we expect everything loaded into
)
cursor = cnx.cursor()

def create_database(cursor, database):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(db_name))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(db_name))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor, db_name)
        print("Database {} created successfully.".format(db_name))
        cnx.database = db_name
    else:
        print(err)
        exit(1)
        
#query to create table
#write a query entry to creat a table
payscale_colleges = """
CREATE TABLE payscale_colleges (
      uni varchar(100) PRIMARY KEY,
      uni_type varchar(100),
      early_car_pay int,
      mid_car_pay int,
      high_meaning float,
      stem_deg float
    );
"""

#calls queery in query_helper.py
query_helper.create_table(payscale_colleges)


