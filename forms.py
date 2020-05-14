from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime
from flask_pymongo import PyMongo  
from bson.json_util import dumps  
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