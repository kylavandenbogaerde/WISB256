#from array import array

#u=array('d', [1,3,4])
#v=array('d', [2,1,3])
import math
    
            
class Vector:

   # __slots__=('dimensie', 'elementen')
    def __init__(self,n, constante=0):
        self.dimensie=n
        if type(constante)!=list:
            self.vector=[]
            for i in range(n):
                self.vector.append(constante)
        
        else:
            #type(constante)==list:
            self.vector=constante
          #  self.dimensie=n
          #  for i in range(n):
           #     self.vector.append(constante)
            
            
    def __str__(self):
        answer=''
        for j in range(len(self.vector)):
            answer=answer + str(self.vector[j]) + '\n'
        return answer

    def lincomb(self,other,alpha,beta):
        answer=[]
        for i in range(len(self.vector)):
            el=alpha*self.vector[i]+ beta*other.vector[i]
            answer.append(el)
        return Vector(self.dimensie, answer)

    def scalar(self, alpha):
        answer=[]
        for i in range(len(self.vector)):
            el=alpha*self.vector[i]
            answer.append(el)
        return Vector(self.dimensie, answer)

    def inner(self,other):
        answer=0
        for i in range(len(self.vector)):
            el=self.vector[i]*other.vector[i]
            answer=answer+el
        return answer

   
    def norm(self):
        answer=math.sqrt(self.inner(self))
        return answer

        
def GrammSchmidt(lijst):
    genormeerd=[]
    y=lijst[0].norm()
    x=1/y
    e1=lijst[0].scalar(x)
    genormeerd.append(e1)
    for i in range(1, len(lijst)):
        a=Vector(lijst[0].dimensie,0)
        for j in range(i):
            b=lijst[i].inner(genormeerd[j])#/((lijst[j].norm())**2)
            c=genormeerd[j].scalar(b)
            a=a.lincomb(c,1,1)
        u=a.scalar(-1)
        e=lijst[i].lincomb(u,1,1)
        e=e.scalar(1/(e.norm()))
        genormeerd.append(e)
    return genormeerd
            
