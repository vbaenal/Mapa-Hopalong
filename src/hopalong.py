import sys

import matplotlib.pyplot as mp
import random as rand
from numpy import sqrt

class Hopalong:

    def __init__(self, alpha=50.0, beta=50.0, gamma=1.0, random_points=25, iterations=20000):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.random_points = random_points
        self.iterations = iterations
        self.x = list()
        xx=[rand.random()*1000 for _ in range(random_points)]
        self.x.append(xx)
        yy=[self.y_function(0,i) for i in range(random_points)]
        self.y = list()
        self.y.append(yy)

    def x_function(self, i, j):
        return self.y[i][j]-self.sgn(self.x[i][j])*sqrt(abs(self.beta*self.x[i][j]-self.gamma))

    def y_function(self, i, j):
        return self.alpha-self.x[i][j]

    def iterar(self):
        for i in range(self.iterations):
            xx = []
            yy = []
            for j in range(self.random_points):
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

    def show(self):
        mp.plot(self.x,self.y,'.')
        mp.savefig('file.png')

hopalong = Hopalong()
hopalong.iterar()
hopalong.show()