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
    
    try:
        # required columns 
        
        cols=['AGE','SEX', 'L100700', 'S000300','L101700', 'L100800', 'L101300',   'L190300', 'L190500', 
                 'FIELD_33','FIELD_38','FIELD_40']
         
        with open('Hyperlipidemia/HyperlipidemiaClassifierModel', 'rb') as f:
            rf = pickle.load(f)
            
        data=data[cols] # extract features from the payload data
        
        #rename the columns to match the orginal model features name
        data.columns=['AGE', 'SEX', 'Uric Acid', 'BMI', 'r-GTP gamma', 'fasting glucose','SGPT', 'RBC', 'HCT', '_4_1_Smoking', 'Drinking_5_1_days',
       '_6_1_of_physical_activity_high_strength']
        
        # compute class probability
        classprobapred= pd.DataFrame(rf.predict_proba(data), columns=['CLASS 0','CLASS 1']).to_json(orient='index')
        
        # compute class value
        classpred=pd.DataFrame(rf.predict(data),columns=['CLASS']).to_json(orient='index')
        
        RESULT = {
          "Class value": json.loads(classpred),
          "Class probability": json.loads(classprobapred) 
        }
        
        return RESULT#(data.to_json(orient='index')) 
    
    except Exception as e: 
        return ((str(e))+ ' Required Fields: ' +', '.join(str(x) for x in cols)) 
           



def predictHyperlipidemiaNextYearValue(data):
    
    try:
        # in this section we predict the next year value of each features. 
    #    to predict next year values this year value and the features used to predict next year value should not be null    
         
        # required columns to predict class status of the patient
        cols=['L190500', 'L190300', 'L101300','L100700', 'S000300', 'L101700', 'L100800','L103300', 'L103100',
          'FIELD_33', 'FIELD_38', 'FIELD_40','SEX', 'AGE']
        
    
    #    features required to generate next year L100700 value
        cols_L100700=['L100700', 'SEX', 'S000300', 'L103000', 'L103100', 'L103300', 'S000501', 
    'S000100', 'L101300', 'L190300', 'L100500', 'L101700']
        
    #    features required to generate next year S000300 value
        cols_S000300=['S000300', 'SEX', 'L103300', 'S000501','L103100', 'L101300', 'S000502', 
    'L190300', 'L190400', 'L100700', 'L103000', 'L100800']
        
    #    features required to generate next year L101700 value
        cols_L101700=['L101700', 'SEX', 'L101300', 'FIELD_38', 'S000300', 'L101200', 
    'L100700', 'L190400', 'L103000', 'L103300', 'L190300', 'L100800',]
        
    #    features required to generate next year L100800 value
        cols_L100800=['L100800', 'L104600', 'SEX', 'AGE', 'L101300', 'S000300', 
    'L103000', 'L103300', 'S000501', 'S000502', 'L101700', 'FIELD_38']    
        
    #    features required to generate next year L103300 value
        cols_L103300=['L103300', 'L103100', 'L103000', 'L103200', 'S000300', 'L102900', 
    'SEX','L100700', 'L190300', 'L190400', 'L190500', 'L100500']
        
    #    features required to generate next year L103100 value
        cols_L103100=['L103100', 'L103300', 'SEX', 'S000300', 'L103000', 'L190300', 
    'L100700', 'L190400', 'L190500', 'L100500', 'S000100', 'L101300']
        
        
        
    #    features required to generate next year L100800 value
        cols_L101300=['L101300', 'SEX', 'S000300', 'L101200', 'L103300', 'L101700',
       'L100700', 'L103100', 'L190400', 'L190300', 'S000100', 'L190500'] 
        
    #    features required to generate next year L103300 value
        cols_L190300=['L190300', 'SEX', 'L190500', 'L190400', 'L103100', 'S000300',
       'L100700', 'L103300', 'S000100', 'L103000', 'S000501', 'S000502' ]
        
    #    features required to generate next year L103100 value
        cols_L190500=['L190500', 'SEX',  'L190400', 'L190300', 'L104500', 'L190800',
       'S000300', 'L100700', 'L103100', 'S000100', 'S000502', 'S000501']
        
        
        
        
        #Load the trained regression models for the next year
        with open('Hyperlipidemia/Models_NextYear/hyperlipidemiaModel_nextyear_L100700_RF_regressor', 'rb') as f:
            reg_L100700 = pickle.load(f)
            
        with open('Hyperlipidemia/Models_NextYear/hyperlipidemiaModel_nextyear_S000300_regressor', 'rb') as f:
            reg_S000300 = pickle.load(f)
            
        with open('Hyperlipidemia/Models_NextYear/hyperlipidemiaModel_nextyear_L101700_RF_regressor', 'rb') as f:
            reg_L101700 = pickle.load(f)        
            
        with open('Hyperlipidemia/Models_NextYear/hyperlipidemiaModel_nextyear_L100800_RF_regressor', 'rb') as f:
            reg_L100800 = pickle.load(f)
            
        with open('Hyperlipidemia/Models_NextYear/hyperlipidemiaModel_nextyear_L103300_RF_regressor', 'rb') as f:
            reg_L103300 = pickle.load(f)
            
        with open('Hyperlipidemia/Models_NextYear/hyperlipidemiaModel_nextyear_L103100_RF_regressor', 'rb') as f:
            reg_L103100 = pickle.load(f)
            
            
            
        with open('Hyperlipidemia/Models_NextYear/hyperlipidemiaModel_nextyear_L101300_RF_regressor', 'rb') as f:
            reg_L101300 = pickle.load(f)
            
        with open('Hyperlipidemia/Models_NextYear/hyperlipidemiaModel_nextyear_L190300_RF_regressor', 'rb') as f:
            reg_L190300 = pickle.load(f)
            
        with open('Hyperlipidemia/Models_NextYear/hyperlipidemiaModel_nextyear_L190500_RF_regressor', 'rb') as f:
            reg_L190500 = pickle.load(f)
            
            
        
    #    # predicte next year value    
        predictedNextYearValues=pd.DataFrame()
        predictedNextYearValues['L100700']=np.array(reg_L100700.predict(data[cols_L100700]))
        predictedNextYearValues['S000300']=list(reg_S000300.predict(data[cols_S000300]))
        predictedNextYearValues['L101700']=list(reg_L101700.predict(data[cols_L101700]))
        predictedNextYearValues['L100800']=list(reg_L100800.predict(data[cols_L100800]))
        predictedNextYearValues['L103300']=list(reg_L103300.predict(data[cols_L103300]))
        predictedNextYearValues['L103100']=list(reg_L103100.predict(data[cols_L103100]))
        
        predictedNextYearValues['L101300']=list(reg_L101300.predict(data[cols_L101300]))
        predictedNextYearValues['L190300']=list(reg_L190300.predict(data[cols_L190300]))
        predictedNextYearValues['L190500']=list(reg_L190500.predict(data[cols_L190500]))
        
        predictedNextYearValues['SEX']=list(data['SEX'])
        predictedNextYearValues['AGE']=list(data['AGE']+1)
        predictedNextYearValues['FIELD_33']=list(data['FIELD_33'])
        predictedNextYearValues['FIELD_38']=list(data['FIELD_38'])
        predictedNextYearValues['FIELD_40']=list(data['FIELD_40'])      
        predictedNextYearValues=predictedNextYearValues[cols]
        
        # load the classifer model and the feature scaller  
        with open('Hyperlipidemia/Models_NextYear/HyperlipidemiaModelClassifierModelForNextYear_rf_model', 'rb') as f:
            _nextyearData_RF_Clf = pickle.load(f)
            
        with open('Hyperlipidemia/Models_NextYear/HyperlipidemiaClassifierModelForNextYear_scaler_SMOTE', 'rb') as f:
            _nextyearData_scaler = pickle.load(f)
                        
        scaledData= _nextyearData_scaler.transform(predictedNextYearValues)
        
        
        # compute class probability
        classprobapred= pd.DataFrame(_nextyearData_RF_Clf.predict_proba(scaledData), columns=['CLASS 0','CLASS 1']).to_json(orient='index')
        
        # compute class value
        classpred=pd.DataFrame(_nextyearData_RF_Clf.predict(scaledData),columns=['CLASS']).to_json(orient='index')
        
        RESULT = {
          "Next Year Value": json.loads(predictedNextYearValues.to_json(orient='index')),
          "Class value": json.loads(classpred),
          "Class probability": json.loads(classprobapred) 
        }
            
        
        return RESULT
    
    except Exception as e:
        return ((str(e))+ ' Required Fields: '+ ', '.join(str(x) for x in 
                 np.unique(np.concatenate((cols_L100700,cols_S000300,cols_L101700,
                cols_L100800,cols_L103300,cols_L103100,cols_L101300,cols_L190300,cols_L190500)))                 
                 ))
                 


