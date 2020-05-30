from flask import Flask
from pusher import Pusher
from flask_script import Manager
from flask_pymongo import PyMongo  
from bson.json_util import dumps  
from bson.objectid import ObjectId   
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
#from test_model import *

#subprocess.Popen("../dataexterne.py 1 ", shell=True)

app = Flask(__name__)
app.config['SECRET_KEY']='62fe8b83cbe6c254ab6bbb3a0651a90a'
app.config['MONGO_URI']="mongodb+srv://captainAllen:10051994@cluster0-wplmr.mongodb.net/test?retryWrites=true&w=majority"
mongo=PyMongo(app)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

from SRVMAPP import routes