from flask import Flask, render_template,request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import pickle
import numpy as np
import requests

app= Flask(__name__)

app.secret_key = 'my secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'Credentials'

mysql = MySQL(app)

movies = pickle.load(open('movie_list.pkl','rb'))
similarity_content = pickle.load(open('similarity.pkl','rb'))
pt= pickle.load(open('pt.pkl','rb'))
similarity_collab =pickle.load(open('similarity_collab.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login',methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'login' in request.form and 'password' in request.form:
        email = request.form['login']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = % s AND password1 = % s', (email, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            msg = 'Logged in successfully !'
            return render_template('home.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)


@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password1' in request.form and 'password2' in request.form :
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password1):
            msg = 'Password must contain a capital letter, a small letter, a number and a special character! Length of password should be 8 or more characters.'
        elif not re.match(password1, password2):
            msg = 'Passwords don\'t match !'
        elif not email or not password1 or not password2:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES ( % s, % s, % s)', (email, password1,password2, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)


@app.route('/recommendation', methods =['GET', 'POST'])
def recommendation():
    return render_template('recommendation.html')

@app.route('/recommend_movies',methods=['post'])
def recommend():
    title = request.form.get('title')
    index = movies[movies['title'] == title].index[0]
    distances = sorted(list(enumerate(similarity_content[index])),reverse=True,key = lambda x: x[1])
    data=[]
    for i in distances[1:6]:
        data.append(movies.iloc[i[0]].title)
        
    index = np.where(pt.index==title)[0][0]
    similar_items = sorted(list(enumerate(similarity_collab[index])),key=lambda x:x[1],reverse=True)[1:6]
    for i in similar_items:
        data.append(pt.index[i[0]])
        

    print(data)

    return render_template('recommendation.html',data=data)