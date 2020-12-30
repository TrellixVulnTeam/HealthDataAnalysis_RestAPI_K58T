import pandas as pd
import numpy as np
import json

# read the dataset and convert it to json
# data = pd.read_csv('sep19SexAndAgeAddedFINAL DATASET_ver2.txt').drop(
#     columns=['Unnamed: 0'])
# data = ischemiadata = pd.read_csv('DATASET_2019-10-24_light.txt')

# prepare the data for diabetes ui test
diabetesTestData = ""
hyperlipidemiaTestData = ""
ischemiaTestData = ""


# def prepareDiabetesTestData():

#     tempdata = data

#     conditions = [(tempdata.L100800 < 100), (tempdata.L100800 >= 100) & (
#         tempdata.L100800 < 126),        (tempdata.L100800 >= 126)]

#     choices = [0, 1, 2]

#     tempdata['CLASS'] = np.select(conditions, choices, default=0)

#     # filter the data set
#     # exclude people who are diagnosed for (diabetes)
#     tempdata = tempdata[tempdata.FIELD_16 != 1]
#     # exclude people who are on medication for diabetes
#     tempdata = tempdata[tempdata.FIELD_23 != 1]

#     # exclude people who are diagnosed for (high blood pressure)
#     tempdata = tempdata[tempdata.FIELD_15 != 1]
#     # exclude people who are on medication for high blood pressure
#     tempdata = tempdata[tempdata.FIELD_22 != 1]

#     # exclude people who are diagnosed for hyperlipidemia
#     tempdata = tempdata[tempdata.FIELD_17 != 1]
#     # exclude people who are on medication for hyperlipidemia
#     tempdata = tempdata[tempdata.FIELD_24 != 1]
#     print(tempdata.shape)

#     diabetes_requiredColumns = ['AGE', 'FIELD_31', 'FIELD_33', 'FIELD_38', 'FIELD_40',
#                                 'L100500', 'L100700', 'L100800', 'L101200', 'L101300',
#                                 'L101600', 'L101700', 'L103000', 'L103100', 'L103300',
#                                 'L104600', 'L107400', 'L190000', 'L190300', 'L190400',
#                                 'S000100', 'S000300', 'S000501', 'S000502', 'SEX', 'CLASS']

#     tempdata = tempdata[diabetes_requiredColumns]
#     tempdata = tempdata.dropna()

#     randomstate = 15
#     sizeofdatapoints = 10

#     diabetesTestData = pd.concat([tempdata[tempdata.CLASS == 0].sample(sizeofdatapoints, random_state=randomstate),
#                                   tempdata[tempdata.CLASS == 1].sample(
#                                       sizeofdatapoints, random_state=randomstate),
#                                   tempdata[tempdata.CLASS == 2].sample(sizeofdatapoints, random_state=randomstate)], ignore_index=True).transpose().to_json()
#     return diabetesTestData


# def prepareHyperlipidemiaTestData():

#     tempdata = data

#     _class = []
#     for i in range(data.shape[0]):
#         if((tempdata.L102900[i] <= 200) & (tempdata.L103200[i] <= 130) & (tempdata.L103000[i] <= 150)):
#             _class.append(0)
#         else:
#             _class.append(1)
#     tempdata["CLASS"] = _class

#     # filter the data set
#     # exclude people who are diagnosed for (diabetes)
#     tempdata = tempdata[tempdata.FIELD_16 != 1]
#     # exclude people who are on medication for diabetes
#     tempdata = tempdata[tempdata.FIELD_23 != 1]

#     # exclude people who are diagnosed for (high blood pressure)
#     tempdata = tempdata[tempdata.FIELD_15 != 1]
#     # exclude people who are on medication for high blood pressure
#     tempdata = tempdata[tempdata.FIELD_22 != 1]

#     # exclude people who are diagnosed for hyperlipidemia
#     tempdata = tempdata[tempdata.FIELD_17 != 1]
#     # exclude people who are on medication for hyperlipidemia
#     tempdata = tempdata[tempdata.FIELD_24 != 1]
#     print(tempdata.shape)

#     diabetes_requiredColumns = ['AGE', 'FIELD_38', 'L100500', 'L100700', 'L100800', 'L101200', 'L101300',
#                                 'L101700', 'L102900', 'L103000', 'L103100', 'L103200', 'L103300',
#                                 'L104500', 'L104600', 'L190300', 'L190400',
#                                 'L190500', 'L190800', 'S000100', 'S000300', 'S000501', 'S000502', 'SEX', 'CLASS']

#     tempdata = tempdata[diabetes_requiredColumns]
#     tempdata = tempdata.dropna()

#     randomstate = 15
#     sizeofdatapoints = 15

#     hyperlipidemiaTestData = pd.concat([tempdata[tempdata.CLASS == 0].sample(sizeofdatapoints, random_state=randomstate),
#                                         tempdata[tempdata.CLASS == 1].sample(
#         sizeofdatapoints, random_state=randomstate)
#     ], ignore_index=True).transpose().to_json()
#     return hyperlipidemiaTestData


