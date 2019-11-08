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



def predictHyperlipidemiaNextYearValue(data):
    # in this section we predict the next year value of each features. 
#    to predict next year values this year value and the features used to predict next year value should not be null    
     
    # required columns to predict class status of the patient
    cols=['L100700','S000300','L101700','L100800','L103300','L103100','FIELD_33','FIELD_38','FIELD_40','SEX','AGE']
    

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
        
        
    
#    # predicte next year value    
    predictedNextYearValues=pd.DataFrame()
    predictedNextYearValues['L100700']=np.array(reg_L100700.predict(data[cols_L100700]))
    predictedNextYearValues['S000300']=list(reg_S000300.predict(data[cols_S000300]))
    predictedNextYearValues['L101700']=list(reg_L101700.predict(data[cols_L101700]))
    predictedNextYearValues['L100800']=list(reg_L100800.predict(data[cols_L100800]))
    predictedNextYearValues['L103300']=list(reg_L103300.predict(data[cols_L103300]))
    predictedNextYearValues['L103100']=list(reg_L103100.predict(data[cols_L103100]))
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
    


def predictNextYearHyperlipidemiaClass(data):    
            
    # required columns to predict class status of the patient
    cols=['L100700','S000300','L101700','L100800','L103300','L103100','FIELD_33','FIELD_38','FIELD_40','SEX','AGE']
    
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
    