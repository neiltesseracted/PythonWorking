# import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

from sklearn.cross_validation import KFold

df=pd.read_csv('./U2/loansData_clean.csv')
rate = df['Interest.Rate']
amt = df['Amount.Requested']
fico = df['FICO.Score']
# they're all series type. needs reshape
# y=np.matrix(rate).transpose()
# x1 = np.matrix(fico).transpose()
# x2 = np.matrix(amt).transpose()
#
# x=np.column_stack([x1,x2])
# X=sm.add_constant(x)
# f=smf.ols(formula='rate ~ amt + fico', data=df).fit()
# f.summary()

kf = KFold(rate.__len__(), n_folds=10, shuffle=True)
f=[]
test=pd.DataFrame(columns=['MAE','MSE','R2'])
for i, fold in enumerate(kf):
    dff=df.iloc[fold[0]]
    rate = dff['Interest.Rate']
    amt = dff['Amount.Requested']
    fico = dff['FICO.Score']
    m=smf.ols(formula='rate ~ amt + fico', data=dff).fit()

    # test
    dfv=df.iloc[fold[1]]
    yhat=m.params[0]+m.params[1]*dfv['Amount.Requested'] + m.params[2]*dfv['FICO.Score']
    y=dfv['Interest.Rate']
    mae=abs(y-yhat).mean()
    ssres=((y-yhat)**2).sum()
    mse=((y-yhat)**2).mean()
    ybar=y.mean()
    sstot=((y-ybar)**2).sum()
    r2=1-ssres/sstot

    test.loc[i]=[mae,mse,r2]

print(test)
