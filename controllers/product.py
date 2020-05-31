from bson.json_util import dumps
from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from app import mongo,app
from models import product_models
import os

product_ctrl = Blueprint('Product', __name__, static_folder='static', template_folder='templates')





@product_ctrl.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    #else must return something as login-process result
    return


@product_ctrl.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        image = request.files["image"]
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
        print(image)
        product=product_models.Product( request.form['nom'],request.form['status'], request.form['discount'],request.form['description'],request.form['prix'],image.filename)
        pro=product.__dict__
        product1 = {"name": request.form['nom'],
        "qte": request.form['quantite'],
        "description":request.form['description'],
        "discount": request.form['discount']}
    
        products = mongo.db.Product
        post_id = products.insert_one(pro).inserted_id
        post_id
        
        #product.discount = request.form['discount']
        
        return redirect(url_for('/'))

    return render_template('addProduct.html')
 

@product_ctrl.route('/shop', methods=['GET', 'POST'])
def index():
    product_list = mongo.db.Product.find()
    return render_template('front/shop.html', product_list = product_list)


