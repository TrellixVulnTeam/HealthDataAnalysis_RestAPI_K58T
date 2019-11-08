# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:43:39 2019

@author: Henock
"""

import numpy as np
import pandas as pd 
import pickle
import json



def predictHyperlipidemiaClass(data):  
    
    # required columns 
    cols=['AGE','S000300','L100700', 'L100800', 'L100100', "S000501","S000502",'L100200','L101300',
          'L190000','L100400','L101700',"L190300","L190500","L190400",'L101600', 'L105200']
    
#    data=data[cols]
    
    with open('Hyperlipidemia/HyperlipidemiaClassifierModel', 'rb') as f:
        rf = pickle.load(f)
        
    data=data[cols] # extract features from the payload data
    
    #rename the columns to match the orginal model features name
    data.columns=['AGE', 'BMI', 'Uric Acid', 'fasting glucose','L100100','SBP','DBP','L100200','SGPT', 
                 'L190000','L100400','r-GTP gamma', 'RBC', 'HCT','Hemoglobin', 'L101600', 'L105200']
    
    # compute class probability
    classprobapred= pd.DataFrame(rf.predict_proba(data), columns=['CLASS 0','CLASS 1']).to_json(orient='index')
    
    # compute class value
    classpred=pd.DataFrame(rf.predict(data),columns=['CLASS']).to_json(orient='index')
    
    RESULT = {
      "Class value": json.loads(classpred),
      "Class probability": json.loads(classprobapred) 
    }
    
    # convert into JSON: 
#    RESULT=json.dumps(RESULT)
    
    
    return RESULT#(data.to_json(orient='index')) 


