class piyushpatil:
    #__init__ method is constructor of as class, this method is called when an object is created, this allows the class to initialize attribute/values
    def __init__(self,name="NOT AVAILABLE",roll=0,division='NOT AVAILABLE'):
        self.n=name
        self.r=roll
        self.d=division
    #self  is used to represent instance of a class, using self keyword we can access attribute/values and method of the class  
    
    def name(self):
        print("Name is :",self.n)
    
    def rollnumber(self):
        print("Roll Number :",self.r)
    
    def division(self):
        print("Division :",self.d)
    

pp=piyushpatil()

pp.name()
pp.rollnumber()
pp.division()