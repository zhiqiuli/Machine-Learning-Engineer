# Case 1
# [0.07040479]
# [0.07040479]
# Case 2
# [-0.04435235]
# [-0.04435235]
# Case 3
# [0.02150537]
# [0.02196111]
 
import numpy as np
from sklearn.linear_model import LinearRegression
 
np.random.seed(1)
 
num_samples = 100
 
'''
Case 1
Noncorrelated variables
'''
print('Case 1')
 
# The desired mean values of the sample.
mu = np.array([0.0, 0.0])
 
# The desired covariance matrix.
r = np.array([[1.0, 0.0],
              [0.0, 1.0]])
 
# Generate random samples
y = np.random.normal(0, 1, size=num_samples)
 
# Generate the random samples.
X = np.random.multivariate_normal(mu, r, size=num_samples)
reg = LinearRegression().fit(X, y)
#print(reg.coef_, reg.intercept_)
print(reg.predict(np.array([[0.5, 0.5]])))
 
 
Z = np.array([X[:,1]-X[:,0],X[:,1]+X[:,0]]).T
reg_2 = LinearRegression().fit(Z, y)
#print(reg_2.coef_, reg_2.intercept_)
print(reg_2.predict(np.array([[0, 1]])))
 
 
'''
Case 2
Correlated variables
'''
print('Case 2')
 
# The desired mean values of the sample.
mu = np.array([0.0, 0.0])
 
# The desired covariance matrix.
r = np.array([[1.0, 0.8],
              [0.8, 1.0]])
 
# Generate random samples
y = np.random.normal(0, 1, size=num_samples)
 
# Generate the random samples.
X = np.random.multivariate_normal(mu, r, size=num_samples)
reg = LinearRegression().fit(X, y)
#print(reg.coef_, reg.intercept_)
print(reg.predict(np.array([[0.5, 0.5]])))
 
 
Z = np.array([X[:,1]-X[:,0],X[:,1]+X[:,0]]).T
reg_2 = LinearRegression().fit(Z, y)
#print(reg_2.coef_, reg_2.intercept_)
print(reg_2.predict(np.array([[0, 1]])))
 
 
 
'''
Case 3
Uncorrelated variables with Regularizations
'''
print('Case 3')
 
from sklearn.linear_model import Ridge
 
# The desired mean values of the sample.
mu = np.array([0.0, 0.0])
 
# The desired covariance matrix.
r = np.array([[1.0, 0.0],
              [0.0, 1.0]])
 
# Generate random samples
y = np.random.normal(0, 1, size=num_samples)
 
# Generate the random samples.
X = np.random.multivariate_normal(mu, r, size=num_samples)
reg = Ridge(alpha=1).fit(X, y)
#print(reg.coef_, reg.intercept_)
print(reg.predict(np.array([[0.5, 0.5]])))
 
 
Z = np.array([X[:,1]-X[:,0],X[:,1]+X[:,0]]).T
reg_2 = Ridge(alpha=1).fit(Z, y)
#print(reg_2.coef_, reg_2.intercept_)
print(reg_2.predict(np.array([[0, 1]])))