# libraries 
from flask import Flask, request, jsonify, render_template, url_for, redirect, Response, abort
from pydantic import BaseModel, SecretBytes, SecretStr, ValidationError # to define schema
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField, PasswordField, RadioField, validators
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import sqlite3

# Create Flask application instance, configuration, database 
app = Flask(__name__)

app.config["SECRET_KEY"] = "my_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails_passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

csrf = CSRFProtect()
csrf.init_app(app)

db = SQLAlchemy(app)

# database model 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False, index=True)

# classes 
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Submit')

# create test endpoint 
@app.route('/', methods=['GET']) # this is a decorator, GET retrieves data, just for testing purposes
def hello_root(): 
    return {'message': 'root'}

# create email registration endpoint
@app.route('/enter_email', methods=['GET', 'POST'])
def enter_email():
    loginform = LoginForm(csrf_enabled=True)
    if loginform.validate_on_submit():
        if request.method == 'POST': # for each post request there should be a valid email and password
            data = request.form
            email = data.get('email')
            password = data.get('password')
            # Do something with the email and password
            response = {'message': 'Email and password received'} # extract data
            return jsonify(response), 200
        return render_template('enter_email.html', template_form = loginform)


# Run development server locally
if __name__ == '__main__':
    app.run(debug=True)
