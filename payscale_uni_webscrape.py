#Payscale Universities Scraping with Beautiful Soup

# import config
# import query_helper
import json
import requests
from bs4 import BeautifulSoup
# api_key = config.API_key
# import time 
# import mysql.connector
# from mysql.connector import errorcode
# import pandas as pd
# import query_helper


#set up iterator to got through pages
def get_pages(web_page_iterator):

    web_addrs = "https://www.payscale.com/college-salary-report/bachelors/page/{}".format(str(web_page_iterator))

    #get first page and go through results
    page = requests.get(web_addrs)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup_1 = soup.find('tbody')
    soup_uni_names = soup_1.find_all(class_="datatable-logo__text")
    uni_names = [uni.get_text() for uni in soup_uni_names]
    soup_uni_type = soup_1.find_all(class_="pxl-hidden-sm-down text-center")
    uni_type = [i.get_text() for i in soup_uni_type]

    #create a dictionary for the current list of items were looking at
    list_of_dict = []
    temp_dict_ ={}
    for i in uni_names:
        temp_dict_['university']=i
        list_of_dict.append(temp_dict_.copy())  

    #add all the variables to each respective universities dictionary
    i = -1 #use this to control iteration thru list_of_dict
    for counter, value in enumerate(uni_type):
        if counter%6==0:
            i+=1 #iterate to next college in list
            continue
        elif(counter%6==1):
            list_of_dict[i]['uni_type']=value
        elif(counter%6==2):
            list_of_dict[i]['early_car_pay']= (int((value.strip('$').replace(',',''))))
        elif(counter%6==3):
            list_of_dict[i]['med_car_pay']=(int((value.strip('$').replace(',',''))))
        elif(counter%6==4):
            if value =='N/A':
                list_of_dict[i]['high_meaning']= 0
            else:
                list_of_dict[i]['high_meaning']= float(value.strip('%'))
        else:
            list_of_dict[i]['stem_deg']= float(value.strip('%'))
                
    return list_of_dict

