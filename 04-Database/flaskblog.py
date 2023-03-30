from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# for database conneciton and process
from flask_sqlalchemy import SQLAlchemy
# for post date-time
from datetime import datetime

app = Flask(__name__)


# token for csrf security!
app.config['SECRET_KEY'] = "89ebfd5dd8e903591565ac20ea2532d8"

# setting the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)  # this is connecting the app to the database i guess!

"""
user_1 = User(username='corey', email='cs@mail.com', password='pass')
user_2 = User(username='john', email='jd@mail.com', password='pass')
"""

# database classes for ORM
# add class is the TABLE, variables are the columns in table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User ('{self.username}', {self.email},{self.image_file})"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post ('{self.title}', {self.date_posted})"


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    }, {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash (f"Account created for {form.username.data}!", "success")
        print("flash çalıştı")
        return redirect(url_for("home"))
    else:
        print("form.validate çalışmadı")
        print(form.errors)
    return render_template('register.html', title='Register', obj=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "a@a.a" and form.password.data == "123":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('NO! Check your username and password.', 'danger')
            
    return render_template('login.html', title='Login', obj=form)


"""
with app.app_context():
    print("db.create !")
    db.create_all()
"""
"""
this can be done within terminal!
    python3
    from flaskblog import *
    app.app_context().push()
    db.create_all()
"""


if __name__ == '__main__':

    app.run(debug=True)
