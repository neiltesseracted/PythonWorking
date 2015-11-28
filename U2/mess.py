"""import pandas as pd
import os
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
os.chdir(os.getcwd())

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.split('\n')
data = [i.split(',') for i in data]
header = data[0]
data =data[1::]
df = pd.DataFrame(data, columns=header)
df['Alcohol']=df['Alcohol'].astype(float)
df['Tobacco']=df['Tobacco'].astype(float)
print df.iloc[:,[1]].mean()
stats.mode(df[[1]])
stats.mode(df[[2]])



mean = 0
variance = 1
sigma = np.sqrt(variance)
x = np.linspace(-3,3,100)    # from -3 to 3, with 100 evenly spaced points
plt.plot(x, mlab.normpdf(x,mean,sigma))

plt.show()
"""
"""
import collections
import matplotlib.pyplot as plt
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
#plt.boxplot(x).show()
plt.hist(x, histtype='bar').show()
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show()

plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show()