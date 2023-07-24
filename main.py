# Step 1: Install Python: follow download instructions via https://www.python.org/downloads/

# Step 2: Create virtual environment and activate it 
# in your terminal, type:
# py -3 -m venv .venv
# then: 
# 

# Step 3: Install Flask
# in your terminal: 
# pip install Flask
# to update your installation, you may need to update via your terminal:
# python.exe -m pip install --upgrade pip 
# pip install pydantic  

# Step 4: Import dependencies
# if you get: ModuleNotFoundError: No module named 'Flask'
# check that Flask is installed
# check that the virtual environment and python --version are identical, and/or restart code editor
# once your virtual environment is installed, you can also select it more easily from the interpreter menu 

from flask import Flask, request, jsonify, render_template, url_for, redirect
from pydantic import BaseModel

# Step 5: Create Flask application instance
app = Flask(__name__)

# Step 6: Define routes and endpoints to handle requests: www.getpostman.com
# use Postman to test API activity 
# in same folder as your main.py file, create folder called templaes, create .html file
# also, create folder called static, which will contain your CSS file for styling  

@app.route('/', methods=['GET']) # this is a decorator, GET retrieves data
def hello_root(): 
    return {'message': 'root'}
# other HTTP request methods: GET, POST, PUT, DELETE, PATCH, HEAD, CONNECT, TRACE

@app.route('/enter_email.html', methods=['GET', 'POST'])
def enter_email():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        
        # Do something with the email and password
        
        response = {'message': 'Email and password received'}
        return jsonify(response), 200

    return render_template('enter_email.html') # renders your HTML webpage including CSS styling
    

# Step 7: Run development server locally
if __name__ == '__main__':
    app.run(debug=True)
    
# Step 8: Go to terminal [check you're in your current working directory using pwd to make sure] 
# and start running the server
#  http://localhost:5000/api/hello to test the /api/hello
# side note: Firefox and Chrome display differently! Firefox recommended. 

# Step 9: Start hosting on the Web with Heroku (popular hosting service, 
# usually requires payment but has a free tier)
# free account: sign up via https://dashboard.heroku.com/
# 
# you will need an authenticator app (I used Google Authenticator)
# you will also need to install Heroku's command line interface (CLI) 
# https://devcenter.heroku.com/articles/heroku-cli
# 
# in your terminal: 
# heroku login (you will be taken to a website where you will be prompted to login)
# then, clone Heroku's Python boilerplate code. in your terminal:
# git clone https://github.com/heroku/python-getting-started.git
# heroku create (to create app)
# git push heroku main (to push app)
# heroku ps:scale web=1 (to check instance is running)
# heroku open (to open app in url)


# Step 10. Continue with local development, for learning purposes.