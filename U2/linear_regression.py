import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData['Interest.Rate']=loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%'))/100, 4))
loansData['Loan.Length']=loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['Debt.To.Income.Ratio']=loansData['Debt.To.Income.Ratio'].map(lambda x: round(float(x.rstrip('%'))/100, 4))
loansData['FICO.Range']=loansData['FICO.Range'].map(lambda x: [int(i) for i in x.split('-')])

loansData['FICO.Score']=loansData['FICO.Range'].map(lambda x: sum(x)/len(x))
loansData.to_csv('loansData_clean.csv', header=True, index=False)

rate = loansData['Interest.Rate']
amt = loansData['Amount.Requested']
fico = loansData['FICO.Score']
# they're all series type. needs reshape
y=np.matrix(rate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(amt).transpose()

x=np.column_stack([x1,x2])
X=sm.add_constant(x)
model=sm.OLS(y, X)

f=model.fit()
f.summary()
