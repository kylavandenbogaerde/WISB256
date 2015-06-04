import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from numpy import matrix
from numpy import linalg

class Lorenz:

    def __init__(self, begincoordinaten, sigma_ =10., rho_ =28., beta_ =8./3.):
        self.sigma=sigma_
        self.rho=rho_
        self.beta=beta_
        self.x=begincoordinaten[0]
        self.y=begincoordinaten[1]
        self.z=begincoordinaten[2]

    def f(self, v, t):
        #vergelijkingen
        dx= self.sigma*(v[1] - v[0])
        dy= v[0]*(self.rho- v[2])-v[1]
        dz= v[0] * v[1] - self.beta* v[2]
        return [dx, dy, dz]

    def solve(self,T,dt):
        ts= np.arange(0, T,dt) 
        a=odeint(self.f, [self.x, self.y, self.z], ts)
        return a

    def df(self, u):
        x=u[0]
        y=u[1]
        z=u[2]
        A=matrix([[-self.sigma, self.sigma, 0],[self.rho - z, -1, -x],[y, x, self.beta]])
        return A

    def isStable(self, u):
        A=self.df(u)
        #eigenwaarden=list(linalg.eigvals(A))
        print(eigenwaarden)
        for i in range(len(eigenwaarden)):
            if eigenwaarden[i]>=0:
                return False
        return True
            

