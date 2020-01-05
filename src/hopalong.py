#!/usr/bin/sage -python
import matplotlib.pyplot as mp
import random as rand
from math import sqrt
from sage.all import *

class Hopalong:

    def __init__(self, alpha=3., beta=2., delta=1., n_points=50, iterations=5000, xx=None, yy=None):
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

    def x_function(self, x, y):
        return y-self.sgn(x)*sqrt(abs(self.beta*x-self.delta))

    def y_function(self, x, y):
        return self.alpha-x

    def iterate(self):
        for i in range(self.iterations):
            xx = []
            yy = []
            for j in range(self.n_points):
                xx.append(self.x_function(self.x[i][j], self.y[i][j]))
                yy.append(self.y_function(self.x[i][j], self.y[i][j]))
            self.x.append(xx)
            self.y.append(yy)

    def sgn(self,x):
        if(x>0):
            return 1.
        elif(x<0):
            return -1.
        else:
            return 0.

    def xy_functions(self,x, y):
        return (self.x_function(x,y), self.y_function(x,y))

    def fixed_points(self):
        x, y = var('x, y')
        functions = vector([y-self.sgn(x)*sqrt(abs(self.beta*x-self.delta)), self.alpha-x])
        #return solve([functions[0] == x, functions[1] == y], x, y)
        return solve([self.x_function(x,y) == x, self.y_function(x,y) == y], x, y)
        