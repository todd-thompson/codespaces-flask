from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/hello")
@app.route("/hello2")
def hello():
    return render_template("index.html", title="Hello")
