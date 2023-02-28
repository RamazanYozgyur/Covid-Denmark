import plotly.express as px
import pandas as pd
import numpy as np
import sys

def do():
   df=pd.read_csv("cleanBIG.csv")
   df_copy=df

   dfnew=df_copy[df_copy.location=="Denmark"][["date","new_cases_smoothed","new_deaths_smoothed"]].dropna()



   dfnew["new_deaths_smoothed"]=dfnew["new_deaths_smoothed"]/np.max(dfnew["new_deaths_smoothed"])*100

   dfnew["new_cases_smoothed"]=dfnew["new_cases_smoothed"]/np.max(dfnew["new_cases_smoothed"])*100


   fig = px.line(dfnew,x="date", y=["new_cases_smoothed","new_deaths_smoothed"])


   fig.update_traces(mode="markers+lines", hovertemplate=None)
   fig.update_layout(hovermode="x",title="Smoothed new case and smoothed new deaths")


   a=sys.argv[1]

   if int(a)==1:
      fig.write_html("smoothed.html")
   else:
      fig.show()

if __name__=='__main__':
    do()


             
