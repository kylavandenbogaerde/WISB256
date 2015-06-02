import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

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



