from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mysqldb import MySQL

db = SQLAlchemy()
mysql = MySQL()

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'
    app.config['MAX_CONTENT_LENGTH'] = 90 * 1024 * 1024

    # for windows

    #app.config['UPLOAD_FOLDER'] = '.\/flask_qa\/static'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mmgoverseas@localhost/flask'

    #app.config['MYSQL_HOST'] = 'localhost'
    #app.config['MYSQL_USER'] = 'root'
    #app.config['MYSQL_PASSWORD'] = 'mmgoverseas'
    #app.config['MYSQL_DB'] = 'flask'
    #mysql = MySQL(app)

    ## for Pythonanywhere ##

    app.config['UPLOAD_FOLDER'] = '/home/mflask/flask_qa_app/flask_qa/static'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mflask:mmgoverseas@mflask.mysql.pythonanywhere-services.com/mflask$default'
    app.config['MYSQL_HOST'] = 'mflask.mysql.pythonanywhere-services.com'
    app.config['MYSQL_USER'] = 'mflask'
    app.config['MYSQL_PASSWORD'] = 'mmgoverseas'
    app.config['MYSQL_DB'] = 'mflask$default'

    mysql = MySQL(app)
    db.init_app(app)
   
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
