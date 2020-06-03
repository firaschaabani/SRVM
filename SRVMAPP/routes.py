from flask import  render_template, request,redirect,session,url_for
from SRVMAPP import app, mongo
from SRVMAPP.forms import *
from flask_login import login_user, current_user, logout_user, login_required ,login_manager
from json import dumps
from SRVMAPP.models.costom_dash import cost_plot




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
            
            if user["Role"]=="user":
                return redirect(url_for('home_front')) 
                
            else :
                return redirect(url_for('gestion'))
#                op=bottles.aggregate([{"$group":{"_id": "$Item","count":{"$sum":1}}}])
#                la=[]
#                for el in op:
#                    la=la+[el]
                
#                return str(la)
        else :
            return render_template('error_404.html')
    #else:
    #    return render_template('error_404.html')


    return render_template('login-2.html',form=form)

@app.route('/home')
def home_front():
    return render_template('front/index_front.html')
@app.route('/shop')
def shop():
    return render_template('front/my_Profile.html')
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html',bott=bot_ts())
@app.route('/indexback',methods=['GET','POST'])
def indexback():
    return render_template('template-back.html')   
@app.route('/basic_table')
def basic_table():
    return render_template('basic-table.html')
@app.route('/charts')
def chart():
    graphJSON = cost_plot("Plastique 30CL Coca")
    return render_template('test_chart.html',
                               graphJSON=graphJSON)
    #return str(cost_plot("Plastique 30CL Coca"))
    #return render_template('chartjs.html')
@app.route('/Product')
def Produit():
    return render_template('addProduct.html')


@app.route('/gestion', methods=['GET', 'POST'])
def gestion():
    result=get_data()
    form=SearchForm()
    form1=SelectBrandprod()
    #form1=UpdateRole()
    users=mongo.db.users
    #forc=cost_plot("Plastique 30CL Coca")
    forc=None
    lab_forc="Choose brand to forecast"
    result=get_data()
    #if request.method == 'POST' : #User controle for the administrator in the user control Section
    if request.method == "POST" and form.validate_on_submit():
        if form.Name.data=='' and form1.submiter.data==False: # display all users
            result=get_data()
            print("Form displayAll is submitted")
            print(str(form1.validate_on_submit()))
            print(str(zip(bot_ts()[0],bot_ts()[0])))
            print(form1.brand.data)
            print(str(form1.submiter.data))
            print(str(form.validate_on_submit()))
        elif form.Name.data != '' and form1.submiter.data==False :# find one user and display it
            user=users.find_one({'Name':form.Name.data})
            result=[user]
            print("Form find is submitted")
            
            #return str(form1.submit.data)    
        elif form.Name.data !='' and form.submit1.data and form1.submiter.data==False : # switch the role of a user (Admin-->user or user--> Admin) and display
            user=users.find_one({'Name':form.Name.data})
            if user["Role"]=="user":
                users.update_one({"Name":form.Name.data},{"$set":{"Role":"Admin"}})
            elif user["Role"]=="Admin":
                users.update_one({"Name":form.Name.data},{"$set":{"Role":"user"}})
            user=users.find_one({'Name':form.Name.data})
            result=[user]
            print("Form Role is submitted")     
        elif form1.submiter.data==True:
            
            forc=cost_plot(form1.brand.data)
            lab_forc=form1.brand.data + " Forecasting"
            print("Form forcast is submitted")

    return render_template('gestion.html',results=result,set=get_acc(),reg_labels=get_acc1()[0],reg_values=get_acc1()[1],values=get_acc_2(),form=form,bar_lab=json.dumps(bot_ts()[0]),bar_val=json.dumps(bot_ts()[1]),pers_val=json.dumps(bot_ts()[2]),form1=form1,costom=forc,lab_forc=lab_forc)

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