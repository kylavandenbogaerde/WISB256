import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

sigma = 0.0

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


L1=Lorenz([-1,1,0])
ant1=L1.solve(50, 0.01)
print(ant1)

# v = beginpunt
# for alle tijdstippen:
#   v += dv(t, x(-1), y(-1), z(-1)/dt * (deze - vorige) # dv/dt = [ dx/dt, dy/dt, dz/dt ]



fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(ant1[:,0],ant1[:,1],ant1[:,2])
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()    
