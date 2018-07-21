from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from data import Blogs
from flask_mysqldb import MySQL
from flask_wtf import Form

from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from wtforms.validators import Required
from passlib.hash import sha256_crypt

app = Flask(__name__)

# config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kredo'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# intialise MySQL
mysql = MySQL(app)

Blogs = Blogs()

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/blogs')
def blogs():
  return render_template( 'blogs.html', blogs = Blogs )

@app.route('/blog/<string:id>/')
def blog(id):
  return render_template('blog.html', blog = blog )

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min = 1, max = 50)])
    username = StringField('Username', [validators.Length(min = 4, max = 25)])
    email = StringField('Email', [validators.Length(min = 6, max = 50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create Cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can login', 'success')

        return redirect(url_for('home'))
    return render_template('register.html', form = form)



if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug = True)
