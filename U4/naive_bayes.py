import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

df=pd.read_csv('./U4/ideal_weight.csv', index_col=0)
df.index.name=df.index.name.strip('\'')
for c in df.columns:
    df.rename(columns=lambda c: c.strip('\''), inplace=True)
df['sex']=df['sex'].map(lambda x: x.strip('\''))

df[['actual','ideal']].plot(kind='hist', alpha=.6, bins=27, color=['g','b'])
plt.figure()
df['diff'].plot(kind='hist',bins=25,color='r')

df['gender'] = pd.Categorical(df['sex'].tolist())
df.gender.value_counts()

# Naive Bayes
gnb=GaussianNB()
X=df.iloc[:, 1:4]
y=df['gender']
print "fitting model..."
model=gnb.fit(X, y)
print "model done."

yhat=gnb.predict(X)
print("Total obs = " + str(len(X)) + ". Mislabeled = " + str( (yhat!=y).sum() ) + ".")

# new points
p1=(145, 160, -15)
p2=(160, 145, 15)
print("p1 = " + str(p1) + ", predicted as: " + str(gnb.predict(p1)) +\
    "\np2 = " + str(p2) + ", predicted as: " + str(gnb.predict(p2)) )

