import pandas as pd
import numpy as np
import json

# read the dataset and convert it to json
data = pd.read_csv('sep19SexAndAgeAddedFINAL DATASET_ver2.txt').drop(
    columns=['Unnamed: 0'])


# prepare the data for diabetes ui test
diabetesTestData = ""
hyperlipidemiaTestData=""


def prepareDiabetesTestData():

    tempdata = data

    conditions = [(tempdata.L100800 < 100), (tempdata.L100800 >= 100) & (
        tempdata.L100800 < 126),        (tempdata.L100800 >= 126)]

    choices = [0, 1, 2]

    tempdata['CLASS'] = np.select(conditions, choices, default=0)

    # filter the data set
    # exclude people who are diagnosed for (diabetes)
    tempdata = tempdata[tempdata.FIELD_16 != 1]
    # exclude people who are on medication for diabetes
    tempdata = tempdata[tempdata.FIELD_23 != 1]

    # exclude people who are diagnosed for (high blood pressure)
    tempdata = tempdata[tempdata.FIELD_15 != 1]
    # exclude people who are on medication for high blood pressure
    tempdata = tempdata[tempdata.FIELD_22 != 1]

    # exclude people who are diagnosed for hyperlipidemia
    tempdata = tempdata[tempdata.FIELD_17 != 1]
    # exclude people who are on medication for hyperlipidemia
    tempdata = tempdata[tempdata.FIELD_24 != 1]
    print(tempdata.shape)

    diabetes_requiredColumns = ['AGE', 'FIELD_31', 'FIELD_33', 'FIELD_38', 'FIELD_40',
                                'L100500', 'L100700', 'L100800', 'L101200', 'L101300',
                                'L101600', 'L101700', 'L103000', 'L103100', 'L103300',
                                'L104600', 'L107400', 'L190000', 'L190300', 'L190400',
                                'S000100', 'S000300', 'S000501', 'S000502', 'SEX', 'CLASS']

    tempdata = tempdata[diabetes_requiredColumns]
    tempdata = tempdata.dropna()

    randomstate = 5
    sizeofdatapoints = 10

    diabetesTestData = pd.concat([tempdata[tempdata.CLASS == 0].sample(sizeofdatapoints, random_state=randomstate),
                                  tempdata[tempdata.CLASS == 1].sample(
                                      sizeofdatapoints, random_state=randomstate),
                                  tempdata[tempdata.CLASS == 2].sample(sizeofdatapoints, random_state=randomstate)], ignore_index=True).transpose().to_json()
    return diabetesTestData


def prepareHyperlipidemiaTestData():

    tempdata = data

    _class = []
    for i in range(data.shape[0]):
        if((tempdata.L102900[i] <= 200) & (tempdata.L103200[i] <= 130) & (tempdata.L103000[i] <= 150)):
            _class.append(0)
        else:
            _class.append(1)
    tempdata["CLASS"] = _class

    # filter the data set
    # exclude people who are diagnosed for (diabetes)
    tempdata = tempdata[tempdata.FIELD_16 != 1]
    # exclude people who are on medication for diabetes
    tempdata = tempdata[tempdata.FIELD_23 != 1]

    # exclude people who are diagnosed for (high blood pressure)
    tempdata = tempdata[tempdata.FIELD_15 != 1]
    # exclude people who are on medication for high blood pressure
    tempdata = tempdata[tempdata.FIELD_22 != 1]

    # exclude people who are diagnosed for hyperlipidemia
    tempdata = tempdata[tempdata.FIELD_17 != 1]
    # exclude people who are on medication for hyperlipidemia
    tempdata = tempdata[tempdata.FIELD_24 != 1]
    print(tempdata.shape)

    diabetes_requiredColumns = ['AGE', 'FIELD_38', 'L100500', 'L100700', 'L100800', 'L101200', 'L101300',
                                'L101700', 'L102900', 'L103000', 'L103100', 'L103200', 'L103300',
                                'L104500', 'L104600', 'L190300', 'L190400',
                                'L190500', 'L190800', 'S000100', 'S000300', 'S000501', 'S000502', 'SEX', 'CLASS']

    tempdata = tempdata[diabetes_requiredColumns]
    tempdata = tempdata.dropna()

    randomstate = 45
    sizeofdatapoints = 15

    hyperlipidemiaTestData = pd.concat([tempdata[tempdata.CLASS == 0].sample(sizeofdatapoints, random_state=randomstate),
                                  tempdata[tempdata.CLASS == 1].sample(
                                      sizeofdatapoints, random_state=randomstate)
                                  ], ignore_index=True).transpose().to_json()
    return hyperlipidemiaTestData


diabetesTestData = prepareDiabetesTestData()
hyperlipidemiaTestData=prepareHyperlipidemiaTestData()


