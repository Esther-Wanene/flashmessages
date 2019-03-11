from  flask import Flask, flash, redirect, render_template, url_for, request

app = Flask(__name__)
app.secret_key = 'some_secret'

# create a function for the home url which will display contents in index,html
@app.route('/')
def index():
    return render_template('index.html')

# function for the login username is admin and password is secret
# if wrong credentials entered error is displayed
# else flash message is displayed and redirects to index.html
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)