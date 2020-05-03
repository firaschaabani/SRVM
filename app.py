from flask import Flask, render_template, request
from pusher import Pusher
from flask_script import Manager
from flask_bootstrap import Bootstrap
import subprocess
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
subprocess.Popen("../dataexterne.py 1 ", shell=True)


app = Flask(__name__)
app.config['SECRET_KEY']='62fe8b83cbe6c254ab6bbb3a0651a90a'

# configure pusher object
pusher = Pusher(
app_id="985383",
key='7f9e5e2a8f5d816a3717',
secret='0bb0d56205ea2a994ec4',
cluster='eu',ssl=True)


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
    app.run(port=port,debug=True)