def predictNextYearHyperlipidemiaClass(data):  
    
    try:            
        # required columns to predict class status of the patient
#        cols=['L100700','S000300','L101700','L100800','L103300','L103100','FIELD_33','FIELD_38','FIELD_40','SEX','AGE']
        cols=['L190500', 'L190300', 'L101300','L100700', 'S000300', 'L101700', 'L100800','L103300', 'L103100',
          'FIELD_33', 'FIELD_38', 'FIELD_40','SEX', 'AGE']
        
        # extract features from the payload data
        data=data[cols]
        
        # load the classifer model and the feature scaller  
        with open('Hyperlipidemia/Models_NextYear/HyperlipidemiaModelClassifierModelForNextYear_rf_model', 'rb') as f:
            _nextyearData_RF_Clf = pickle.load(f)
            
        with open('Hyperlipidemia/Models_NextYear/HyperlipidemiaClassifierModelForNextYear_scaler_SMOTE', 'rb') as f:
            _nextyearData_scaler = pickle.load(f)
            
        scaledData= _nextyearData_scaler.transform(data)    
        
        # compute class probability
        classprobapred= pd.DataFrame(_nextyearData_RF_Clf.predict_proba(scaledData), columns=['CLASS 0','CLASS 1']).to_json(orient='index')
        
        # compute class value
        classpred=pd.DataFrame(_nextyearData_RF_Clf.predict(scaledData),columns=['CLASS']).to_json(orient='index')
        
        RESULT = {
          "Class value": json.loads(classpred),
          "Class probability": json.loads(classprobapred) 
        }
        
        return RESULT#(data.to_json(orient='index'))
        
    except Exception as e:
        return ((str(e))+ ' Required Fields: '+ ', '.join(str(x) for x in cols)) 
    