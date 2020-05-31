
from flask_mongoengine import MongoEngine

db = MongoEngine()

import sys
if sys.version_info[0] >= 3:
    unicode = str


class User(db.Document):
    __collection__ = 'panier'

    structure = {
        '_id': int,
        'Birthdate': unicode,
        'Name': unicode,
        'Gender': unicode,
        
        'Occupation': unicode,
        'City': unicode,
        'email': unicode,
        'pwd': unicode,
        'Score': int,
        'Role': unicode,

        
         
    }

    def __init__(self,_id,Birthdate,Name,Gender,Occupation,City,email,pwd,Score,Role): 
        self._id = _id
        self.Birthdate = Birthdate
        
        self.Name = Name
        self.Gender = Gender
        self.Occupation = Occupation
        
        self.City = City
        self.email = email
        self.pwd = pwd
        
        self.Score = Score
        
        self.Role = Role

