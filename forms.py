from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime
from flask_pymongo import PyMongo  
from bson.json_util import dumps
import json
from bson.objectid import ObjectId   
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from app import mongo



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
    users=mongo.db.rvm
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
    users=mongo.db.rvm
    lis_occ=users.distinct("Occupation")
    lis_red=[]
    for doc in lis_occ:
        nbr=users.find({"Occupation":doc}).count()
        lis_red=lis_red+[nbr]
    colors=["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1","#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]   
    #dec={lis_occ[i]: lis_red[i],"color":colors[i]  for i in range(len(lis_occ))}
    zipped=zip(lis_occ,lis_red,colors)
    
    return zipped

def get_acc_1():
    users=mongo.db.rvm
    l=[]
    lis_occ=users.distinct("Occupation")
    l = "".join([str(elem) for elem in lis_occ]) 


    return l

def get_acc_2():
    users=mongo.db.rvm
    lis_occ=users.distinct("Occupation")
    lis_red=[]
    for doc in lis_occ:
        nbr=users.find({"Occupation":doc}).count()
        lis_red=lis_red+[nbr]
    
    
    return lis_red



