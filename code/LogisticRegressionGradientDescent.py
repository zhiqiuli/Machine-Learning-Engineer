import numpy as np

class LogitGradient:
    def __init__(self):
        self.lr = 0.01

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def fit(self, data, label):
        n = data.shape[0]
        p = data.shape[1]
        w = w_prev = np.zeros((p,1))
        b = b_prev = 0

        while True:
            z = np.dot(data,w) + b
            a = self.sigmoid(z)
            dw = np.dot(data.T, (a-label))/n # how dw and db are defined are important to remember directly
            db = np.sum(a-label)/n

            w = w - self.lr*dw
            b = b - self.lr*db

            if np.sum(np.abs(w-w_prev)<1e-6)==p:
                break

            w_prev = w.copy()
            b_prev = b

        self.w = w
        self.b = b

        return self.w

n = 100
p = 4
np.random.seed(0)
data = np.random.randn(n,p)
label = np.random.randint(2,size=(n,1))
g = LogitGradient()
g.fit(data,label)

print(g.w)