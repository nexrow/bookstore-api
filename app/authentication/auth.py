from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')#home page

@app.route('/login')
def login():
    return render_template('login.html')#login page

@app.route('/register')
def register():
    return render_template('register.html')#register/sign up up page

if __name__ == '__main__':
    app.run(debug = True)

