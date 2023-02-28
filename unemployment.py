import pandas as pd
import numpy as np
import plotly.express as px
import sys


def do():

   df=pd.read_csv("Unemployementcln.csv")
   df_copy=df


   fig=px.line(df_copy,x="TIME",y="Value",color="LOCATION",labels=dict(Value="Unemployment rate"))



   a=sys.argv[1]
   if int(a)==1:
       fig.write_html("unemployement.html")
   else:
       fig.show()

if __name__=='__main__':
    do()

