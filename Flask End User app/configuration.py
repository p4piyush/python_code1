from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.template_folder = "/pages" #default --> whatever the pages u have-- pages
app.template_folder = "pages/"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/flask_db'
db = SQLAlchemy(app)