import lorenz
from lorenz import *


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
