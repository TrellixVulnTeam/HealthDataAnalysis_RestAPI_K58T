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


@app.route('/success/<name>')
def success(name):
   return 'welcome ' + name


if __name__ == '__main__':
   app.run(debug=True)
   
   
   
   