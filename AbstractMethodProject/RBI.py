from abc import ABC, abstractmethod

class RBIndia(ABC):
    def __init__(self,aadhar, pan, name, address, accType):
        self.aadharNumber = aadhar
        self.panNumber = pan
        self.fullName = name
        self.address = address
        self.accountType=accType




    @abstractmethod
    def AccountOpening(self):
        pass

    def __str__(self):
        return f'''\n{self.__dict__}'''
    
    def __repr__(self):
        return str(self)
    
    @abstractmethod
    def KYC(self):
        pass
    

        
