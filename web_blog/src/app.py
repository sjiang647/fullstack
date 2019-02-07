from flask import Flask, render_template, request, session

from src.common.database import Database
from src.models.blog import Blog
from src.models.user import User
#__name__ is a built in private variable in python that contains '__main__'
#  giving app a name which is something python determines for us that allows us to determine
#  whether we are running the app directly from terminal or not
app = Flask(__name__)
app.secret_key = 'super secret key'


#first define route, then define method that occurs once route is accessed
#defines endpoint '/' and when we access this endpoint it returns hello function
@app.route('/login') #www.mysite.com/api/login
def login_template():
    return render_template('login.html')

@app.route('/register') #www.mysite.com/api/login
def register_template():
    return render_template('register.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/')
def home_template():
    return render_template('home.html')
@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None
    return render_template('profile.html', email=session['email'])

@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']
    User.register(email, password)
    return render_template('profile.html', email=session['email'])

@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def user_blogs(user_id=None):
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session['email'])
    blogs = user.get_blogs()
    return render_template("user_blogs.html", blogs=blogs, email=user.email)

@app.route('/blogs/new', methods=['POST', 'GET'])
def create_new_blog():
    if request.method == 'GET':
        return render_template('new_blog.html')
    else:
        title = request.form['title']
        description = request.form['content']
        user = User.get_by_email(session['email'])

        new_blog = Blog(user.email, title, description, user._id);
        new_blog.save_to_mongo()
        return make_response(user_blogs(user._id))

@app.route('/posts/<string:blog_id>')
def blog_posts(blog_id):
    blog = Blog.get_from_mongo(blog_id)
    posts = blog.get_posts()
    return render_template('posts.html', posts=posts, blog_title=blog.title)



if __name__ == '__main__':
    app.run(debug=True)