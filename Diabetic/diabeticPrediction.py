
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
    

def predictNextYearDiabeticClass(data):    
            
    # required columns 
#    cols=['L104600','L103000','S000300','L101700','SEX','AGE',
#          'L100700','FIELD_33','FIELD_38','FIELD_40','FIELD_31']
    
    # extract features from the payload data
    data=data[['L104600','L103000','S000300','L101700','L100700','FIELD_33',
               'FIELD_38','FIELD_40','FIELD_31','SEX','AGE']]
    
    # load the classifer model and the feature scaller  
    with open('Diabetic/Models_NextYear/DiabeticClassifierModelForNextYear_rf_model_SMOTE', 'rb') as f:
        _nextyearData_RF_Clf = pickle.load(f)
        
    with open('Diabetic/Models_NextYear/DiabeticClassifierModelForNextYear_scaler_SMOTE', 'rb') as f:
        _nextyearData_scaler = pickle.load(f)
        
    scaledData= _nextyearData_scaler.transform(data)    
    
    # compute class probability
    classprobapred= pd.DataFrame(_nextyearData_RF_Clf.predict_proba(scaledData), columns=['CLASS 0','CLASS 1','CLASS 2']).to_json(orient='index')
    
    # compute class value
    classpred=pd.DataFrame(_nextyearData_RF_Clf.predict(scaledData),columns=['CLASS']).to_json(orient='index')
    
    RESULT = {
      "Class value": json.loads(classpred),
      "Class probability": json.loads(classprobapred) 
    }
    
    return RESULT#(data.to_json(orient='index'))
    

def predictDiabeticNextYearValue(data):
    # in this section we predict the next year value of each features. 
#    to predict next year values this year value and the features used to predict next year value should not be null    
     
    # required columns to predict class status of the patient
    cols=['L104600','L103000','S000300','L101700','L100700',
          'SEX','AGE','FIELD_33','FIELD_38','FIELD_40','FIELD_31']

#    features required to generate next year L104600 value
    cols_L104600=["L104600","L100800","S000300","AGE","L101300","S000501","L101700","S000502",
            "L190000","L101600","L190300"]
    
#    features required to generate next year L103000 value
    cols_L103000=["L103000","L100700","L101700","S000300","S000502",
                  "FIELD_33","L190000","L100800","L101600","S000501"]
    
#    features required to generate next year S000300 value
    cols_S000300=["S000300","L103300","S000501","L100700","SEX",
                  "L103100","L190300","L190400","L101300","S000502",]
    
#    features required to generate next year L101700 value
    cols_L101700=["L101700","L101300","L103000","SEX","L100700","L101200","S000300",
                  "S000501","L100800","S000502","L101600","S000100",]    
    
#    features required to generate next year L100700 value
    cols_L100700=["L100700","L100500","S000100","S000300","L103300","L103000",
                  "L103100","S000501","L101300","L101700","S000502","L107400",]
    
    
    #Load the trained regression models for the next year
    with open('Diabetic/Models_NextYear/DiabeticModel_nextyear_L104600_RF_regressor', 'rb') as f:
        reg_L104600 = pickle.load(f)
        
    with open('Diabetic/Models_NextYear/DiabeticModel_nextyear_L103000_RF_regressor', 'rb') as f:
        reg_L103000 = pickle.load(f)
        
    with open('Diabetic/Models_NextYear/DiabeticModel_nextyear_S000300_RF_regressor', 'rb') as f:
        reg_S000300 = pickle.load(f)
        
    with open('Diabetic/Models_NextYear/DiabeticModel_nextyear_L101700_RF_regressor', 'rb') as f:
        reg_L101700 = pickle.load(f)
        
    with open('Diabetic/Models_NextYear/DiabeticModel_nextyear_L100700_RF_regressor', 'rb') as f:
        reg_L100700 = pickle.load(f)
        
    
    # predicte next year value
    N_y_L104600=np.array(reg_L104600.predict(data[cols_L104600]))
    N_y_L103000=list(reg_L103000.predict(data[cols_L103000]))
    N_y_S000300=list(reg_S000300.predict(data[cols_S000300]))
    N_y_L101700=list(reg_L101700.predict(data[cols_L101700]))
    N_y_L100700=list(reg_L100700.predict(data[cols_L100700]))
    N_y_SEX=list(data['SEX'])
    N_y_AGE=list(data['AGE']+1)
    N_y_FIELD_33=list(data['FIELD_33'])
    N_y_FIELD_38=list(data['FIELD_38'])
    N_y_FIELD_40=list(data['FIELD_40'])
    N_y_FIELD_31=list(data['FIELD_31'])
    
    predictedNextYearValues=pd.DataFrame()
    predictedNextYearValues['L104600']=N_y_L104600
    predictedNextYearValues['L103000']=N_y_L103000
    predictedNextYearValues['S000300']=N_y_S000300
    predictedNextYearValues['L101700']=N_y_L101700
    predictedNextYearValues['L100700']=N_y_L100700
    predictedNextYearValues['SEX']=N_y_SEX
    predictedNextYearValues['AGE']=N_y_AGE
    predictedNextYearValues['FIELD_33']=N_y_FIELD_33
    predictedNextYearValues['FIELD_38']=N_y_FIELD_38
    predictedNextYearValues['FIELD_40']=N_y_FIELD_40
    predictedNextYearValues['FIELD_31']=N_y_FIELD_31
    
    predictedNextYearValues=predictedNextYearValues[['L104600','L103000','S000300','L101700','L100700','FIELD_33',
                                                     'FIELD_38','FIELD_40','FIELD_31','SEX','AGE']]
    
    # load the classifer model and the feature scaller  
    with open('Diabetic/Models_NextYear/DiabeticClassifierModelForNextYear_rf_model_SMOTE', 'rb') as f:
        _nextyearData_RF_Clf = pickle.load(f)
        
    with open('Diabetic/Models_NextYear/DiabeticClassifierModelForNextYear_scaler_SMOTE', 'rb') as f:
        _nextyearData_scaler = pickle.load(f)
        
    scaledData= _nextyearData_scaler.transform(predictedNextYearValues)
    
    
    # compute class probability
    classprobapred= pd.DataFrame(_nextyearData_RF_Clf.predict_proba(scaledData), columns=['CLASS 0','CLASS 1','CLASS 2']).to_json(orient='index')
    
    # compute class value
    classpred=pd.DataFrame(_nextyearData_RF_Clf.predict(scaledData),columns=['CLASS']).to_json(orient='index')
    
    RESULT = {
      "Next Year Value": json.loads(predictedNextYearValues.to_json(orient='index')),
      "Class value": json.loads(classpred),
      "Class probability": json.loads(classprobapred) 
    }
        
    
    return RESULT
    


    