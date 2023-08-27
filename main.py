    # libraries 
from flask import Flask, request, jsonify, render_template, url_for, redirect
from pydantic import BaseModel, SecretBytes, SecretStr, ValidationError # to define schema
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

# classes 
class LoginForm(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField('Submit')

# Create Flask application instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"

# create test endpoint 
@app.route('/', methods=['GET']) # this is a decorator, GET retrieves data, just for testing purposes
def hello_root(): 
    return {'message': 'root'}

# create email registration endpoint
@app.route('/enter_email.html', methods=['GET', 'POST'])
def enter_email():
    loginform = LoginForm()
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
    
    
    