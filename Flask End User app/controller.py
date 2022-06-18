from configuration import app,db
from flask import request,render_template
from models import Employee

@app.route('/employee/')
@app.route('/employee/welcome')
@app.route('/')
@app.route('/employee')
def welcome_page():
    return render_template('index.html')


@app.route('/employee/save',methods = ['GET','POST'])
def save_update_employee():
    # formdata = request.args
    # print(formdata)
    message = ''
    if request.method == 'POST':
        formdata = request.form
        print(formdata)
        emp = Employee(f_name=formdata.get('empfnm'),
                       m_name=formdata.get('empmnm'),
                       l_name=formdata.get('emplnm'),
                       gender=formdata.get('gender'),
                       age=formdata.get('empage'),
                       email=formdata.get('empemail'),
                       photo=formdata.get('empphoto'),
                       dob=formdata.get('empdob'))
        db.session.add(emp)
        db.session.commit()
        message = "Employee Saved Successfully...!"
    return render_template('add.html',result = message)


def edit_employee():
    pass

def delete_employee():
    pass

@app.route('/employee/list')
def list_of_employees():
    emp_list = Employee.query.all()

    return render_template('list.html',result_list = emp_list)




if __name__ == '__main__':
    app.run(debug=True)