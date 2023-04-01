from flask import Flask
# for database conneciton and process
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# token for csrf security!
app.config['SECRET_KEY'] = "89ebfd5dd8e903591565ac20ea2532d8"
# setting the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)  # this is connecting the app to the database i guess!

from flaskblog import routes