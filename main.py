from flask import Flask, request, redirect, render_template

import cgi

import re
import os
import jinja2



app = Flask(__name__)

app.config['DEBUG'] = True



page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Signup</title>
    </head>
    <body>
        <h1>Signup</h1>
"""

page_footer = """
    </body>
</html>
"""
 

def proper_length(entry):
    
    if len(entry) > 2 and len(entry) < 21:
        return True

def proper_email(entry):
    if 2 < len(entry) < 21 and re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", entry) != None:
        return True

def has_spaces(entry):
    if ' ' in entry:
        return True

@app.route('/', methods=["GET"])
def display_form():
    return render_template('table.html', username='', username_error='', password='', password_error='',
     password_check='', password_check_error='', email='', email_error='')


@app.route('/', methods=["POST"])
def validate_information():

    username = request.form['username']
    username_error = ''

    password = request.form['password']
    password_error = ''

    password_check = request.form['verifypassword']
    password_check_error = ''

    email = request.form['email']
    email_error = ''

    if has_spaces(username):
        username_error = 'Your username cannot contain spaces.'

    if has_spaces(password):
        password_error = 'Your password cannot contain spaces.'
        password = ''


    if  not proper_length(username):
        username_error = 'Your username must be between 3 and 20 characters.'
        #username = ''

    if not proper_length(password):
        password_error = 'Your password must be between 3 and 20 characters.'
        

    
    if password != password_check:
        password_check_error = 'Your passwords do not match.'
        password_check = ''
        password = ''
    
    if not proper_email(email) and email != '':
        email_error = 'Your email is not in the correct format or is not between 3 and 20 characters.'

    if not username_error and not password_error and not password_check_error and not email_error:
        name = request.form['username']
        return "Welcome {0}!".format(name)
    else:
        return render_template('table.html', username_error=username_error, password_error=password_error,
        password_check_error=password_check_error, email_error=email_error, username=username, 
        password='', password_check='', email=email)
        
        


app.run()