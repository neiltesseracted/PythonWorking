# Data is downloadable here
# https://archive.ics.uci.edu/ml/datasets/Iris
import requests
import io
import pandas as pd
import matplotlib.pyplot as plt
import random

r=requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
df=pd.read_csv(io.BytesIO(r.content), header=None)
"""
7. Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class:
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica
"""
header=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df.columns=header

# only need sepal
df.drop(df.columns[[2,3]],axis=1, inplace=True)

# scatter plot the data
classes=df['class'].value_counts().index
cc=iter(['y', 'g', 'm'])
fig, ax=plt.subplots()
for c in classes:
    df[df['class']==c].plot(kind='scatter', x='sepal_length', y='sepal_width', c=cc.next(), ax=ax)

# generate a random point within the range
p_l=round((df.sepal_length.max()-df.sepal_length.min())*random.random() + df.sepal_length.min() , 2)
p_w=round((df.sepal_width.max()-df.sepal_width.min())*random.random() + df.sepal_width.min() , 2)
point=(p_l, p_w)

# knn()
def knn(point, df, k):
    df2=df
    df2['x_dist']=df[[0]]-point[0]
    df2['y_dist']=df[[1]]-point[1]
    df2['dist']=(df2['x_dist']**2+df2['y_dist']**2)**.5
    tally=df['class'][df2['dist'].argsort()[0:k]].value_counts()
    return tally.argmax()

ax.plot([point[0]], [point[1]], 'Dr', ms=9, alpha=.6)
print("New random point is plotted as a red diamond. \n"
      "kNN with k=10 thinks it's " + str(knn(point, df, 10)) + ".")
