class person():
    def __init__(self, pid, pname, padr):
        self.personId=pid
        self.personName=pname
        self.personAddres=padr

    def __str__(self):
        return f'''\n{self.__dict__}'''
    
    def __repr__(self):
        return str(self)

class student(person):
    def __init__(self, sid, sname, sadr, sscode, sgrade):
        self.studientSubjectcode=sscode
        self.studientGrade=sgrade
        super().__init__(sid, sname, sadr)

class employee(person):
    def __init__(self, eid, ename, eadr, esal, eeml, erole):
        self.empSalary=esal
        self.empEmail=eeml
        self.empRole=erole
        super().__init__(eid, ename, eadr)


s1=student(sid=100,sname="Piyush Patil",sscode="English",sgrade="A+",sadr='Wardha')
print(s1)
