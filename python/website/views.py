from flask import Blueprint, render_template, redirect, url_for, request
from .models import Posts, Comments
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def toIndex():
    return redirect(url_for('views.index', lang='en'))


@views.route('/<lang>/index.html', methods=['GET', 'POST'])
def index(lang):
    posts = Posts.query.all()
    return render_template('/' + lang + '/index.html', posts=posts[::-1])

@views.route('/<lang>/error.html', methods=['GET', 'POST'])
def error(lang):
    return render_template('/' + lang + '/error.html')

@views.route('/<lang>/contact.html', methods=['GET', 'POST'])
def contact(lang):
    return render_template('/' + lang + '/contact.html')

@views.route('/<lang>/about.html', methods=['GET', 'POST'])
def about(lang):
    return render_template('/' + lang + '/about.html')


@views.route('/<lang>/blog-details.html', methods=['GET', 'POST'])
def blogDetails(lang):
    postId = int(request.args.get('id'))
    if request.method == 'POST':
        details = request.form
        if details['commenterName'] == '':
            insertComment = Comments(postId, 'Zochin', details['comment'])
        else:
            insertComment = Comments(
                postId, details['commenterName'], details['comment'])
        db.session.add(insertComment)
        db.session.commit()
    posts = Posts.query.all()
    post = Posts.query.get(postId)
    comments = Comments.query.filter(Comments.postId == postId).all()
    numberOfComments = len(comments)
    lenPosts = len(posts)
    posts = posts[::-1]
    return render_template('/' + lang + '/blog-details.html', post=post, posts=posts[0:3], lenPosts=lenPosts, numberOfComments=numberOfComments, comments=comments)


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        details = request.form
        print(details)
        return redirect(url_for('views.index'))
    return render_template('signin.html')


@views.route('/<lang>/blog.html', methods=['GET', 'POST'])
def blog(lang):
    posts = Posts.query.all()
    category = request.args.get('category')
    if category is not None:
        posts = Posts.query.filter(Posts.category == category)
    search = request.args.get('search')
    if search is not None:
        search = ''
    posts = posts[::-1]
    return render_template('/' + lang + '/blog.html', posts=posts)


@views.route('/en/add-blog.html', methods=['GET', 'POST'])
def addBlog():
    if request.method == 'POST':
        details = request.form
        # print(details)
        insertComment = Posts(
            details['postName'], details['postBody'], 'Admin', details['category'])
        db.session.add(insertComment)
        db.session.commit()
    return render_template('add-blog.html')
