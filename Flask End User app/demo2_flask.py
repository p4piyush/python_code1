import pymysql
pymysql.connect(host='localhost',user='root',password='1234',db='flask_db')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/flask_db'
db = SQLAlchemy(app)
#db --> instance of a SQLALCHEMY --> FLASk --> Flask - Database Connection...


class Employee(db.Model): #model        #Which Database
    id = db.Column('emp_id',db.Integer(),primary_key=True)
    name = db.Column('emp_name',db.String(40))
    email = db.Column('emp_email',db.String(40),unique=True)
    salary = db.Column('emp_salary',db.Float())
    role = db.Column('emp_role',db.String(40))

    def m1(self):
        print('inside m1')
        return
#ORM framework -->

#create table --->
db.create_all() #

#insert
e1 = Employee(id=101,name='AAA',email='abc@gmail.com',salary=28333.45,role='SSE')
db.session.add(e1)
db.session.commit()
e1.m1()

#bulk_insert
e2 = Employee(id=102,name='AAA1',email='abc1@gmail.com',salary=58333.45,role='SSE')
e3 = Employee(id=103,name='AAA2',email='abc2@gmail.com',salary=26333.45,role='SE')
e4 = Employee(id=104,name='AAA3',email='abc3@gmail.com',salary=77333.45,role='Manager')
db.session.add_all([e2,e3,e4])
db.session.commit()

#select query -->
emp1 = Employee.query.filter_by(id=101).first()
print(emp1)

emplist = Employee.query.all()
print(emplist)
#delete
emp2 = Employee.query.filter_by(id=102).first()
if emp2:
    db.session.delete(emp2)
    db.session.commit()

#update
emp3 = Employee.query.filter_by(id=103).first()
if emp3:
    emp3.name = 'Yogesh'
    db.session.commit()