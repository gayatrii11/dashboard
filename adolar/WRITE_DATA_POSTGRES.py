from sqlalchemy import create_engine
import pandas as pd

engine=create_engine('postgresql://postgres:root@localhost:5432/adolar')

df=pd.read_excel("RCM_base_data.xlsx")

df.to_sql('rcm_base',engine,index=False)33