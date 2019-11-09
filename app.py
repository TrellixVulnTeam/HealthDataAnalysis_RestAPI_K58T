


from flask import Flask, redirect, url_for, request
import numpy as np
import patientData  
from Diabetic import diabeticPrediction as dp 
from Hyperlipidemia import HyperlipidemiaPrediction as hp 
from Ischemia import Ischemia as ip 

app = Flask(__name__)

# ==== test route
@app.route('/')
def hello_world():
   return 'Hello World'


@app.route('/hello')
def hello_world2():
   return 'Hello World'


@app.route('/success/<name>')
def success(name):
   return 'welcome ' + name

#======== patient info API ============
#   ================================
   
@app.route('/getAllPatientData', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def getAllPatientData():
    return patientData.getAllPatientData()


@app.route('/getPatientByID/<_patientID>', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def getPatientByID(_patientID):
    return patientData.getPatientByID(_patientID)


@app.route('/getPatientByIDAndDate/<_patientID>/<_date>', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def getPatientByIDAndDate(_patientID,_date):
    return patientData.getPatientByIDAndDate(_patientID,_date)


#======== DIABETIC info API============
#   ================================

@app.route('/predictDiabetic', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def predictDiabetic():
    content = request.get_json()
    if(content == None):
        return 'No dataset available'
    else:
        import pandas as pd 
        df = pd.DataFrame.from_dict(content, orient='index')   
        return dp.predictDiabeticClass(df) #RF_iris_load.predictRf(np.asarray(df))
    
@app.route('/predictDiabeticNextYearValue', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def predictDiabeticNextYearValue():
    content = request.get_json()
    if(content == None):
        return 'No dataset available'
    else:
        import pandas as pd 
        df = pd.DataFrame.from_dict(content, orient='index')   
        return dp.predictDiabeticNextYearValue(df) #RF_iris_load.predictRf(np.asarray(df))
    
      
@app.route('/predictNextYearDiabeticClass', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def predictNextYearDiabeticClass():
    content = request.get_json()
    if(content == None):
        return 'No dataset available'
    else:
        import pandas as pd 
        df = pd.DataFrame.from_dict(content, orient='index')   
        return dp.predictNextYearDiabeticClass(df) #RF_iris_load.predictRf(np.asarray(df))
    
    

#======== Hyperlipidemia info API============
#   ================================
    
@app.route('/predictHyperlipidemiaClass', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def predictHyperlipidemiaClass():
    content = request.get_json()
    if(content == None):
        return 'No dataset available'
    else:
        import pandas as pd 
        df = pd.DataFrame.from_dict(content, orient='index')   
        return hp.predictHyperlipidemiaClass(df) #RF_iris_load.predictRf(np.asarray(df))
    
@app.route('/predictHyperlipidemiaNextYearValue', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def predictHyperlipidemiaNextYearValue():
    content = request.get_json()
    if(content == None):
        return 'No dataset available'
    else:
        import pandas as pd 
        df = pd.DataFrame.from_dict(content, orient='index')   
        return hp.predictHyperlipidemiaNextYearValue(df) #RF_iris_load.predictRf(np.asarray(df))
      
@app.route('/predictNextYearHyperlipidemiaClass', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def predictNextYearHyperlipidemiaClass():
    content = request.get_json()
    if(content == None):
        return 'No dataset available'
    else:
        import pandas as pd 
        df = pd.DataFrame.from_dict(content, orient='index')   
        return hp.predictNextYearHyperlipidemiaClass(df) #RF_iris_load.predictRf(np.asarray(df))
    
    

#======== Ischemia info API============
#   ================================
    

@app.route('/predictIschemiaClass', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def predictIschemiaClass():
    content = request.get_json()
    if(content == None):
        return 'No dataset available'
    else:
        import pandas as pd 
        df = pd.DataFrame.from_dict(content, orient='index')   
        return ip.predictIschemiaClass(df) #RF_iris_load.predictRf(np.asarray(df))
    
    
@app.route('/predictIschemiaNextYearValue', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def predictIschemiaNextYearValue():
    content = request.get_json()
    if(content == None):
        return 'No dataset available'
    else:
        import pandas as pd 
        df = pd.DataFrame.from_dict(content, orient='index')   
        return ip.predictIschemiaNextYearValue(df) #RF_iris_load.predictRf(np.asarray(df))
        
@app.route('/predictIschemiaNextYearClass', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def predictIschemiaNextYearClass():
    content = request.get_json()
    if(content == None):
        return 'No dataset available'
    else:
        import pandas as pd 
        df = pd.DataFrame.from_dict(content, orient='index')   
        return ip.predictIschemiaNextYearClass(df) #RF_iris_load.predictRf(np.asarray(df))
      
#=============app start=====================
if __name__ == '__main__':
   app.run(debug=True)
   
   
   
   
   
   