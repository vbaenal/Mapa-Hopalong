import matplotlib.pyplot as mp
import random as rand
from math import sqrt

class Hopalong:

    def __init__(self, alpha=3., beta=2., delta=1, n_points=50, iterations=5000, xx=None, yy=None):
        self.alpha = alpha
        self.beta = beta
        self.delta = delta
        self.n_points = n_points
        self.iterations = iterations
        self.x = list()
        self.y = list()
        if(xx == None or yy == None):
            xx=[rand.uniform(-10.,10.) for _ in range(n_points)]
            yy=[rand.uniform(-10.,10.) for _ in range(n_points)]
        else:
            if(len(xx) == len(yy)):
                self.n_points = len(xx)
            else:
                xx = [0.]
                yy = [0.]
                self.n_points = 1
        self.x.append(xx)
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