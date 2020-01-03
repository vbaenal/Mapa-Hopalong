import matplotlib.pyplot as mp
import random as rand
from math import sqrt

class Hopalong:

    def __init__(self, alpha=25.0, beta=50.0, delta=1, n_points=50, iterations=5000):
        self.alpha = alpha
        self.beta = beta
        self.delta = delta
        self.n_points = n_points
        self.iterations = iterations
        self.x = list()
        xx=[rand.randint(-100,100) for _ in range(n_points)]
        self.x.append(xx)
        yy=[rand.randint(-100,100) for _ in range(n_points)]
        self.y = list()
        self.y.append(yy)
        self.iterate()

    def x_function(self, i, j):
        return self.y[i][j]-self.sgn(self.x[i][j])*sqrt(abs(self.beta*self.x[i][j]-self.delta))

    def y_function(self, i, j):
        return self.alpha-self.x[i][j]

    def iterate(self):
        for i in range(self.iterations):
            xx = []
            yy = []
            for j in range(self.n_points):
                xx.append(self.x_function(i,j))
                yy.append(self.y_function(i,j))
            self.x.append(xx)
            self.y.append(yy)

    def sgn(self,x):
        if(x>0):
            return 1.
        elif(x<0):
            return -1.
        else:
            return 0.