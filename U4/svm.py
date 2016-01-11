import numpy as np
from sklearn import datasets
iris = datasets.load_iris()

from matplotlib.colors import ListedColormap
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])  # red green blue
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])   # red green blue

# cdict_mesh = {0:'#FFAAAA', 1:'#AAFFAA', 2:'#AAAAFF'}    # light red green blue
# cdict_plot = {0:'#FF0000', 1:'#00FF00', 2:'#0000FF'}    # bold red green blue

def plot_estimator(estimator, X, y):
    estimator.fit(X, y)
    x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
    y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = estimator.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    # plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light, vmin=0, vmax=2)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, vmin=0, vmax=2)
    plt.axis('tight')
    #plt.tight_layout()

import matplotlib.pyplot as plt
plt.scatter(iris.data[:, 1], iris.data[:, 2], c=iris.target)
plt.xlabel(iris.feature_names[1])
plt.ylabel(iris.feature_names[2])

from sklearn import svm
svc = svm.SVC(kernel='linear')

# svm 3x6=18 plots
i=0
plt.figure(figsize=(16,12))
for label1 in xrange(0,3):
    for label2 in xrange(label1+1,3):
        for feat1 in xrange(0,4):
            for feat2 in xrange(feat1+1,4):
                i+=1
                rows=range(label1*50, label1*50+50) + range(label2*50,label2*50+50)
                X = iris.data[rows][:,[feat1, feat2]]
                y = iris.target[rows]
                svc.fit(X, y)

                plt.subplot(3,6,i)
                plot_estimator(svc, X, y)
                plt.xlabel(iris.feature_names[feat1])
                plt.ylabel(iris.feature_names[feat2])
plt.tight_layout()
plt.savefig('svm_2labels')

# svm 3 labels
i=0
plt.figure(figsize=(12,9))
for feat1 in xrange(0,4):
    for feat2 in xrange(feat1+1,4):
        i+=1
        rows=range(0,150)
        X = iris.data[rows][:,[feat1, feat2]]
        y = iris.target[rows]
        svc.fit(X, y)

        plt.subplot(2,3,i)
        plot_estimator(svc, X, y)
        plt.xlabel(iris.feature_names[feat1])
        plt.ylabel(iris.feature_names[feat2])
plt.tight_layout()
plt.savefig('svm_3labels')
