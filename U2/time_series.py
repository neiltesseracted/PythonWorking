import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df=pd.read_csv('../../PythonWorking_largedata/LoanStats3d.csv', skiprows=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index('issue_d_format')
year_month_summary = dfts.groupby(by=lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

plt.plot(loan_count_summary)
sm.graphics.tsa.plot_acf(loan_count_summary)
sm.graphics.tsa.plot_pacf(loan_count_summary)

