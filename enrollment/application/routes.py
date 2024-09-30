from application import app,db
from application.models  import Users
from flask import jsonify, render_template, request, Response, flash, redirect
import json
from application.forms import LoginForm,RegistrationForm


course_data =  [
        {"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, 
        {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, 
        {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, 
        {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, 
        {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}
    ]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', index=True)


@app.route('/register')
def register():
    return render_template('register.html', register=True)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else:
        if request.form.get('email') == 'test@gmail.com':
            flash("You are logged in Sucessfully.", category='success')
            redirect('/index')
        else:
            flash("Sorry, Something went wrong.", category='danger')
            redirect('/login')
    return render_template('login.html', form=form, login=True)


@app.route('/courses')
def courses():
    return render_template('courses.html', course_data = course_data, course=True,term = "Spring 2024")


@app.route('/enrollment', methods=['GET','POST'])
def enrollment():
    hidden_form_data = request.form
    return render_template('enrollment.html', enrollment=True, data=hidden_form_data)


@app.route('/logout')
def logout():
    return render_template('logout.html', logout=True)


@app.route('/api')
@app.route('/api/<idx>')
def api(idx=None):
    if idx == None:
        jdata = course_data
    else:
        jdata = course_data[int(idx)]
    return Response(response=json.dumps(course_data),status=200,mimetype='application/json')



@app.route('/users')
def show_users():
    # Users(user_id=1, first_name="Rupesh", last_name="Yadav", email='21bcs11201', password='Hello@dsdf').save()
    # Users(user_id=2, first_name="Ritesh", last_name="Yadav", email='21bai71181', password='Rello@dsdf').save()
    users = Users.objects.all() 
    
    return jsonify(users)