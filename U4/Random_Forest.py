import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as skm
import pylab as pl

# data is downloadable here:
# https://archive.ics.uci.edu/ml/machine-learning-databases/00240/
# description here:
# https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones
datafolder="../PythonWorking_largedata/UCI HAR Dataset/"

trainx=pd.read_fwf(datafolder+"train/X_train.txt", header=None, widths=[16]*561)
trainy=pd.read_csv(datafolder+"train/Y_train.txt", header=None)

header=pd.read_csv(datafolder+"features.txt", header=None, sep=' ')[1]
trainx.columns=header

rfc = RandomForestClassifier(n_estimators=500, oob_score=True)
print("fitting model...")
model=rfc.fit(trainx, trainy.values.ravel())
# if no .ravel(), warns me this:
# DataConversionWarning: A column-vector y was passed when a 1d array was expected. \
# Please change the shape of y to (n_samples,), for example using ravel().
print("rfc done." + " oob_score_ is " + str(rfc.oob_score_))
############## rfc done. ###############

fi = rfc.feature_importances_
# get top 10 features' index
t10idx=fi.argsort()[-10::]
# get top 10 features' names
t10 = trainx.columns[t10idx]

# test set
testx=pd.read_fwf(datafolder+"test/X_test.txt", header=None, widths=[16]*561)
testy=pd.read_csv(datafolder+"test/y_test.txt", header=None)
testx.columns=header

test_pred=rfc.predict(testx)
print("test data rfc score= %f" % (rfc.score(testx, testy)) )

# what's confusion matrix?
test_cm = skm.confusion_matrix(testy, test_pred)

pl.matshow(test_cm)
pl.title('Confusion matrix for test data')
pl.colorbar()
pl.show()

# Accuracy
print("Accuracy = %f" %(skm.accuracy_score(testy,test_pred)))
# Precision
print("Precision = %f" %(skm.precision_score(testy,test_pred)))
# Recall
print("Recall = %f" %(skm.recall_score(testy,test_pred)))
# F1 Score
print("F1 score = %f" %(skm.f1_score(testy,test_pred)))
