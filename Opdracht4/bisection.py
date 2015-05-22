import math

lijst=[]

def findRoot(f, a, b, epsilon):
    if abs(b-a)>epsilon:
        #print(a,b)
        m=(a+b)/2
        #print(m)
        #print(f(m))
        lijst.append(m)

        if f(a)>0 and f(m)<0:
            #print([a,m])
            findRoot(f,a,m,epsilon)
            return

        elif f(a)<0 and f(m)>0:
            #print([a,m])
            findRoot(f,a,m,epsilon)
            return

        elif f(b)>0 and f(m)<0:
            #print([m,b])
            findRoot(f,m,b,epsilon)
            return

        elif f(b)<0 and f(m)>0:
            #print([m,b])
            findRoot(f,m,b,epsilon)
            return
    else:
        print(lijst[-1])
        




    
#root = findRoot(lambda x:x - 1,0,3,.1)




        
    
    