def getDiabetesTestData():
    return diabetesTestData

def getHyperlipidemiaTestData():
    return hyperlipidemiaTestData


def getAllPatientData():
    return data.to_json(orient='index')


def getPatientByID(_id):
    return data[data.FIELD_1 == int(_id)].to_json(orient='index')


def getPatientByIDAndDate(_id, _date):
    return data.query('FIELD_1==' + str(_id) + ' and FIELD_2==' + str(_date)
                      ).to_json(orient='index')


def prepareTempData():
    tempdata = data.copy()

    # filter the tempdata set

    # exclude people who are diagnosed for (diabetes)
    tempdata = tempdata[tempdata.FIELD_16 != 1]

    # exclude people who are on medication for diabetes
    tempdata = tempdata[tempdata.FIELD_23 != 1]
    tempdata = tempdata[
        tempdata.FIELD_15 != 1
    ]  # exclude people who are diagnosed for (high blood pressure)
    tempdata = tempdata[
        tempdata.FIELD_22 != 1
    ]  # exclude people who are on medication for high blood pressure

    # exclude people who are diagnosed for hyperlipidemia
    tempdata = tempdata[tempdata.FIELD_17 != 1]
    tempdata = tempdata[
        tempdata.FIELD_24 != 1
    ]  # exclude people who are on medication for hyperlipidemia

    tempdata = tempdata[
        [
            "L100800",
            "L104600",
            "L103000",
            "S000300",
            "L101700",
            "L100700",
            "FIELD_33",
            "FIELD_38",
            "FIELD_40",
            "FIELD_31",
            "SEX",
            "AGE"
        ]
    ]
    tempdata = tempdata.dropna()

    return tempdata


tempdata = prepareTempData()


def gethistplotData():

    age_counts, age_bin_edges = np.histogram(
        tempdata[tempdata.AGE >= 18].AGE, bins=10)
    fpg_counts, fpg_bin_edges = np.histogram(
        tempdata[tempdata.L100800 <= 300].L100800, bins=10)
    hbalc_counts, hbalc_bin_edges = np.histogram(
        tempdata[tempdata.L104600 <= 20].L104600, bins=10)
    bmi_counts, bmi_bin_edges = np.histogram(
        tempdata[tempdata.S000300 <= 50].S000300, bins=10)

    RESULT = {
        "age_counts": json.loads(str(list(age_counts))),
        "age_bin_edges": json.loads(str(list(age_bin_edges))),

        "fpg_counts": json.loads(str(list(fpg_counts))),
        "fpg_bin_edges": json.loads(str(list(fpg_bin_edges))),

        "hbalc_counts": json.loads(str(list(hbalc_counts))),
        "hbalc_bin_edges": json.loads(str(list(hbalc_bin_edges))),

        "bmi_counts": json.loads(str(list(bmi_counts))),
        "bmi_bin_edges": json.loads(str(list(bmi_bin_edges))),


    }

    return RESULT


# def getDiabetesTestData():

#     return 0

    # conditions = [(data.L100800 < 100),(data.L100800 >= 100) & (
    #     data.L100800 < 126),        (data.L100800 >= 126)]

    # choices = [0, 1, 2]

    # data['CLASS'] = np.select(conditions, choices, default=0)

    # # filter the data set
    # # exclude people who are diagnosed for (diabetes)
    # data = data[data.FIELD_16 != 1]
    # # exclude people who are on medication for diabetes
    # data = data[data.FIELD_23 != 1]

    # # exclude people who are diagnosed for (high blood pressure)
    # data = data[data.FIELD_15 != 1]
    # # exclude people who are on medication for high blood pressure
    # data = data[data.FIELD_22 != 1]

    # # exclude people who are diagnosed for hyperlipidemia
    # data = data[data.FIELD_17 != 1]
    # # exclude people who are on medication for hyperlipidemia
    # data = data[data.FIELD_24 != 1]
    # print(data.shape)

    # diabetes_requiredColumns = ['AGE', 'FIELD_31', 'FIELD_33', 'FIELD_38', 'FIELD_40',
    #                             'L100500', 'L100700', 'L100800', 'L101200', 'L101300',
    #                             'L101600', 'L101700', 'L103000', 'L103100', 'L103300',
    #                             'L104600', 'L107400', 'L190000', 'L190300', 'L190400',
    #                             'S000100', 'S000300', 'S000501', 'S000502', 'SEX', 'CLASS']

    # data = data[diabetes_requiredColumns]
    # data=data.dropna()

    # return pd.concat([data[data.CLASS == 0].sample(5, random_state=42),
    #                   data[data.CLASS == 1].sample(5, random_state=42),
    #                   data[data.CLASS == 2].sample(5, random_state=42)], ignore_index=True).transpose().to_json()
