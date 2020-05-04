from flask import Flask, render_template, request
from pusher import Pusher
from flask_script import Manager
from flask_bootstrap import Bootstrap
import subprocess
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
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

# configure pusher object
pusher = Pusher(
app_id="985383",
key='7f9e5e2a8f5d816a3717',
secret='0bb0d56205ea2a994ec4',
cluster='eu',ssl=True)

@app.route('/add',methods=['POST'])
def add_user():
    _json=request.json
    _name=_json["name"]
    _email=_json["email"]
    _region=_json["region"]
    _password=_json["pwd"]
    if _name and _email and _region and _password and request.method=='POST':
        _hashed=generate_password_hash(_password)
        id = mongo.db.rvm.insert({"name":_name,'email':_email,'region':_region,'pwd':_hashed})
        resp=jsonify("user added successfully")
        resp.status_code=200
        return resp
    else:
        return None


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/basic_table')
def basic_table():
    return render_template('basic-table.html')
@app.route('/charts')
def chart():
    return render_template('chartjs.html')

'''
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/orders', methods=['POST'])
def order():
    data = request.form
    pusher.trigger(u'order', u'place', {
            u'units': data['units']
    })
    return "units logged"

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('Register.html', title='Register', form=form)
@app.route('/customer', methods=['POST'])
def customer():
    data = request.form
    pusher.trigger(u'customer', u'add', {
            u'name': data['name'],
            u'position': data['position'],
            u'office': data['office'],
            u'age': data['age'],
            u'salary': data['salary'],
    })
    return "customer added"
'''
if __name__ == '__main__':
    manager = Manager(app)
    ##bootstrap = Bootstrap(app)

    port = int(5000)
    app.run(debug=True)
