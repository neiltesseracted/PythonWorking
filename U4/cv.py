from sklearn import cross_validation as cv
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics as skm

iris = datasets.load_iris()
# df=pd.DataFrame(data=iris.data, columns=iris.feature_names)
# df['target']=iris.target
# df['target_names']=df['target'].map(lambda x: iris.target_names[x])
# df=df.reindex_axis(df.columns[[0,1,2,3,5,4]],axis=1)

# split to train and test sets
# train, test = cross_validation.train_test_split(df, test_size=.4)

# I want petal lenth & petal width vs target
# data=df.ix[:,[2,3,4]]

# from sklearn.cross_validation import KFold
# kf = KFold(data.__len__(), n_folds=5, shuffle=True)

from sklearn import svm
svc = svm.SVC(kernel='linear')
X=iris.data[:,[2,3]]
y=iris.target

# w/o train-test split
svc.fit(X, y)
y_pred = svc.predict(X)
print "W/O train-test split, svm accuracy is:", skm.accuracy_score(y, y_pred)

# Cross-Validation
print "W/ Cross-validation (5folds), svm accuracy is: \n", cv.cross_val_score(svc, X, y, cv=5)
