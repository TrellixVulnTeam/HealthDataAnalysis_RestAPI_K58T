# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:30:29 2019

@author: Henock
"""

import numpy as np
import pandas as pd 
import pickle
import json



def predictIschemiaClass(data):
    
            
    # required columns 
    cols=['AGE','S000300','FIELD_15','L190900','L103300','L504700','L190300',
          'L103100','L100700','FIELD_33','FIELD_38','SEX','L103000','L101700']
        
    with open('Ischemia/ISchemicClassifierModel_rf', 'rb') as f:
        rf = pickle.load(f)
        
    data=data[cols] # extract features from the payload data
    
    #rename the columns to match the orginal model features name
    data.columns=['AGE', 'BMI', 'FIELD_15', 'L190900','Cardiac risk factor', 
                  'L504700', 'RBC','HDL-Cholesterol', 'Uric Acid', 
                  '_4_1_Smoking', 'Drinking_5_1_days', 'SEX',
                  'Triglycerides','r-GTP gamma']
    
    # compute class probability
    classprobapred= pd.DataFrame(rf.predict_proba(data), columns=['CLASS 0','CLASS 1']).to_json(orient='index')
    
    # compute class value
    classpred=pd.DataFrame(rf.predict(data),columns=['CLASS']).to_json(orient='index')
    
    RESULT = {
      "Class value": json.loads(classpred),
      "Class probability": json.loads(classprobapred) 
    }
    
    return RESULT#(data.to_json(orient='index'))