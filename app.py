from flask import Flask, render_template, request
from flask_mysqldb import MySQL

import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

""" app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dashboard' """

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



@app.route("/dashboard/enterprise-level-risk")
def page_2():
  path= request.path
  
  q1_strategic_risk= 20
  q1_operational_risk= 40
  q1_financial_risk= 50
  q1_regulatory_risk= 80
  q1_reputational_risk= 10

  q2_strategic_risk= 70
  q2_operational_risk= 30
  q2_financial_risk= 10
  q2_regulatory_risk= 50
  q2_reputational_risk= 20

  q3_strategic_risk= 50
  q3_operational_risk= 90
  q3_financial_risk= 20
  q3_reputational_risk= 60
  q3_regulatory_risk= 70

  return render_template("enterprise-level-risk.html", **locals())


@app.route("/dashboard/db-data")
def db_data():
  path= request.path

  cur = mysql.connection.cursor()
  cur.execute("""SELECT * FROM `dashboard`""")
  data = cur.fetchall()
  print(type(data))
  return render_template("db-data.html", **locals())

@app.route("/dashboard/kpi-charts")
def kpi_charts():
  path= request.path

  cur = mysql.connection.cursor()
  cur.execute("""SELECT * FROM `kpi charts`""")
  data = cur.fetchall()
  Current_ratio=data[0][2]
  Acid_test_ratio= data[1][2] 
  Cash_ratio= data[2][2] 
  Net_op_cash_flow_ratio= data[3][2] 
  DSO= data[4][2] 
  return render_template("kpi_charts.html", **locals())


@app.route("/dashboard/js-chart")
def jschart():
  return render_template("js-chart.html")
