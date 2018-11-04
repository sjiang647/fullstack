import uuid
from src.common.database import Database
import datetime

class Post():


    def __init__(self, blog_id, title, content, author, date = datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self._id = uuid.uuid4().hex if _id is None else _id
        self.date = date
        self.title = title
        self.content = content
        self.author = author

    def saveToMongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return {
            "blog_id": self.blog_id,
            "_id": self._id,
            "date": self.date,
            "title": self.title,
            "content": self.content,
            "author": self.author,
        }

    @classmethod
    def from_mongo(cls, _id):
        post_data = Database.find_one("posts", {"_id": _id})
        return cls(**post_data)

    @staticmethod
    def from_blog(_id):
        return [post for post in Database.find("posts", {"blog_id": _id})]
