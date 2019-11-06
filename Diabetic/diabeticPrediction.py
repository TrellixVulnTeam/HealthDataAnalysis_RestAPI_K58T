
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 23:19:25 2019

@author: Henock
""" 
import numpy as np
import pandas as pd 
import pickle
import json
 

def predictDiabeticClass(data):    
            
    # required columns 
    cols=['L104600','L103000','S000300','L101700','SEX','AGE',
          'L100700','FIELD_33','FIELD_38','FIELD_40','FIELD_31']
    
#    data=data[cols]
    
    with open('Diabetic/DiabeticClassifierModel', 'rb') as f:
        rf = pickle.load(f)
        
    data=data[cols] # extract features from the payload data
    
    #rename the columns to match the orginal model features name
    data.columns=['HBA1C', 'Triglycerides', 'BMI', 'r-GTP gamma', 'SEX', 'AGE', 'Uric Acid', 
                  '_4_1_Smoking', 'Drinking_5_1_days', '_6_1_of_physical_activity_high_strength', 'Family_history']
    
    # compute class probability
    classprobapred= pd.DataFrame(rf.predict_proba(data), columns=['CLASS 0','CLASS 1','CLASS 2']).to_json(orient='index')
    
    # compute class value
    classpred=pd.DataFrame(rf.predict(data),columns=['CLASS']).to_json(orient='index')
    
    RESULT = {
      "Class value": json.loads(classpred),
      "Class probability": json.loads(classprobapred) 
    }
    
    # convert into JSON: 
#    RESULT=json.dumps(RESULT)
    
    
    return RESULT#(data.to_json(orient='index'))
    
    


    