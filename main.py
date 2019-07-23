from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/validate", methods=['POST'])
def validate():
    username = request.form['user_name']
    password = request.form['password']
    verify_password = request.form['password_verify']
    email = request.form['email']


    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if username == "" or ' ' in username:
        username_error = "Enter a valid username"

    if(len(username) > 20 or len(username) < 3):
            username_error = "Enter a username between 3 and 20 characters"

    if(password == ""):
            password_error = "Enter a password"

    if(password != verify_password):
            verify_password_error= "Passwords do not match"
        
    if(verify_password==""):
            verify_password_error="Please verify your password"

    if (email != ""):
        if ' ' not in email and '@' in email and len(email) > 3 and len(email) < 20:
            email_error = ""
        else:
            email_error = "Please enter a valid email"


    if username_error == "" and password_error == "" and verify_password_error == "" and email_error == "":
        return render_template('welcome.html', user_name=username)
    else:
        return render_template('index.html', user_name_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)





app.run()