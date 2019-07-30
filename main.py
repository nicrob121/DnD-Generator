from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/generator")
def generator():
    return render_template("generator.html")

@app.route('/<name>')
def index(name):
    return '<h1>Hello {}!</h1>'.format(name)
