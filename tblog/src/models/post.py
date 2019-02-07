from src.database import Database


class Post(object):
    def __init__(self, blog_id, title, content, author, created_date, id):
        self.blog_id = blog_id
        self.content = content
        self.title = title
        self.author = author
        self.id = id

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())
    def json(self):
        return {
            'id': self.id,
            'blog_id' : self.blog_id,
            'author' : self.author,
            'content' : self.content,
            'title' : self.title,
            'created_date': self.created_date
            }
    @staticmethod
    def from_mongo(id):
        data = Database.find_one(collections='posts', query={'id': id})
        return data
    @staticmethod
    def from_blog(id):
        data = Database.find(collection='posts', query={'blog_id' : id})
        return [post for post in data]