import pandas as pd
import numpy as np
import json

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
