from configuration import db as ORM


class Employee(ORM.Model):
    __tablename__ = 'EMPLOYEE_MASTER'   #EMPLOYEE_MASTER
    id = ORM.Column('id',ORM.Integer,primary_key=True)
    f_name = ORM.Column('firstname', ORM.String(30))
    m_name = ORM.Column('middlename',ORM.String(30))
    l_name = ORM.Column('lastname', ORM.String(30))
    gender = ORM.Column('gender', ORM.String(30))
    age = ORM.Column('age', ORM.Integer)
    email = ORM.Column('email', ORM.String(30))
    photo = ORM.Column('photo',ORM.String(30))  #blob binary large object...
    dob = ORM.Column('dob',ORM.String(30))




print('Tables are created..')
ORM.create_all()

