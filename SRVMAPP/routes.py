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
            occ_low=form.occupation.data.lower()
            users.insert({'Name':form.username.data,'Birthdate':bd_str,'Gender':form.gender.data,'Occupation':occ_low,'City':form.region.data,'email':form.email.data,'pwd':_hashed,'Score':0,'Role':'user'})
            
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
            render_template('error_404.html')
    #else:
    #    return render_template('error_404.html')


    return render_template('login-2.html',form=form)

@app.route('/home')
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


@app.route('/gestion', methods=['GET', 'POST'])
def gestion():
    result=get_data()
    form=SearchForm()
    #form1=UpdateRole()
    users=mongo.db.users
    if request.method == 'POST': #User controle for the administrator in the user control Section
        if form.Name.data=='': # display all users
            result=get_data()
        elif form.Name.data != '' and form.submit.data:# find one user and display it
            user=users.find_one({'Name':form.Name.data})
            result=[user]
            
        elif form.Name.data !='' and form.submit1.data: # switch the role of a user (Admin-->user or user--> Admin) and display
            user=users.find_one({'Name':form.Name.data})
            if user["Role"]=="user":
                users.update_one({"Name":form.Name.data},{"$set":{"Role":"Admin"}})
            elif user["Role"]=="Admin":
                users.update_one({"Name":form.Name.data},{"$set":{"Role":"user"}})
            user=users.find_one({'Name':form.Name.data})
            result=[user]     
        
    return render_template('gestion.html',results=result,set=get_acc(),labels=get_acc_1(),values=get_acc_2(),form=form)

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