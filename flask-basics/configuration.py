from flask import Flask,render_template,request
app = Flask(__name__)


             #http://localhost:5001/
@app.route('/welcome')         #http://localhost:5001/welcome   -->
def welcome_method():   # i want to invoke this method from browser(client)-- web application
    return "Welcome to sample web-application"


@app.route('/')                 #http://localhost:5001/
def show_calculator_page():
    return render_template('calculator.html')


@app.route('/calculate',methods=['POST','GET'])
def process_elements():
    result = None
    if request.method == 'POST':
        print(request.method, request.args)  #get
        print(request.method,request.form) #post

        formdata = request.form

        action = formdata.get('ADD')
        num1 = int(formdata.get('num1'))
        num2 = int(formdata.get('num2'))

        if action:
            result = num1 + num2

        action = formdata.get('SUB')
        if action:
            result = num1 - num2


    return render_template('calculator.html',response = result)

if __name__ == '__main__':
    app.run(debug=True,port=5001)  # default port --> flask - 5000