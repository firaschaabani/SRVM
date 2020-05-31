
from flask_mongoengine import MongoEngine

db = MongoEngine()

import sys
if sys.version_info[0] >= 3:
    unicode = str


class Product(db.Document):
    __collection__ = 'product'

    structure = {
        '_id': int,
        'nom': unicode,
        'status': unicode,
        'discount': unicode,
        'description': unicode,
        
        'image': unicode,
        'prix': int,
         
    }

    def __init__(self,nom,status,discount,description,prix,image): 
        self.nom = nom
        self.status = status
        
        self.discount = discount
        self.description = description
        
        self.image = image
        
        self.prix = prix
      
   

