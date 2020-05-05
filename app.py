from flask import Flask, render_template, request,redirect,session
from pusher import Pusher
from flask_script import Manager
from flask_bootstrap import Bootstrap
import subprocess
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo  
from bson.json_util import dumps  
from bson.objectid import ObjectId   
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash

subprocess.Popen("../dataexterne.py 1 ", shell=True)


app = Flask(__name__)
app.config['SECRET_KEY']='62fe8b83cbe6c254ab6bbb3a0651a90a'
app.config['MONGO_URI']="mongodb://localhost:27017/rvm"
mongo=PyMongo(app)

from forms import RegistrationForm, LoginForm

@app.route('/register',methods=['POST','GET'])
def register():

    form=RegistrationForm()
    if request.method == 'POST':
    
        users=mongo.db.rvm
        exists = users.find_one({'name' : form.username.data})
        if exists is None:
            _hashed=generate_password_hash(form.password.data)
            users.insert({'name':form.username.data,'email':form.email.data,'region':form.region.data,'pwd':_hashed})
            
            return render_template('basic-table.html')
        else :
            return render_template('basic-table.html')
    return render_template('register-2.html',title='Register',form=form)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')
@app.route('/basic_table')
def basic_table():
    return render_template('basic-table.html')
@app.route('/charts')
def chart():
    return render_template('chartjs.html')
@app.route('/Login')
def log_in():
    return render_template('login-2.html')

if __name__ == '__main__':

    app.run(debug=True)
