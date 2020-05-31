from flask import Flask,session,g, render_template, request,redirect,session,url_for
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

from models import user_model

#subprocess.Popen("../dataexterne.py 1 ", shell=True)

app = Flask(__name__)
app.config['SECRET_KEY']='62fe8b83cbe6c254ab6bbb3a0651a90a'


app.config['MONGO_URI']="mongodb://localhost:27017/rvm"
app.config["IMAGE_UPLOADS"]="static\images"

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

mongo=PyMongo(app)

from pymongo import MongoClient
from forms import *
ListUser=[]
users=[]
Users = mongo.db.users.find({})
for i in Users:
         ListUser.append(i['Name'])  


users=list(mongo.db.users.find({}))

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        for x in users:
            if (str(x['_id'])==(session['user_id'])):
               userclass=user_model.User(x['_id'],x['Birthdate'],x['Name'],x['Gender'],x['Occupation'],x['City'],x['email'],x['pwd'],x['Score'],x['Role'])
               print(userclass)
               g.user =userclass
                 
    

@app.route('/register',methods=['POST','GET'])
def register():

    form=RegistrationForm()
    if request.method == 'POST':
       
    
        users=mongo.db.users
        exists = users.find_one({'Name' : form.username.data})
        if exists is None:
            _hashed=generate_password_hash(form.password.data)
            bd_str=form.bd.data.strftime("%d/%m/%Y ")
            users.insert({'Name':form.username.data,'Birthdate':bd_str,'Gender':form.gender.data,'Occupation':form.occupation.data,'City':form.region.data,'email':form.email.data,'pwd':_hashed,'Score':0,'Role':'user'})
            
           
           
            return render_template('basic-table.html')
        else :
            return render_template('error_404.html')
            #return(get_data())

    return render_template('register-2.html',title='Register',form=form)

@app.route('/home-front')
def index1():
    return render_template('front/index_front.html')

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')
@app.route('/indexback',methods=['GET','POST'])
def indexback():
    return render_template('template-back.html')   
@app.route('/basic_table')
def basic_table():
    return render_template('basic-table.html')
@app.route('/charts')
def chart():
    return render_template('chartjs.html')
@app.route('/Product')
def Produit():
    return render_template('addProduct.html')
@app.route('/login', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['Username']
        password = request.form['password']
        print(password)
        pwd=[]
        for x in ListUser:
             if x== username:
                 user=mongo.db.users.find(({"Name":x}) )
                
                 for i in user:
                     pwd=i['pwd']
                     id=str(i['_id'])
                     
             if(check_password_hash(pwd, password)):
                 
                 session['user_id'] =id
                
                 return redirect(url_for('index1'))
        
        return render_template('login-2.html')
    return render_template('login-2.html')    

@app.route('/gestion')
def gestion():
    return render_template('gestion.html',results=get_data(),set=get_acc(),labels=get_acc_1(),values=get_acc_2())

from controllers import product
app.register_blueprint(blueprint=product.product_ctrl, url_prefix='/product')


if __name__ == '__main__':

    app.run(debug=True)
