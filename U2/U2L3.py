import pandas as pd
import matplotlib.pyplot as plt
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData['Interest.Rate']=loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%'))/100, 4))
loansData['Loan.Length']=loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['Debt.To.Income.Ratio']=loansData['Debt.To.Income.Ratio'].map(lambda x: round(float(x.rstrip('%'))/100, 4))
loansData['FICO.Range']=loansData['FICO.Range'].map(lambda x: [int(i) for i in x.split('-')])

loansData['FICO.Score']=loansData['FICO.Range'].map(lambda x: sum(x)/len(x))

"""
plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()
"""
loansData.hist(column='FICO.Score')
plt.show()

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10),diagonal='hist')
