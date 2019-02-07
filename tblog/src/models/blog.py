import uuid
import datetime
from src.database import Database
from src.models.pos import Post

class Blog(object):
    def __init__(self, author, title, description, id=None):
        #set correct local variables
        self.author = author;
        self.title = title;
        self.description = description;
        self.id = uuid.uuid(4).hex if id is None else id

    def new_post(self):
        #get title, content, date with input
        title = input("Input a post title: ")
        content = input("Input content: ")
        date = input("Input a date in format DDMMYY, input nothing if you want to use current date: ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        #make new post from the input to blog and stuff
        p = Post(self.id, title, content, self.author, date, uuid.uuid(4).hex);
        p.save_to_mongo()
        #save post to mongo

    def get_posts(self):
        # 1 line
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        # 1 line, with database
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        # return in json format
        # 4 values
        return {
            'author' : self.author,
            'title' : self.title,
            'description' : self.description,
            'id' : self.id
        }

    @classmethod
    def from_mongo(cls, id):
        # get teh blog data with query from mongo
        # return class with correct data from blog data gotten above^
        ret = Database.find_one(collection='blogs', query={'id' : id})
        return Blog(ret.author, ret.title, ret.description, ret.id)