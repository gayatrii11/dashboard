from flask import Flask, render_template, request
from flask_mysqldb import MySQL

import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'akshay'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'dashboard_app-dev'

mysql = MySQL(app)

@app.route("/")
def home():
    return "<p>Hello World</p>"

@app.route("/dashboard")
def dashboard():
    path= request.path
    gross_revenue= "$2.3 Bn"
    net_revenue= "$1.4Bn"
    net_profit= "$837 Mn"
    customer_base= "912"
    net_worth= "$1.7 Bn"
    reserve_and_sur="$900 Mn"
    equity= "$800"
    long_term_debt= "$300"

    alert_1= "67%"
    alert_1_area= "North America & America"
    alert_rest= "33%"

    gover_score= "92%"
    five_ent_score= ">90%"
    twenty_ent_score= "60% to 90%" 
    three_ent_score= "<60%"

    return render_template("dashboard.html", **locals())

@app.route("/dashboard/js-chart")
def jschart():
  return render_template("js-chart.html")

@app.route("/dashboard/page-2")
def page_2():
  path= request.path
  return render_template("page-2.html", **locals())