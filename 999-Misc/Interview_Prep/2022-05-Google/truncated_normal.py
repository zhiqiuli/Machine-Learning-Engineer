import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

mu, sigma = 0, 1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000) # to generate random variables using np.random

a = 1
b = np.inf

# truncated 
print(np.mean(s[s>a]))

# sim mean versus the analytic mean
# https://en.wikipedia.org/wiki/Truncated_normal_distribution
Z = norm.cdf(b) - norm.cdf(a)
print(mu + (norm.pdf(a) - norm.pdf(b)) / Z * sigma)

# cdf of truncated normal
def truncated(x, mu, sigma, a, b):
    eta   = (x - mu) / sigma
    alpha = (a - mu) / sigma
    beta  = (b - mu) / sigma
    Z     = norm.cdf(beta) - norm.cdf(alpha)
    return (norm.cdf(eta) - norm.cdf(alpha)) / Z

x = np.array([1 + 0.1 * i for i in range(21)])
y = truncated(x, mu, sigma, a, b)

plt.plot(x, y)
plt.show()