class calulator:
    def __init__(self,n1, n2):
        self.n1=n1
        self.n2=n2
    
    def addition(self):
        res=self.n1+self.n2
        print("Addition",res)

    def substraction(self):
        res=self.n1-self.n2
        print("Subtraction: ",res)
    
    def multiplication(self):
        res=self.n1*self.n2
        print("Multiplication:",res)
    
    def double(self):
        res=(self.n1*2)+(self.n2*2)
        print("Double:",res)
    
    def squre(self):
        res= self.n1**2
        res2=self.n2**2
        print(f"Squre of {self.n1} is {res} and squre of {self.n2} is {res2}")

cal1=calulator(2,3)

cal1.addition()
cal1.substraction()
cal1.multiplication()
cal1.double()
cal1.squre()


