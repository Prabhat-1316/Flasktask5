from flask import Flask

app = Flask(__name__) 

@app.route('/')
def homepage ():
    return "home page"

@app.route('/login')
def login ():
    return "Login page"

@app.route('/contact')
def contact ():
    return "Contact page Name: Vishwanath S R"

app.run(debug = True)
