from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Fettah Yildiz',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'Feburary 23, 2023'
    },
    {
        'author': 'Fatih Baygul',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Feburary 25, 2023'
    }
]
# Routes are what we type into browsers to go to different pages
@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts, title='Main')

@app.route("/about")
def about():
    return render_template('about.html', posts=posts, title='About')

if __name__ == '__main__':
    app.run(debug=True )