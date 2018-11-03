import uuid
from database import Database
import datetime

class Post():


    def __init__(self, blog_id, title, content, author, date = datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.id = uuid.uuid4().hex if id is None else id
        self.date = date
        self.title = title
        self.content = content
        self.author = author

    def saveToMongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return {
            "blog_id": self.blog_id,
            "id": self.id,
            "date": self.date,
            "title": self.title,
            "content": self.content,
            "author": self.author,
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one("posts", {"id": id})
        return cls(post_data['blog_id'], post_data['title'], post_data['content'], post_data['author'], post_data['datetime'], post_data['id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find("posts", {"blog_id": id})]
