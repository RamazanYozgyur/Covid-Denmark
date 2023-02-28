import pandas as pd
import numpy as np
df1=pd.read_csv("BIG_CSV.csv")
df1.loc[869,"new_cases"]=2001

df1.loc[870:895,'total_cases']+=4002.0

df1.loc[1783,'new_cases']= 4787.0

df1.loc[1783:max(df1[df1.location=='United Kingdom'].index)+1,'total_cases']+=2*4787.0

df1.loc[133,'new_cases']=1
df1.loc[133:max(df1[df1.location=='China'].index)+1,'total_cases']+=2


df1.loc[1783,'new_cases_per_million']=70.515
df1.loc[1783:,'total_cases_per_million']+=2*70.515

df1.loc[133,'new_cases_per_million']=0.001
df1.loc[133:max(df1[df1.location=='China'].index)+1,'total_cases_per_million']+=2*0.001

df1.loc[869,'total_cases_per_million']=39660.902
df1.loc[870:max(df1[df1.location=='Denmark'].index)+1,'total_cases_per_million']+=2*345.464

df1.to_csv('cleanBIG.csv',index=False)
