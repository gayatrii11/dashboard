import pandas as pd
import numpy as np

from sqlalchemy import create_engine
import pandas as pd


engine=create_engine('postgresql://postgres:bugatti3Bchiron@localhost:5432/adolar')


conn=engine.connect()


query="select * from rcm_calculations"
df=pd.read_sql(query,conn)


risk_classf_wise=df.groupby(["Risk Classification"]).agg(Overall_Weight=("Overall Weight",np.sum),Assessment_Score=("Assessment Score",np.sum)).reset_index()

# risk_classf_wise.to_excel("risk_Calssification_wise.xlsx")

risk_classf_wise["percentage_score"]=risk_classf_wise["Assessment_Score"]/risk_classf_wise["Overall_Weight"]*100

print(risk_classf_wise)
risk_class_json=risk_classf_wise.to_json()
df.to_sql('risk_classf_wise',engine,index=False)

