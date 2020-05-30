from flask import Flask, render_template, request,redirect,session

# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
'''
app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SECRET_KEY']='62fe8b83cbe6c254ab6bbb3a0651a90a'
'''
# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
#from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app


# Model saved with Keras model.save()
MODEL_PATH = 'controllers/model_97ACC.h5'

# Load your trained model
model = load_model(MODEL_PATH)
model._make_predict_function()          # Necessary
# print('Model loaded. Start serving...')

# You can also use pretrained model from Keras
# Check https://keras.io/applications/
#from keras.applications.resnet50 import ResNet50
#model = ResNet50(weights='imagenet')
#model.save('')
#print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(200, 150))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='caffe')

    preds = model.predict(x)
    return preds
"""
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('model-test.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        #f = request.files['file']

        # Save the file to ./uploads
        #basepath = os.path.dirname(__file__)
        
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path.replace("\\","/"))
            
        file_path = r"C:\Users\esprit\Desktop\PDS\Resized Images\Plastique\100CL\Vahnia\0224022440.jpg"
        # Make prediction
        preds = model_predict(file_path, model)
        indx=preds.tolist()[0].index(1)    
        # Process your result for human
        # pred_class = preds.argmax(axis=-1)            # Simple argmax
           # ImageNet Decode
                       # Convert to string
        labels= ["Metal 33CL Boga","Metal 33CL Coca","Plastique 100CL Coca","Plastique 100CL Vahnia","Plastique 150CL Coca","Plastique 150CL Marwa","Plastique 150CL Royale","Plastique 150CL Sabrine","Plastique 150CL Safia","Plastique 150CL Tijen","Plastique 2L Fourat","Plastique 2L Jannet","Plastique 2L palma","Plastique 30CL Boga","Plastique 30CL Coca","Plastique 30CL Fanta","Plastique 50CL ElBehi","Plastique 50CL Fanta","Plastique 50CL Melliti","Plastique 50CL Palma","Plastique 50CL Royale","Plastique 50CL Safia"]              
        return labels[indx]
    return None

if __name__ == '__main__':
    app.run(debug=True)
    """