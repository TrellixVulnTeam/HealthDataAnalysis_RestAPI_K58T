# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 00:53:41 2019

@author: Henock
"""

# Load the library with the iris dataset
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
np.random.seed(0)


iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()


df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
df.head()

# Create two new dataframes, one with the training rows, one with the test rows
train, test = df[df['is_train']==True], df[df['is_train']==False]

# Show the number of observations for the test and training dataframes
print('Number of observations in the training data:', len(train))
print('Number of observations in the test data:',len(test))

# Create a list of the feature column's names
features = df.columns[:4]
# View features
features


# train['species'] contains the actual species names. Before we can use it,
# we need to convert each species name into a digit. So, in this case there
# are three species, which have been coded as 0, 1, or 2.
y = pd.factorize(train['species'])[0]
# View target
y

ytest = pd.factorize(test['species'])[0]
# View target
ytest




# Create a random forest Classifier. By convention, clf means 'Classifier'
clf = RandomForestClassifier(n_jobs=2, random_state=0)

# Train the Classifier to take the training features and learn how they relate
# to the training y (the species)
clf.fit(train[features], y)


preds_original=clf.predict(test[features])



import pickle

with open('rfmodel', 'wb') as f:
    pickle.dump(clf, f)


# in your prediction file                                                                                                                                                                                                           

with open('rfmodel', 'rb') as f:
    rf = pickle.load(f)


preds_loaded = rf.predict(test[features])



from sklearn import metrics as m

print(m.accuracy_score(ytest,preds_original))
print(m.accuracy_score(ytest,preds_loaded))

pd.DataFrame(y).to_csv('ytrain.txt',sep=',',index=False)
pd.DataFrame(ytest).to_csv('ytest.txt',sep=',',index=False)
pd.DataFrame(train[features]).to_csv('xtrain.txt',sep=',',index=False)
pd.DataFrame(test[features]).to_csv('xtest.txt',sep=',',index=False)



