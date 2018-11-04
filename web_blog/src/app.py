from flask import Flask

#__name__ is a built in private variable in python that contains '__main__'
#  giving app a name which is something python determines for us that allows us to determine
#  whether we are running the app directly from terminal or not
app = Flask(__name__)


#first define route, then define method that occurs once route is accessed
#defines endpoint '/' and when we access this endpoint it returns hello function
@app.route('/') #www.mysite.com/api/
def hello_method():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()