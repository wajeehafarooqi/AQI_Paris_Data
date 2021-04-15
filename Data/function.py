# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:00:25 2021

@author: wajee
"""

import pandas as pd



def PM25_2015():
       df = pd.read_csv("D://wajeeha/research-19-03-2021/paris_pm2.5/data_2015.csv")
       #df['pm2.5']=df['PM 2.5'].astype(float)
       df_2015=df['PM 2.5']
       dt_2015 = df_2015.values.tolist()
       return dt_2015

def PM25_2016():
       df = pd.read_csv("D://wajeeha/research-19-03-2021/paris_pm2.5/data_2016.csv")
       #df['pm2.5']=df['PM 2.5'].astype(float)
       df_2016=df['PM 2.5']
       dt_2016 = df_2016.values.tolist()
       return dt_2016

def PM25_2017():
       df = pd.read_csv("D://wajeeha/research-19-03-2021/paris_pm2.5/data_2017.csv")
       #df['pm2.5']=df['PM 2.5'].astype(float)
       df_2017=df['PM 2.5']
       dt_2017 = df_2017.values.tolist()
       return dt_2017

def PM25_2018():
       df = pd.read_csv("D://wajeeha/research-19-03-2021/paris_pm2.5/data_2018.csv")
       #df['pm2.5']=df['PM 2.5'].astype(float)
       df_2018=df['PM 2.5']
       dt_2018 = df_2018.values.tolist()
       return dt_2018

def PM25_2019():
       df = pd.read_csv("D://wajeeha/research-19-03-2021/paris_pm2.5/data_2019.csv")
       #df['pm2.5']=df['PM 2.5'].astype(float)
       df_2019=df['PM 2.5']
       dt_2019 = df_2019.values.tolist()
       return dt_2019
   
def PM25_2020():
       df = pd.read_csv("D://wajeeha/research-19-03-2021/paris_pm2.5/data_2020.csv")
       #df['pm2.5']=df['PM 2.5'].astype(float)
       df_2020=df['PM 2.5']
       dt_2020 = df_2020.values.tolist()
       return dt_2020

if __name__=='__main__':
    PM25_2015()
    PM25_2016()
    PM25_2017()
    PM25_2018()
    PM25_2019()
    PM25_2020()