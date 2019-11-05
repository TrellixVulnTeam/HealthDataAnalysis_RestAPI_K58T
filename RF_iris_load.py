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




#{"0":{"sepal length (cm)":5.0,"sepal width (cm)":3.4,"petal length (cm)":1.5,"petal width (cm)":0.2},"1":{"sepal length (cm)":4.4,"sepal width (cm)":2.9,"petal length (cm)":1.4,"petal width (cm)":0.2},"2":{"sepal length (cm)":5.4,"sepal width (cm)":3.7,"petal length (cm)":1.5,"petal width (cm)":0.2},"3":{"sepal length (cm)":4.3,"sepal width (cm)":3.0,"petal length (cm)":1.1,"petal width (cm)":0.1},"4":{"sepal length (cm)":5.1,"sepal width (cm)":3.5,"petal length (cm)":1.4,"petal width (cm)":0.3}}