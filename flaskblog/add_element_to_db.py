from flaskblog import db

from flaskblog import User, Post

db.create_all()
user_1 = User(username="Fettah", email="f@demo.com", password="pw")
user_2 = User(username="Fatih", email="f2@demo.com", password="pw")
db.session.add(user_1)
db.session.add(user_2)

User.query.all() # Get all users infos
User.query.first() # Get the first user infos
User.query.filter_by(username='Fettah').all()
user = User.query.filter_by(username='Fettah').first()
user.id
user2 = User.query.get(1)

post_1 = Post(title='Blog 1', content='First Post Content!', user_id = user.id) # user.id = Fettah.id
post_2 = Post(title='Blog 2', content='Second Post Content!', user_id = user.id)

db.session.add(post_1)
db.session.add(post_2)
db.session.commit()

user.posts

for post in user.posts:
    print(post.title)

post = Post.query.first()
post.user_id
post.author