from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'iqwuge92tye0h12ug98y'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authetication Failed"
    return render_template("signin.html")

full_name = ''
username = ''
bio = ''
userinputs = {}


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            userinputs = {'full_name': request.form['full_name'], 'username':request.form['username'], 'bio':request.form['bio']}
            db.child("Users").child(login_session)['user']['localId'].set(user)

            return redirect(url_for('add_tweet'))
        except:
            error = "Authetication Failed"  
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
        tweet = {'tweet_title': request.form['tweet_title'], 'Text': request.form['Text'], 'uid': db.child("Users").child(login_session['user']['localId']).set(user)}
        db.child("Articles").push(tweet)
    return render_template("add_tweet.html")


@app.route('/all_tweets', methods='GET', 'POST')
def all_tweets():
    if request.method == 'GET':
        return render_template('tweets.html')



config = {
  "apiKey": "AIzaSyAr3NsJDDPkr4UhKgu-1ATjBpW5XFFzuac",
  "authDomain": "fir-lab-aa93d.firebaseapp.com",
  "projectId": "fir-lab-aa93d",
  "storageBucket": "fir-lab-aa93d.appspot.com",
  "messagingSenderId": "731672824209",
  "appId": "1:731672824209:web:d81473564536410f67b230",
  "measurementId": "G-Y82MTZYJM6",
  "databaseURL": "https://fir-lab-aa93d-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()



if __name__ == '__main__':
    app.run(debug=True)


    