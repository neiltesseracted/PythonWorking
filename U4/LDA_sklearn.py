from sklearn.lda import LDA
from sklearn.decomposition import PCA as sklearnPCA
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
df=pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target']=iris.target
df['target_names']=df['target'].map(lambda x: iris.target_names[x])
df=df.reindex_axis(df.columns[[0,1,2,3,5,4]],axis=1)

# split data table into data X and class labels y
X = df.ix[:,0:4].values
y = iris.target
label_dict = {0: 'Setosa', 1: 'Versicolor', 2:'Virginica'}

# Standardizing
# from sklearn.preprocessing import StandardScaler
# X_std = StandardScaler().fit_transform(X)

# LDA
sklearn_lda = LDA(n_components=2)
X_lda_sklearn = sklearn_lda.fit_transform(X, y)

def plot_scikit_lda(X, y, title, mirror=1):

    # fig, ax = plt.subplots()
    # ax=plt.subplot(111)
    for label,marker,color in zip(
        range(0,3),('^', 's', 'o'),('blue', 'red', 'green')):

        plt.scatter(x=X[:,0][y == label]*mirror,
                y=X[:,1][y == label],
                marker=marker,
                color=color,
                alpha=0.5,
                label=label_dict[label]
                )

    plt.xlabel('LD1')
    plt.ylabel('LD2')

    leg = plt.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.title(title)

    # hide axis ticks
    plt.tick_params(axis="both", which="both", bottom="off", top="off",
            labelbottom="on", left="off", right="off", labelleft="on")

    # remove axis spines
    # ax.spines["top"].set_visible(False)
    # ax.spines["right"].set_visible(False)
    # ax.spines["bottom"].set_visible(False)
    # ax.spines["left"].set_visible(False)

    plt.grid()
    plt.tight_layout
    plt.show()

fig=plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plot_scikit_lda(X_lda_sklearn, y, title='LDA via scikit-learn')

# kMeans on decomposed data
from scipy.cluster.vq import kmeans, vq, whiten
centroids, dist =kmeans(X_lda_sklearn,3)
idx, idxdist = vq(X_lda_sklearn, centroids)

# lazy move to align kmeans' labels with target labels
x0 = (idx==idx[0]).nonzero()
x1 = (idx==idx[75]).nonzero()
x2 = (idx==idx[-1]).nonzero()
idx[x0], idx[x1], idx[x2] = 0,1,2

plt.subplot(1,2,2)
# plt.scatter(X_lda_sklearn[:,0], X_lda_sklearn[:,1], c=idx.reshape(150,1),  alpha=.8, s=40)
plot_scikit_lda(X_lda_sklearn, idx, title='LDA via scikit-learn')
plt.scatter(x=X_lda_sklearn[idx!=y, 0],
                y=X_lda_sklearn[idx!=y, 1],
                marker='x',
                color='k',
                alpha=0.75, s=100)
plt.title('kMeans on LDA data')
# plt.axis('tight')
print "kMeans accuracy on decomposed data:", str((idx==y).sum()) + "/" + str(len(y))

