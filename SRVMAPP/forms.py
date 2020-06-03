from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#from datetime import datetime
from flask_pymongo import PyMongo  
from bson.json_util import dumps
import json
from bson.objectid import ObjectId   
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from SRVMAPP import app, mongo
from flask_login import UserMixin



class RegistrationForm(FlaskForm):
    regns=[('Tunis', 'Tunis'), ('Ariana', 'Ariana'),('Sousse','Sousse'),('Kasserine','Kasserine'),('Beja','Beja'),('Gafsa','Gafsa')]
    genders=[('Male', 'Male'), ('Female', 'Female'),('Other','Other')]
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    region = SelectField(u'City',choices = regns,validators=[DataRequired()])
    bd = DateField('BirthDate', format="%d/%m/%Y",validators=[DataRequired()])
    gender=SelectField(u'Gender',choices = genders,validators=[DataRequired()])
    occupation=StringField('Occupation',
                           validators=[DataRequired(), Length(min=2, max=20)])
    
 


    password = PasswordField('Password', validators=[DataRequired()]) 
    submit = SubmitField('Sign Up')
 



class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


def get_data():

    users=mongo.db.users

    doc_str=users.find()
    
    response=[]
    for doc in doc_str:
        doc['_id']=str(doc['_id'])
        #dic=json.loads(doc)
        response.append(doc)
    #print (json.dumps(response))
    
    #print(type(json.dumps(response)[0]))
    #print(json.dumps(response)[0])
    #print(type(response[0]))
    return response
def get_acc():

    users=mongo.db.users

    lis_occ=users.distinct("Occupation")
    lis_red=[]
    for doc in lis_occ:
        nbr=users.find({"Occupation":doc}).count()
        lis_red=lis_red+[nbr]
    colors=["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1","#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]   
    #dec={lis_occ[i]: lis_red[i],"color":colors[i]  for i in range(len(lis_occ))}
    zipped=zip(lis_occ,lis_red,colors)
    
    return zipped



def get_acc_2():

    users=mongo.db.users

    lis_occ=users.distinct("Occupation")
    lis_red=[]
    for doc in lis_occ:
        nbr=users.find({"Occupation":doc}).count()
        lis_red=lis_red+[nbr]
    
    
    return lis_red



class SearchForm(FlaskForm):
    Name = StringField('name')
    submit = SubmitField('Find user')
    submit1 = SubmitField('Switch Role')


class User(UserMixin):
    def __init__(self, user_json):
        self.user_json = user_json

    # Overriding get_id is required if you don't have the id property
    # Check the source code for UserMixin for details
    def get_id(self):
        object_id = self.user_json.get('_id')
        return str(object_id)

def bot_ts():
    op=mongo.db.Bottles.aggregate([{"$group":{"_id": "$Item","count":{"$sum":1}}}])
    la=[]
    lab=[]
    val=[]
    som=0
    som_list=[]
    for el in op:
        la=la+[el]
    for d in la:
        lab=lab+[d['_id']]
        val=val+[d['count']]
    for i in val:
        som=som+i
    for i in val:
        som_list=som_list+[(i*100)/som] 

    return (lab,val,som_list)


class SelectBrandprod(FlaskForm):
    brands=list(zip(bot_ts()[0],bot_ts()[0]))
    brand=SelectField(u'Brand Product',choices=brands,validators=[DataRequired()])
    submiter = SubmitField('Display forecast')


def get_acc1():

    users=mongo.db.users

    lis_labels=users.distinct("City")
    lis_values=[]
    for doc in lis_labels:
        nbr=users.find({"City":doc}).count()
        lis_values=lis_values+[nbr]
    #colors=["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1","#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]   
    #dec={lis_occ[i]: lis_red[i],"color":colors[i]  for i in range(len(lis_occ))}
    
    
    return (json.dumps(lis_labels),json.dumps(lis_values),lis_labels)