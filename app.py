# libraries 
from flask import Flask, request, jsonify, render_template, url_for, redirect, Response, abort
from pydantic import BaseModel, SecretBytes, SecretStr, ValidationError # to define schema
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect, CSRFError
from wtforms import StringField, SubmitField, PasswordField, RadioField, validators
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash 
import flask_login
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from datetime import datetime


# Create Flask application instance, configuration, database 
app = Flask(__name__)

app.config["SECRET_KEY"] = "my_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails_passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

csrf = CSRFProtect()
csrf.init_app(app)

db = SQLAlchemy(app) # SQLAlchemy is an ORM

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# database model 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False, index=True)
    
# Views from templates
# Any view using FlaskForm to process the request is already getting CSRF protection. 
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
# initialise database
with app.app_context():
    db.create_all()

# create email registration endpoint
@app.route('/enter_email', methods=['GET', 'POST'])
def enter_email():
    loginform = LoginForm(csrf_enabled=True)
    if loginform.validate_on_submit():
        if request.method == 'POST': # for each post request there should be a valid email and password
            data = request.form
            email = data.get('email')
            password = data.get('password')
            if email not in db:
                db.session.add(email, password)
            # Do something with the email and password
            # response = {'message': 'Email and password received'} # extract data
            # return jsonify(response), 200
        return render_template('enter_email.html', User=User.query.all(), template_form = loginform)

# determine what happens when errors are encountered
@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html") 

# as per flask documentation, 
# 'When CSRF validation fails, it will raise a CSRFError. By default 
# this returns a response with the failure reason and a 400 code. 
# You can customize the error response using Flask’s errorhandler().' 
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400

# create test endpoint 
@app.route('/', methods=['GET']) # this is a decorator, GET retrieves data, just for testing purposes
def hello_root(): 
    return {'message': 'root'}


# Run development server locally
if __name__ == '__main__':
    app.run(debug=True) # got strange port error, can be fixed by specifying port like so app.run(debug=True, port=5001)
