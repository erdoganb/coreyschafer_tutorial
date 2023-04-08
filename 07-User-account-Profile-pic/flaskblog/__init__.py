from flask import Flask
# for database conneciton and process
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt #need for crypting passwords
from flask_login import LoginManager, login_required

app = Flask(__name__)
# token for csrf security!
app.config['SECRET_KEY'] = "89ebfd5dd8e903591565ac20ea2532d8"
# setting the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)  # this is connecting the app to the database i guess!
bcrypt = Bcrypt(app) # create a instance for app
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes