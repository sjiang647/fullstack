from flask import Flask, render_template, request, session

from src.common.database import Database
from src.models.user import User
#__name__ is a built in private variable in python that contains '__main__'
#  giving app a name which is something python determines for us that allows us to determine
#  whether we are running the app directly from terminal or not
app = Flask(__name__)
app.secret_key = 'super secret key'


#first define route, then define method that occurs once route is accessed
#defines endpoint '/' and when we access this endpoint it returns hello function
@app.route('/') #www.mysite.com/api/
def hello_method():
    return render_template('login.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None
    return render_template('profile.html', email=session['email'])


if __name__ == '__main__':
    app.run(debug=True)