from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/validate", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']


    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if username == "":
        username_error = "Enter a username"
        print(username_error)
    return render_template('index.html')
    






app.run()