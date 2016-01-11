import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from scipy.cluster.vq import kmeans, vq, whiten

df=pd.read_csv('./U4/un.csv')

# only need 4 col
df=df[['lifeMale','lifeFemale','infantMortality','GDPperCapita']]
# get rid of NaNs
df=df[df['lifeMale'].notnull()][df['lifeFemale'].notnull()][df['infantMortality'].notnull()][df['GDPperCapita'].notnull()]

whitened=whiten(df)
distavg=[]
for k in range(1,11):
    centroids, _ =kmeans(whitened[:,3],k)
    _, idxdist = vq(whitened[:,3],centroids)
    distavg.append(idxdist.mean())
# plot average distortions with different k
plt.plot(distavg, '-ob', markersize=3)

# k = 3
plt.figure()
centroids, dist =kmeans(whitened[:,[2,3]],3)
idx, idxdist = vq(whitened[:,[2,3]],centroids)
plt.plot(df.iloc[idx==0, 3], df.iloc[idx==0, 2], 'ob',
            df.iloc[idx==1, 3], df.iloc[idx==1, 2], 'or',
            df.iloc[idx==2, 3], df.iloc[idx==2, 2], 'og')
plt.xlabel(df.columns[3])
plt.ylabel(df.columns[2])
plt.savefig('kmeans_mortality_v_gdp_2dcentroids')

# GDPperCapita as base for kmeans
plt.figure()
centroids, dist =kmeans(whitened[:,3],3)
idx, idxdist = vq(whitened[:,3],centroids)
plt.plot(df.iloc[idx==0, 3], df.iloc[idx==0, 2], 'ob',
            df.iloc[idx==1, 3], df.iloc[idx==1, 2], 'or',
            df.iloc[idx==2, 3], df.iloc[idx==2, 2], 'og')
plt.xlabel(df.columns[3])
plt.ylabel(df.columns[2])
plt.savefig('kmeans_mortality_v_gdp_1dcentroids')


