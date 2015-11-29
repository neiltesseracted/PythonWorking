import pandas as pd
import os
import statsmodels.api as sm
import math
import matplotlib.pyplot as plt
os.chdir(os.getcwd())

df=pd.read_csv('loansData_clean.csv')
df['IR_TF']=df['Interest.Rate'].map(lambda x: x < .12)
df['ones']=1
"""ind_vars=df.columns.tolist()
ind_vars.remove('IR_TF')
"""
ind_vars=['ones', 'FICO.Score', 'Amount.Requested']
logit=sm.Logit(df['IR_TF'], df[ind_vars])
result = logit.fit()
coeff = result.params
#print(coeff)

def logistic(FicoScore, LoanAmount):
    expbx=math.exp(coeff[0] + coeff[1]*FicoScore + coeff[2]*LoanAmount)
    return expbx/(1+expbx)
    #return 1/(1+expbx)

print logistic(720, 10000)

ficos=list(range(550, 850))
p=map(lambda x: logistic(x, 1000), ficos)
plt.plot(ficos,p)
plt.ylabel('Chance')
plt.xlabel('FICO')