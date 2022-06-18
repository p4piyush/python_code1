from RBI import *

class SBI(RBIndia):
    def AccountOpening(self,aadhar, pan, name, address, accType,  diposite, age ):
        super().__init__(aadhar, pan, name, address, accType)
        self.dipositeAmount = diposite
        self.personAge =age
        

    def __str__(self):
        return f'''\n{self.__dict__}'''
    
    def __repr__(self):
        return str(self)

    def SBIFunction(self,data1):
        self.mydata=data1
        print(self.mydata)

    def KYC(self,photoUpl,adhrUpl):
        self.isPhotoUploaded = photoUpl
        self.isAdharUploaded = adhrUpl
        print("KYC photo:",self.isPhotoUploaded," Aadhar:",self.isAdharUploaded)
        