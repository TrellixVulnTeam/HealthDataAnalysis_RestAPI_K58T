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




def predictIschemiaNextYearValue(data):
    # in this section we predict the next year value of each features. 
#    to predict next year values this year value and the features used to predict next year value should not be null    
     
    # required columns to predict class status of the patient
    cols=['AGE','FIELD_1','FIELD_15','FIELD_2','FIELD_33','FIELD_38',
            'FIELD_4','L100200','L100500','L100700','L100800','L101200','L101300',
            'L101600','L101700','L102900','L103000','L103100','L103200','L103300',
            'L104300','L104400','L104500','L190000','L190300','L190400','L190500',
            'L190600','L190700','L190800','L190900','L504700','S000100','S000300',
            'S000501','S000502','SEX']   
                
    data=data[cols]
    
#    'L100700','S000300','L101700','L103300','L103100','L190900','L504700','L190300','L103000','FIELD_15','FIELD_38','FIELD_33','SEX','AGE','CLASS'
    
                   
    #Load the trained regression models for the next year
    with open('Ischemia/Models_NextYear/ISchemiaModel_nextyear_L100700_RF_regressor', 'rb') as f:
        reg_L100700 = pickle.load(f)
        
    with open('Ischemia/Models_NextYear/ISchemiaModel_nextyear_S000300_RF_regressor', 'rb') as f:
        reg_S000300 = pickle.load(f)
        
    with open('Ischemia/Models_NextYear/ISchemiaModel_nextyear_L101700_RF_regressor', 'rb') as f:
        reg_L101700 = pickle.load(f)
        
    with open('Ischemia/Models_NextYear/ISchemiaModel_nextyear_L103300_RF_regressor', 'rb') as f:
        reg_L103300 = pickle.load(f)        
        
    with open('Ischemia/Models_NextYear/ISchemiaModel_nextyear_L103100_RF_regressor', 'rb') as f:
        reg_L103100 = pickle.load(f)
        
    with open('Ischemia/Models_NextYear/ISchemiaModel_nextyear_L190900_RF_regressor', 'rb') as f:
        reg_L190900 = pickle.load(f)
        
    with open('Ischemia/Models_NextYear/ISchemiaModel_nextyear_L504700_RF_regressor', 'rb') as f:
        reg_L504700= pickle.load(f)
        
    with open('Ischemia/Models_NextYear/ISchemiaModel_nextyear_L190300_RF_regressor', 'rb') as f:
        reg_L190300 = pickle.load(f)                      
        
    with open('Ischemia/Models_NextYear/ISchemiaModel_nextyear_L103000_RF_regressor', 'rb') as f:
        reg_L103000 = pickle.load(f)
        
        
#    with open('Ischemia/Models_NextYear/ISchemiaModel_nextyear_L103000_RF_regressor', 'rb') as f:
#        reg_L101700 = pickle.load(f)
    
#    # predicte next year value    
    predictedNextYearValues=pd.DataFrame()
    predictedNextYearValues['L100700']=list(reg_L100700.predict(data[['L100700', 'SEX', 'S000300', 'L103000', 'L103100', 'L103300','S000501', 'S000100', 'L101300', 'L190300', 'L100500', 'L101700']]))
    predictedNextYearValues['S000300']=list(reg_S000300.predict(data[['S000300', 'SEX', 'L103300', 'S000501','L103100', 'L101300', 'S000502','L190300', 'L190400', 'L100700', 'L103000', 'L100800']]))
    predictedNextYearValues['L101700']=list(reg_L101700.predict(data[['L101700', 'SEX', 'L101300', 'FIELD_38', 'S000300', 'L101200','L100700', 'L190400', 'L103000', 'L103300', 'L190300', 'L100800']])) 
    predictedNextYearValues['L103300']=list(reg_L103300.predict(data[['L103300', 'L103100', 'L103000', 'L103200', 'S000300', 'L102900', 'SEX','L100700', 'L190300', 'L190400', 'L190500', 'L100500','AGE']]))
    predictedNextYearValues['L103100']=list(reg_L103100.predict(data[['L103100', 'L103300', 'SEX', 'S000300', 'L103000', 'L190300','L100700', 'L190400', 'L190500', 'L100500', 'S000100', 'L101300']]))
    predictedNextYearValues['L190900']=list(reg_L190900.predict(data[['L190900', 'L190700', 'L104500', 'L190800', 'L190600', 'L190400', 'L190500', 'L104300', 'L104400', 'S000100', 'L100200']]))
    predictedNextYearValues['L504700']=list(reg_L504700.predict(data[['L504700', 'AGE','L101700', 'FIELD_4', 'L100800','S000100', 'L103300', 'L101600', 'L100700', 'S000501', 'FIELD_38']]))
    predictedNextYearValues['L190300']=list(reg_L190300.predict(data[['L190300', 'L190500', 'L190400', 'L103100', 'S000300','L100700', 'L103300', 'S000100', 'L103000', 'S000501', 'S000502']]))
    predictedNextYearValues['L103000']=list(reg_L103000.predict(data[['L103000', 'L100700', 'L101700', 'S000300', 'S000502', 'FIELD_33','L190000', 'L100800', 'L101600', 'S000501']]))
    predictedNextYearValues['FIELD_15']=list(data['FIELD_15'])
    predictedNextYearValues['FIELD_38']=list(data['FIELD_38'])
    predictedNextYearValues['FIELD_33']=list(data['FIELD_33'])
    predictedNextYearValues['SEX']=list(data['SEX'])
    predictedNextYearValues['AGE']=list(data['AGE']+1)      
#    predictedNextYearValues=predictedNextYearValues[cols]
#    
    # load the classifer model   
    with open('Ischemia/Models_NextYear/ISchemia_nextyear_RF_classifier', 'rb') as f:
        _nextyearData_RF_Clf = pickle.load(f)
            
    
    # compute class probability
    classprobapred= pd.DataFrame(_nextyearData_RF_Clf.predict_proba(predictedNextYearValues), columns=['CLASS 0','CLASS 1']).to_json(orient='index')
    
    # compute class value
    classpred=pd.DataFrame(_nextyearData_RF_Clf.predict(predictedNextYearValues),columns=['CLASS']).to_json(orient='index')
    
    RESULT = {
      "Next Year Value": json.loads(predictedNextYearValues.to_json(orient='index')),
      "Class value": json.loads(classpred),
      "Class probability": json.loads(classprobapred) 
    }
        
    
    return RESULT #data.to_json(orient='index')
    
