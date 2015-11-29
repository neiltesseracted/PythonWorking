import pandas as pd
import os
import statsmodels.formula.api as smf
import numpy as np
import matplotlib.pyplot as plt
os.chdir(os.getcwd())

# download csv here
# https://www.lendingclub.com/info/download-data.action
# DOWNLOAD LOAN DATA: 2015 - 09/30/15
df=pd.read_csv('LoanStats3d.csv', skiprows=1)

# get rid of NaN in annual_inc and int_rate and home_ownership
df=df[df['annual_inc'].notnull()]
df=df[df['int_rate'].notnull()]
df=df[df['home_ownership'].notnull()]

df=pd.DataFrame(df, columns=['int_rate', 'annual_inc', 'home_ownership'])
df.int_rate = df['int_rate'].map(lambda x: round(float(x.rstrip('%'))/100, 4))
df['ho'] = pd.Categorical(df.home_ownership).codes

est1 = smf.ols(formula="int_rate ~ annual_inc", data=df).fit()
est2 = smf.ols(formula="int_rate ~ annual_inc + ho", data=df).fit()
est3 = smf.ols(formula="int_rate ~ annual_inc * ho", data=df).fit()
est1.summary()
est2.summary()
est3.summary()