# def prepareIschemiaTestData():

#     tempdata = ischemiadata

#     diabetes_requiredColumns = ['AGE', 'FIELD_15', 'FIELD_33', 'FIELD_38', 'FIELD_4', 'L100200',
#                                 'L100500', 'L100700', 'L100800', 'L101200', 'L101300', 'L101600',
#                                 'L101700', 'L102900', 'L103000', 'L103100', 'L103200', 'L103300',
#                                 'L104300', 'L104400', 'L104500', 'L190000', 'L190300', 'L190400',
#                                 'L190500', 'L190600', 'L190700', 'L190800', 'L190900', 'L504700',
#                                 'S000100', 'S000300', 'S000501', 'S000502', 'SEX', 'CLASS']

#     tempdata = tempdata[diabetes_requiredColumns]
#     tempdata = tempdata.dropna()

#     randomstate = 45
#     sizeofdatapoints = 15

#     return pd.concat([tempdata[tempdata.CLASS == 0].sample(sizeofdatapoints, random_state=randomstate),
#                       tempdata[tempdata.CLASS == 1].sample(
#         sizeofdatapoints, random_state=randomstate)
#     ], ignore_index=True).transpose().to_json()


# diabetesTestData = prepareDiabetesTestData()
# hyperlipidemiaTestData = prepareHyperlipidemiaTestData()
# ischemiaTestData = prepareIschemiaTestData()


def getDiabetesTestData():
    return diabetesTestData


def getHyperlipidemiaTestData():
    return hyperlipidemiaTestData


def getIschemiaTestData():
    return ischemiaTestData


# def getAllPatientData():
#     return data.to_json(orient='index')


# def getPatientByID(_id):
#     return data[data.FIELD_1 == int(_id)].to_json(orient='index')


# def getPatientByIDAndDate(_id, _date):
#     return data.query('FIELD_1==' + str(_id) + ' and FIELD_2==' + str(_date)
#                       ).to_json(orient='index')


# def prepareTempData():
#     tempdata = data.copy()

#     # filter the tempdata set

#     # exclude people who are diagnosed for (diabetes)
#     tempdata = tempdata[tempdata.FIELD_16 != 1]

#     # exclude people who are on medication for diabetes
#     tempdata = tempdata[tempdata.FIELD_23 != 1]
#     tempdata = tempdata[
#         tempdata.FIELD_15 != 1
#     ]  # exclude people who are diagnosed for (high blood pressure)
#     tempdata = tempdata[
#         tempdata.FIELD_22 != 1
#     ]  # exclude people who are on medication for high blood pressure

#     # exclude people who are diagnosed for hyperlipidemia
#     tempdata = tempdata[tempdata.FIELD_17 != 1]
#     tempdata = tempdata[
#         tempdata.FIELD_24 != 1
#     ]  # exclude people who are on medication for hyperlipidemia

#     tempdata = tempdata[
#         [
#             "L100800",
#             "L104600",
#             "L103000",
#             "S000300",
#             "L101700",
#             "L100700",
#             "FIELD_33",
#             "FIELD_38",
#             "FIELD_40",
#             "FIELD_31",
#             "SEX",
#             "AGE"
#         ]
#     ]
#     tempdata = tempdata.dropna()

#     return tempdata


# tempdata = prepareTempData()


def gethistplotData():
    """
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
    """
    RESULT = {
        "age_bin_edges": [
            18.0,
            26.9,
            35.8,
            44.7,
            53.6,
            62.5,
            71.4,
            80.30000000000001,
            89.2,
            98.10000000000001,
            107.0
        ],
        "age_counts": [
            3379,
            31713,
            49972,
            40572,
            13998,
            2601,
            453,
            24,
            0,
            5
        ],
        "bmi_bin_edges": [
            2.6,
            7.07,
            11.54,
            16.01,
            20.48,
            24.95,
            29.42,
            33.89,
            38.36,
            42.83,
            47.3
        ],
        "bmi_counts": [
            1,
            0,
            316,
            27375,
            75110,
            34708,
            4558,
            565,
            74,
            15
        ],
        "fpg_bin_edges": [
            0.0,
            30.0,
            60.0,
            90.0,
            120.0,
            150.0,
            180.0,
            210.0,
            240.0,
            270.0,
            300.0
        ],
        "fpg_counts": [
            1,
            13,
            44610,
            94180,
            3105,
            408,
            164,
            114,
            62,
            39
        ],
        "hbalc_bin_edges": [
            0.0,
            1.53,
            3.06,
            4.59,
            6.12,
            7.65,
            9.18,
            10.71,
            12.24,
            13.77,
            15.3
        ],
        "hbalc_counts": [
            1,
            0,
            353,
            137251,
            4378,
            399,
            205,
            98,
            34,
            5
        ]
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
