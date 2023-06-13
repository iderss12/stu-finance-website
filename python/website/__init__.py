from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_url_path='',
                static_folder='static',
                template_folder='templates')
    app.config['SECRET_KEY'] = ''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@127.0.0.1:3306/database'

    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app
