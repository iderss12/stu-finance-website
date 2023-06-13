import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

static = os.path.join(os.path.dirname(__file__), 'static')
app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@127.0.0.1:3306/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postName = db.Column(db.String(100), nullable=False)
    postBody = db.Column(db.Text)

    def __repr__(self):
        return f'<Posts {self.postName}>'


@app.route('/')
def toIndex():
    return redirect(url_for('index'))


@app.route('/index.html')
def index():
    posts = Posts.query.all()
    return render_template('index.html', posts=posts[::-1])


@app.route('/signin', methods=['GET', 'POST'])
def signIn():
    if request.method == "POST":
        details = request.form
        print(details)
        return redirect(url_for('index'))
    return render_template('signin.html')


@app.route('/blog-details.html')
def static_proxy():
    posts = Posts.query.all()
    id = request.args.get("id")
    blog = posts[int(id) - 1]
    return render_template('blog-details.html', blog=blog)


if __name__ == '__main__':
    app.run()
