# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 01:43:30 2019

@author: Henock
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import pickle
from sklearn import metrics as m
np.random.seed(0)

xtest=pd.read_csv('xtest.txt')
ytest=pd.read_csv('ytest.txt')



with open('rfmodel', 'rb') as f:
    rf = pickle.load(f)


preds_loaded = rf.predict(xtest)
print(m.accuracy_score(ytest,preds_loaded))


def returnAccuracy():
    return str(m.accuracy_score(ytest,preds_loaded))

def predictRf(data):
    return str(list(rf.predict(data)))
