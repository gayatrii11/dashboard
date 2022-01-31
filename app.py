from flask import Flask, render_template
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
    return "<p>Hello, World!</p>"

@app.route("/dashboard")
def dashboard():
    df = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    })   
    fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')   
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("dashboard.html", graphJSON= graphJSON )

@app.route("/dashboard/js-chart")
def jschart():
  return render_template("js-chart.html")