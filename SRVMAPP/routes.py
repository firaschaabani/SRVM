from flask import  render_template, request,redirect,session,url_for
from SRVMAPP import app, mongo
from SRVMAPP.forms import *




@app.route('/register',methods=['POST','GET'])
def register():

    form=RegistrationForm()
    if request.method == 'POST':
    
        users=mongo.db.users
        exists = users.find_one({'email' : form.email.data})
        if exists is None:
            _hashed=generate_password_hash(form.password.data)
            bd_str=form.bd.data.strftime("%d/%m/%Y ")
            users.insert({'Name':form.username.data,'Birthdate':bd_str,'Gender':form.gender.data,'Occupation':form.occupation.data,'City':form.region.data,'email':form.email.data,'pwd':_hashed,'Score':0,'Role':'user'})
            
            return render_template('basic-table.html')
        else :
            return render_template('error_404.html')
            #return(get_data())

    return render_template('register-2.html',title='Register',form=form)
@app.route('/login', methods=['GET', 'POST'])
def log_in():
    form=LoginForm()
    users=mongo.db.users
    if request.method == 'POST':
        user=users.find_one({'email':form.email.data})
        if user and check_password_hash(user["pwd"],form.password.data):
            #login_user(user,remember=form.remember.data)
            #next_page=request.args.get('next')
            if user["Role"]=="user":
                return redirect(url_for('home_front')) 
            else :
                return redirect(url_for('gestion')) 
        else :
            return render_template('error_404.html')
    #else:
    #    return render_template('error_404.html')


    return render_template('login-2.html',form=form)

@app.route('/home-front')
def home_front():
    return render_template('front/index_front.html')
@app.route('/shop')
def shop():
    return render_template('front/shop.html')
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')
@app.route('/indexback',methods=['GET','POST'])
def indexback():
    return render_template('template-back.html')   
@app.route('/basic_table')
def basic_table():
    return render_template('basic-table.html')
@app.route('/charts')
def chart():
    return render_template('chartjs.html')
@app.route('/Product')
def Produit():
    return render_template('addProduct.html')


@app.route('/gestion')
def gestion():
    return render_template('gestion.html',results=get_data(),set=get_acc(),labels=get_acc_1(),values=get_acc_2())

#@app.route('/model',methods=['POST'])
#def model():
#    return render_template('model-test.html')
'''
@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['image']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)

        # Process your result for human
        # pred_class = preds.argmax(axis=-1)            # Simple argmax
        pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
        result = str(pred_class[0][0][1])               # Convert to string
        return result
    else:    
        return render_template('model-test.html')

'''