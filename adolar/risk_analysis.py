# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:00:20 2022

@author: Abhinandh N
"""
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2



engine=create_engine('postgresql://postgres:root@localhost:5432/adolar')


conn=engine.connect()

# df=pd.read_csv(r"\Adolar\risk_analytics_base_data.csv",encoding="unicode_escape")
#
# df.to_sql(con=engine,name='tb',if_exists='replace')

query="select * from rcm_base"
df=pd.read_sql(query,conn)




df['Risk Score']=df['Risk Impact']*df['Risk Likelihood']


conditions=[(df['Risk Score']<=3),(df['Risk Score']>3) & (df['Risk Score']<6),(df['Risk Score']>=6)]
results=['Low','Moderate','High']
df['Risk Category']=np.select(conditions, results)


conditions=[(df['Risk Category'].str.upper()=='LOW'),(df['Risk Category'].str.upper()=='MODERATE'),(df['Risk Category'].str.upper()=='HIGH')]
results=[1,2,3]
df['Overall Risk Weight']=np.select(conditions, results)

conditions=[(df['Control Category'].str.upper()=='LOW'),(df['Control Category'].str.upper()=='MODERATE'),(df['Control Category'].str.upper()=='HIGH')]
results=[1,2,3]
df['Control weight']=np.select(conditions, results)

df['Overall Weight']=df['Overall Risk Weight']*df['Control weight']

conditions=[(df['Assessed Effective/Ineffective/Not Assessed']=='Effective'),(df['Assessed Effective/Ineffective/Not Assessed']=='Ineffective'),(df['Assessed Effective/Ineffective/Not Assessed']=='Not Assessed')]
results=[(df['Overall Weight'])*1,(df['Overall Weight'])*.5,0]
df['Assessment Score']=np.select(conditions,results)

df['ERM Risk Migration Status']=((df['Assessment Score']/df['Overall Weight'])*df['Risk Score'])


######Table name should have the month end date.

df.to_sql('rcm_calculations',engine,index=False)



