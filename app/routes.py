from app import app
from flask import request, render_template, session, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/reservation', methods = ['POST', 'GET'])
def reservation():
    if('user' in session and session['user'] == user['username']):
        if(request.method == 'POST'):
            restaurant = request.form.get('restaurant')
            date = request.form.get('date')
        return render_template("reservation.html")
    return '<h1>You are not logged in.</h1>'

app.secret_key = 'ItShouldBeAnythingButSecret'
user = {"username": "abc", "password": "xyz"}
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user['username'] and password == user['password']:
            session['user'] = username
            return redirect('/dashboard')
        return "<h1>Wrong username or password</h1>"
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    if('user' in session and session['user'] == user['username']):
        return render_template("dashboard.html")
    return '<h1>You are not logged in.</h1>'

@app.route('/new_restaurant', methods = ['POST', 'GET'])
def new_restaurant():
    if('user' in session and session['user'] == user['username']):
        if(request.method == 'POST'):
            restaurant = request.form.get('restaurant')
        return render_template("new_restaurant.html")
    return '<h1>You are not logged in.</h1>'

@app.route('/list_reservations')
def list_reservations():
    if('user' in session and session['user'] == user['username']):
        return render_template("list_reservations.html")
    return '<h1>You are not logged in.</h1>'

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')
