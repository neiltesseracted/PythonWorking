from sklearn.lda import LDA
from sklearn.decomposition import PCA as sklearnPCA
import matplotlib.pyplot as plt

# LDA
sklearn_lda = LDA(n_components=2)
X_lda_sklearn = sklearn_lda.fit_transform(X, y)

# PCA
sklearn_pca = sklearnPCA(n_components=2)
X_ldapca_sklearn = sklearn_pca.fit_transform(X_lda_sklearn)

def plot_scikit_lda(X, title, mirror=1):

    ax = plt.subplot(111)
    for label,marker,color in zip(
        range(1,4),('^', 's', 'o'),('blue', 'red', 'green')):

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
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)

    plt.grid()
    plt.tight_layout
    plt.show()

plot_step_lda()
plot_scikit_lda(X_ldapca_sklearn, title='LDA+PCA via scikit-learn', mirror=(-1))
plot_scikit_lda(X_lda_sklearn, title='Default LDA via scikit-learn')