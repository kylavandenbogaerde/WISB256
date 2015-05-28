import math

lijst=[]

def findRoot(f, a, b, epsilon):
    if f(a)==0:
        return a
    if f(b)==0:
        return b
    if abs(b-a)>epsilon:
        #print(a,b)
        m=(a+b)/2
        #print(m)
        #print(f(m))
        lijst.append(m)

        if f(a)>0 and f(m)<0:
            #print([a,m])
            return findRoot(f,a,m,epsilon)
            

        elif f(a)<0 and f(m)>0:
            #print([a,m])
            return findRoot(f,a,m,epsilon)
            

        elif f(b)>0 and f(m)<0:
            #print([m,b])
            return findRoot(f,m,b,epsilon)
            

        elif f(b)<0 and f(m)>0:
            #print([m,b])
            return findRoot(f,m,b,epsilon)
            
    else:
        m=(a+b)/2
        return m

#def f(x):
 #   return x-1
    
#root = findRoot(lambda x:x - 1,0,3,.1)




def findALLRoots(f,a,b,epsilon):
    nulpunten=[]
    aantal_intervallen= int((b-a)/epsilon)
    #print(aantal_intervallen)
    for i in range(aantal_intervallen):
        if f(a+(i+1)*epsilon)*f(a+i*epsilon)<=0:
            wortel=findRoot(f,a+i*epsilon, a+(i+1)*epsilon, epsilon)
            nulpunten=nulpunten+[wortel]
            i=i+1
            #print(nulpunten)
    return (list(set(nulpunten)))

#def findALLRoots(f, a, b, epsilon):
#    nulpunten=[]
#    if f(a)==0:
#        nulpunten.append(a)
#    if f(b)==0:
#        nulpunten.append(b)
#    if abs(b-a)>epsilon:
        #print(a,b)
#        m=(a+b)/2
        #print(m)
        #print(f(m))
#        lijst.append(m)
#        if f(m)==0:
#            nulpunten.append(m)

#        if f(a)*f(m)<0:
            #print([a,m])
#            findALLRoots(f,a,m,epsilon)
            
#        if f(b)*f(m)<0:
            #print([m,b])
#            findALLRoots(f,m,b,epsilon)
           
#    else:
#        m=(a+b)/2
#        nulpunten.append(m)
        #findALLRoots(f,a,m-epsilon,epsilon)
       # findALLRoots(f, m+epsilon, b, epsilon)
#    print(nulpunten)
       # findALLRoots(f, a, b, epsilon)
        
    
    
