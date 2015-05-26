import random
import math
import sys

if len(sys.argv)-1 >= 3:
    random.seed(int(sys.argv[3]))

if len(sys.argv)-1<2:
    print('Use: estimate_pi.py N L')
    exit()

N=int(sys.argv[1])            #aantal herhalingen experiment

d=1                           #afstand tussen de lijnen
L = float(sys.argv[2])          #lengte van de naald


def drop_needle(l):
    x=random.random()
    a=random.vonmisesvariate(0,0)
    if abs(L*math.cos(a))>abs(d-x):
        return (True)
    else:
        return(False)
juist=0

if L>d:
    C= 2*L-2*(math.sqrt((L**2)-1)+math.asin(1/L))
    for i in range(N):
        if drop_needle(L):
            juist+=1            #juist=juist+1
            Pi= (C*N)/(juist-N)
            
if L<=d:
    for i in range(N):
        if drop_needle(L):
            juist+=1            #juist=juist+1
            Pi= 2*L*N / juist

print(str(juist) + ' hits in ' + str(N) + ' tries')


print('Pi = '+str(Pi))

    



    

    

