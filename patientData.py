import pandas as pd

# read the dataset and convert it to json
data = pd.read_csv('sep19SexAndAgeAddedFINAL DATASET_ver2.txt').drop(
    columns=['Unnamed: 0'])


def getAllPatientData():
    return data.to_json(orient='index')


def getPatientByID(_id):
    return data[data.FIELD_1 == int(_id)].to_json(orient='index')


def getPatientByIDAndDate(_id, _date):
    return data.query('FIELD_1==' + str(_id) + ' and FIELD_2==' + str(_date)
                      ).to_json(orient='index')
