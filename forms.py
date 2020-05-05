from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from flask_pymongo import PyMongo  
from bson.json_util import dumps  
from bson.objectid import ObjectId   
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from app import mongo



class RegistrationForm(FlaskForm):
    regns=[('Tunis', 'tunis'), ('Ariana', 'ariana'),('Sousse','sousse'),('Kasserine','kasserine')]
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    region = SelectField(u'Region',choices = regns)

    password = PasswordField('Password', validators=[DataRequired()]) 
    submit = SubmitField('Sign Up')
    


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')