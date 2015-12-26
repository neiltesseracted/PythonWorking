import numpy as np
import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt

# Set seed for reproducible results
np.random.seed(414)

# Gen toy data
X = np.linspace(0, 15, 1000)
y = 3 * np.sin(X) + np.random.normal(1 + X, .2, 1000)

train_X, train_y = X[:700], y[:700]
test_X, test_y = X[700:], y[700:]

train_df = pd.DataFrame({'X': train_X, 'y': train_y})
test_df = pd.DataFrame({'X': test_X, 'y': test_y})

# Linear Fit
poly_1 = smf.ols(formula='y ~ 1 + X', data=train_df).fit()

# Quadratic Fit
poly_2= smf.ols(formula='y ~ 1 + X + I(X**2)', data=train_df).fit()

# plotting
yhat_1=poly_1.params[0]+ poly_1.params[1]*X
yhat_2=poly_2.params[0]+ poly_2.params[1]*X + poly_2.params[2]*(X**2)

plt.scatter(train_X,train_y, s=.5)
plt.scatter(test_X,test_y, s=.5, color='r')

plt.plot(X, yhat_1, color='g')
plt.plot(X, yhat_2, color='y')
