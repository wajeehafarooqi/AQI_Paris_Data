# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:00:48 2021

@author: wajee
"""

import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app = Flask(__name__)
model =pickle.load(open('C://Users/wajee/OneDrive/Bureau/projects/Paris_AQI/Data/Model/Random_forest.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

