import math
class GeometricProgression:
    def __init__(self,_number_one,_q):
        self.number_one = _number_one
        self.q=_q
    
    def print_number_one(self):
        print(self.number_one)

    def print_q(self):
        print(self.q)

    def input_number_one(self):
        self.number_one = float(input('self.number_one'))
        
    def input_q(self):
    
        q = float(input('q='))
        if q == 0 or q==1:
         raise Exception ("velue is incorrect")
        else:
             self.q = q

    def number_n(self,n):
        return self.number_one * math.pow(self.q,n-1)
    def sum(self,n):
        return (self.number_one*(math.pow(self.q,n)-1))/(self.q-1)

b = GeometricProgression(3,2)
b.input_number_one()
b.input_q()
b.print_number_one()
b.print_q()
print(b.number_n(3))
print(b.sum(4))





