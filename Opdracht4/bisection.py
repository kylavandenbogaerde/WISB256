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




        
    
    
