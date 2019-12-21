import sys

import matplotlib.pyplot as mp
from numpy import sqrt

class Hopalong:

    def __init__(self, alpha=50.0, beta=50.0, gamma=0.0, random_points=25, iterations=2000):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.random_points = random_points
        self.iterations = iterations
        self.x=[0.]
        self.y=[0.]

    def x_function(self, i):
        return self.y[i]-self.sgn(self.x[i])*sqrt(abs(self.beta*self.x[i]-self.gamma))

    def y_function(self, i):
        return self.alpha-self.x[i]

    def iterar(self):
        for i in range(self.iterations):
            xx=self.x_function(i)
            yy=self.y_function(i)
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
        mp.plot(self.x,self.y)
        mp.savefig('file.png')

hopalong = Hopalong()
hopalong.iterar()
hopalong.show()