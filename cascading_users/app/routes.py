from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, AddForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('login'))  
    return render_template('index.html', title='Home')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
	print(request.body)
        user1 = User(username=form.username1.data)
        user1.set_password(form.password1.data)
        db.session.add(user1)
        user2 = User(username=form.username2.data)
        user2.set_password(form.password2.data)
        db.session.add(user2)
        db.session.commit()
        flash('Congratulations,Users Registered!')   
    return render_template('add.html', title='add', form=form), 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        form = LoginForm()
        if form.validate_on_submit():
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations,User Registered!')
            #return redirect(url_for('add'))   
        return render_template('login.html', title='user', form=form), 200
    except Exception as err:
        return str(err), 500

@app.route('/form', methods=['GET', 'POST'])
def form():
	if request.method == 'GET':
		return render_template('form.html', title='add users'), 200
	elif request.method == 'POST':
		print(request.form)
		for each in request.form.items():
		    print(each)
		    if each[0].find('user') >= 0:
		        pwd = request.form.get('pswd' + each[0].lstrip('user'))
		        user = User(username=each[1])
		        user.set_password(pwd[1])
		        db.session.add(user)
		db.session.commit()
		return render_template('form.html', title='add users'), 201
	else:
		print(request.method)
		return '', 404
