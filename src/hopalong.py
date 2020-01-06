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
        return y-sgn(x)*sqrt(abs(self.beta*x-self.delta))

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

    def fixed_points(self):
        x, y = var('x, y')
        functions = vector([y-x/abs(x)*sqrt(abs(self.beta*x-self.delta)), self.alpha-x])
        fps = solve([functions[0] == x, functions[1] == y], x, y)
        #fps = solve([self.x_function(x,y) == x, self.y_function(x,y) == y], x, y)
        fx = functions.diff(x)
        fy = functions.diff(y)
        df = matrix([fx, fy]).transpose()
        res = list()
        for i in fps:
            xx = str(i[0]).split("==")[1]
            yy = str(i[1]).split("==")[1]
            av=df(x=sage_eval(xx), y=sage_eval(yy)).eigenvalues()
            av1 = abs(av[0])
            av2 = abs(av[1])
            if(av1 == 1 or av2 == 1):
                res.append([xx, yy, "Punto de silla"])
            elif(av1 < 1):
                if(av2 < 1):
                    res.append([xx, yy, "Atractivo"])
                else:
                    res.append([xx, yy, "Punto de silla"])
            else:
                if(av2 < 1):
                    res.append([xx, yy, "Punto de silla"])
                else:
                    res.append([xx, yy, "Atractivo"])
        return res

    def k_periods_2(self):
        x, y = var('x, y')
        fx = y-x/abs(x)*sqrt(abs(self.beta*x-self.delta))
        fy = self.alpha-x
        fxx = fx(x,y)
        fyy = fy(x)
        return solve([fxx == x, fyy == y], x, y)
    
    def k_periods_3(self):
        x, y = var('x, y')
        fx = y-x/abs(x)*sqrt(abs(self.beta*x-self.delta))
        fy = self.alpha-x
        fx2 = fx(x,y)
        fy2 = fy(x)
        fx3 = fx2(x,y)
        fy3 = fy2(x)
        return solve([fx3 == x, fy3 == y], x, y)
    
    def k_periods_4(self):
        x, y = var('x, y')
        fx = y-x/abs(x)*sqrt(abs(self.beta*x-self.delta))
        fy = self.alpha-x
        fx2 = fx(x,y)
        fy2 = fy(x)
        fx3 = fx2(x,y)
        fy3 = fy2(x)
        fx4 = fx3(x,y)
        fy4 = fy3(x)
        return solve([fx4 == x, fy4 == y], x, y)
            
    def xy_functions(self,x, y):
        return (self.x_function(x,y), self.y_function(x,y))

    def hopa_jacobian(self):
        x, y = var('x, y')
        return jacobian(self.xy_functions(x,y), (x,y))

    def exp_lyapunov(self):
        dfn = 1
        Df = matrix(self.hopa_jacobian())
        for i in range(self.iterations):
            dfn*=det(Df(x=self.x[i][0], y=self.y[i][0]))
        return 1/(2*self.iterations)*log(dfn)
        
