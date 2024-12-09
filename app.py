from flask import Flask, request, render_template, redirect, url_for
from db import add_user, authenticate_user

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

# Route: Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if authenticate_user(username, password):
            return "Login Successful!"
        else:
            return "Invalid credentials", 401

    return render_template('login.html', title="Login")


# Route: Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if add_user(username, email, password):
            return redirect(url_for('login'))
        else:
            return "User already exists", 400

    return render_template('register.html', title="Register")


if __name__ == '__main__':
    app.run(debug=True)
