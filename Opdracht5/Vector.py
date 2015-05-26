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

        
        
            
