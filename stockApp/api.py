import requests
from flask import render_template, request, url_for
from stockApp import app
from getStockData import queryStock

@app.route('/')
def index():
    return "hi collin"

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/home', methods=['POST'])
def form():
    ticker = request.form['tickerArr']
    startDate = request.form['startDate']
    endDate = request.form['endDate']
    #'GOOG, APPL' => ['GOOG', 'APPL']
    tickerArr = [ticker]
    return queryStock(tickerArr, startDate, endDate)
