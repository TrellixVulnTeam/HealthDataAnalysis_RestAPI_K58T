from flask import Flask, redirect, url_for, request
import numpy as np
import patientData 
#import RF_iris_load

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'


@app.route('/hello')
def hello_world2():
   return 'Hello World'


@app.route('/getAllPatientData', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def getAllPatientData():
    return patientData.getAllPatientData()


@app.route('/getPatientByID/<_patientID>', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def getPatientByID(_patientID):
    return patientData.getPatientByID(_patientID)


@app.route('/getPatientByIDAndDate/<_patientID>/<_date>', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def getPatientByIDAndDate(_patientID,_date):
    return patientData.getPatientByIDAndDate(_patientID,_date)

#
#@app.route('/returnAccuracy', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
#def returnAccuracy():
#    return RF_iris_load.returnAccuracy()
#
#
#@app.route('/predictRf', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
#def predictRf():
#    content = request.get_json()
#    if(content == None):
#        return 'No dataset available'
#    else:
#        import pandas as pd 
#        df = pd.DataFrame.from_dict(content, orient='index')    
#        return RF_iris_load.predictRf(np.asarray(df))
#
##    return RF_iris_load.predictRf([[5. , 3.4, 1.5, 0.2],[5. , 3.4, 1.5, 0.2],[5. , 3.4, 1.5, 0.2]])


@app.route('/success/<name>')
def success(name):
   return 'welcome ' + name


if __name__ == '__main__':
   app.run(debug=True)
   
   
   
   