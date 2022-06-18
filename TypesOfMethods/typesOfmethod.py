class piyush:
    #This is piyush class to demonstrate @staticmethod and @classmethod
    def __init__(self,value):
        self.value=value
        print("This is init of class piyush, value is :",self.value)

    def display_piyush(self,disp):  #instance method
        self.display=disp
        print("This is INSTANCE of class..DisplayMethod :",self.display)

    @classmethod
    def piyush_classmethod(val):
        print("This is class method...value:",val)
    
    @staticmethod
    def piyush_static():
        print("This is class Static method..")

p1=piyush(10)
p1.display_piyush('piyush')
p1.piyush_classmethod()
p1.piyush_static()

    
