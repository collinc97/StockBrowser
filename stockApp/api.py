from flask import render_template, request
from stockApp import app

@app.route('/')
def index():
    return "index.html"

@app.route('/home')
def home():
    return render_template("index.html")

@app.route("/TEST", methods=['GET', 'POST'])
def TEST():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are using GET"
