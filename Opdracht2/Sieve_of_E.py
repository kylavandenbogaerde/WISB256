#from math import sqrt
#from math import floor
from math import ceil
import time
import sys
N=int(sys.argv[1])

candidates = list(range(2,N))
#print(candidates)

#j=2
#for j in range(0, sqrt(N)):
#    if(candidates[j] > 0):
#        prime = candidates[j]
#        for i in range(1, N/prime-1):
#            candidates[j+i*prime] = 0        
#    n = n+1


primes=[]

T1 = time.perf_counter()
for j in range(2,N):
    if j in candidates:
        primes.append(j)
        for i in range(2, ceil(N/j)):
            candidates[j*i -2]=0
T2 = time.perf_counter()
#print('Time required', T2 - T1, 'sec.')

print('Found '+ str(len(primes)) +' Prime numbers smaller than ' + str(N) + ' in ' + str(T2-T1)+' sec.')

#print (candidates)
#print(primes)
document = sys.argv[2]

prime_dat= open(document,'w')
for k in range(0,len(primes)):
    print(primes[k],file=prime_dat)
    
 #   prime_dat.write(str(primes[k])+'\n')

prime_dat.close()
    
#for prime in primes:
 #   prime_dat.write(prime)

