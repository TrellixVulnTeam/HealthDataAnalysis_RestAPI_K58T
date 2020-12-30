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

def getDiabetesTestData():
    return diabetesTestData


def getHyperlipidemiaTestData():
    return hyperlipidemiaTestData


def getIschemiaTestData():
    return ischemiaTestData 


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

