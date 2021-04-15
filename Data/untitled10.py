# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:11:29 2021

@author: wajee
"""

from function import PM25_2015,PM25_2016,PM25_2017,PM25_2018,PM25_2019,PM25_2020

import requests
import sys
import pandas as pd
import os
import csv
from bs4 import BeautifulSoup

def met_data(month, year):
    file_html = open('Data/Html_Data/{}/{}.html'.format(year,month), 'rb')
    plain_text = file_html.read()

    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)

    rows = len(tempD) / 15

    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)

    length = len(finalD)

    finalD.pop(length - 1)
    finalD.pop(0)

    for a in range(len(finalD)):
        finalD[a].pop(14)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        #finalD[a].pop(6)
        finalD[a].pop(4)
        finalD[a].pop(0)

    return finalD

def data_combine(year, cs):
    for a in pd.read_csv('Data/Extract-Data/ex_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


if __name__ == "__main__":
    if not os.path.exists("Data/Extract-Data"):
        os.makedirs("Data/Extract-Data")
    for year in range(2015, 2021):
        final_data = []
        with open('Data/Extract-Data/ex_' + str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(
                ['T', 'TM', 'Tm', 'H', 'PP','VV', 'V', 'VM', 'PM 2.5'])
        for month in range(1, 13):
            temp = met_data(month, year)
            final_data = final_data + temp
            
        pm = getattr(sys.modules[__name__], 'PM25_{}'.format(year))()

        

        for i in range(len(final_data)):
            # final[i].insert(0, i + 1)
            final_data[i].insert(8, pm[i])

        with open('Data/Extract-Data/ex_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
                    wr.writerow(row)
            
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
    data_2017 = data_combine(2017, 600)
    data_2018 = data_combine(2018, 600)
    data_2019 = data_combine(2019, 600)
    data_2020 = data_combine(2020, 600) 
    
    total=data_2015+data_2016+data_2017+data_2018+data_2019+data_2020
    
    with open('Data/Extract-Data/ext_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm', 'H', 'PP','VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
        
        
df=pd.read_csv('Data/Extract-Data/ext_Combine.csv')
        
    
           
                    
                
                
                