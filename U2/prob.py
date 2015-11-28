import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.figure()
plt.boxplot(x)
plt.savefig('testboxplot')

plt.figure()
plt.hist(x,histtype="bar")
plt.savefig("testhistplot")

plt.figure()
stats.probplot(x,dist="norm",plot=plt)
plt.savefig("testqqplot")