import random
import math
import sys

if len(sys.argv)-1 >= 3:
    random.seed(int(sys.argv[3]))

if len(sys.argv)-1<2:
    print('Use: estimate_pi.py N L')
    exit()

d=1                           #afstand tussen de lijnen
L = int(sys.argv[2])          #lengte van de naald
if L>d:
    print('AssertionError: L should be smaller than '+ str(d))
    exit()
N=int(sys.argv[1])            #aantal herhalingen experiment

def drop_needle(l):
    x=random.random()
    a=random.vonmisesvariate(0,0)
    if abs(L*math.cos(a))>abs(d-x):
        return (True)
    else:
        return(False)
juist=0

for i in range(N):
    if drop_needle(L):
        juist+=1            #juist=juist+1

print(str(juist) + ' hits in ' + str(N) + ' tries')

Pi= 2*L*N / juist
print('Pi = '+str(Pi))

    



    

    

