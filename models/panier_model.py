
from flask_mongoengine import MongoEngine

db = MongoEngine()

import sys
if sys.version_info[0] >= 3:
    unicode = str


class Product(db.Document):
    __collection__ = 'panier'

    structure = {
        '_id': int,
        'id_user': unicode,
        'id_product': unicode,
        'qte': int,
        
         
    }

    def __init__(self,id_user,id_product,qte): 
        self.id_user = id_user
        self.id_product = id_product
        
        self.qte = qte
       

