import numpy as np

n = 100
p = 0.4

M = np.random.binomial(n, p, (10, 5)) # generate rv's using np.random

M_normalized = np.sum(M / np.sum(M, axis=0), axis=0)

M_normalized = M / np.sum(M, axis=0)

print(M_normalized)