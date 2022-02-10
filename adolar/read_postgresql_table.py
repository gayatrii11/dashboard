import psycopg2
from sqlalchemy import create_engine
import pandas as pd

engine=create_engine('postgresql://postgres:bugatti3Bchiron@localhost:5432/adolar')


conn=engine.connect()

# df=pd.read_csv(r"C:\Users\DEEbugg\PycharmProjects\Adolar\risk_analytics_base_data.csv",encoding="unicode_escape")
#
# df.to_sql(con=engine,name='tb',if_exists='replace')

query="select * from rcm_base"
df=pd.read_sql(query,conn)

# df.to_excel("rcm_from_postgres.xlsx")
engine=create_engine('postgresql://postgres:bugatti3Bchiron@localhost:5432/adolar')
