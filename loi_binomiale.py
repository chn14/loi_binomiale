import math

class Binomiale:

    def __init__(self,n,p):
        self.n = n
        self.p = p

    def egal(self,k):
        pk = math.comb(self.n,k)*(self.p**k)*((1-self.p)**(self.n-k))
        print("P(X="+str(k)+")="+str(pk))

    def auplus(self,k):
        pk = 0
        for i in range(k+1):
            pk += math.comb(self.n,i)*(self.p**i)*((1-self.p)**(self.n-i))
        print("P(X<="+str(k)+")="+str(pk))

    def aumoins(self,k):
        pk = 0
        for i in range(k,self.n+1):
            pk += math.comb(self.n,i)*(self.p**i)*((1-self.p)**(self.n-i))
        print("P(X>="+str(k)+")="+str(pk))


