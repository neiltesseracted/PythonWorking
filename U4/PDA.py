import numpy as np
from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()
df=pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target']=iris.target
df['target_names']=df['target'].map(lambda x: iris.target_names[x])
df=df.reindex_axis(df.columns[[0,1,2,3,5,4]],axis=1)

# split data table into data X and class labels y
X = df.ix[:,0:4].values
y = df.ix[:,4].values

# Standardizing
from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X)

# Cov on mean
mean_vec = np.mean(X_std, axis=0)
cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)
print('Covariance matrix \n%s' %cov_mat)
# or
# print('NumPy covariance matrix: \n%s' %np.cov(X_std.T))

# eigendecomposition on the covariance
cov_mat = np.cov(X_std.T)

eig_vals, eig_vecs = np.linalg.eig(cov_mat)

print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)

# or
# u,s,v = np.linalg.svd(X_std.T)
# u

# corr
# cor_mat1 = np.corrcoef(X.T)
# cor_mat1

# Sorting Eigenpairs
for ev in eig_vecs:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
print('Everything ok!')

# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort()
eig_pairs.reverse()

# Visually confirm that the list is correctly sorted by decreasing eigenvalues
print('Eigenvalues in descending order:')
for i in eig_pairs:
    print(i[0])

# Projection Matrix
matrix_w = np.hstack((eig_pairs[0][1].reshape(4,1),
                      eig_pairs[1][1].reshape(4,1)))

print 'Matrix W:\n', matrix_w

Y = X_std.dot(matrix_w)

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
# cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])  # red green blue
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])   # red green blue

# plot
plt.figure(figsize=(16,8))

plt.subplot(1,2,1)
plt.scatter(Y[:,0], Y[:,1], c=df['target'], cmap=cmap_bold, alpha=.8, s=40)
plt.title('True Target')
plt.grid()

# kMeans on decomposed Y
from scipy.cluster.vq import kmeans, vq, whiten
centroids, dist =kmeans(Y,3)
idx, idxdist = vq(Y, centroids)
plt.subplot(1,2,2)
plt.scatter(Y[:,0], Y[:,1], c=idx.reshape(150,1),  alpha=.8, s=40)
plt.title('kMeans on decomposed Y')
plt.grid()
