import math
import sys
import os

file=open(sys.argv[1], 'r')

#b = os.path.getsize("prime.dat")

#print(size(file))
count=0
lijst=[]
for line in file:
    lijst.append(line)
    count=count+1
    

N=Largest_Prime=int(lijst[-1])

def pi(N):
    count=0
    for line in open(sys.argv[1], 'r'):
        count=count+1
    return count

N/math.log(N)

ratio=pi(N)/(N/math.log(N))

def pi_2(N):
    lijst=[]
    twin=0
    for line in open(sys.argv[1], 'r'):
        lijst.append(int(line))
    for i in range(len(lijst)):
       if lijst[i]-lijst[i-1]==2:
            twin=twin+1
    return twin

C=0.6601618
2*C*N/(math.log(N)**2)
ratio2=(pi_2(N)*((math.log(N))**2))/(2*C*N)

print('Largest Prime =', Largest_Prime)

print('pi(N) =', pi(N))
print('N/log(N) =', N/math.log(N))
print('ratio =', ratio)

print('pi_2(N) = ', pi_2(N))
print('2CN/log(N)^2 =', 2*C*N/(math.log(N)**2))
print('ratio =', ratio2)






            
