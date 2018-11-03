from database import Database
# from models.post import Post
from models.blog import Blog
from menu import Menu
# blog = Blog('yeet', 'dog', 'hi')
#
# blog.new_post()
# blog.save_to_mongo()
# from_database = Blog.get_from_mongo(blog.id)
# print(blog.get_posts())

menu = Menu()
menu.run_menu()