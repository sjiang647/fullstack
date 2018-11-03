import uuid
from models.post import Post
import datetime
from database import Database
Database.initialize()

class Blog(object):

    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter Post Title: ")
        content = input("Enter Post Content: ")
        author = self.author
        date = input("Enter Post Date otherwise leave blank for today (in format DDMMYYYY): ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(self.id, title, content, author, date)
        post.saveToMongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert('blogs', self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one('blogs', {'id': id})
        return cls(blog_data['author'], blog_data['title'], blog_data['description'], blog_data['id'])