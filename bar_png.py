import pandas as pd
import sys
import  plotly.express as px
from utils import *

def do():

    df=pd.read_csv('cleanBIG.csv')

    fig=px.line(x=df[df.location=='Denmark'].date,y=df[df.location=='Denmark'].new_cases_smoothed.fillna(method="pad"),color=px.Constant("Smoothed case"),labels=dict(x="Date",y='Case',color='Case type'), width=1000, height=500)
    fig.add_bar(x=df[df.location=='Denmark'].date,y=df[df.location=='Denmark'].new_cases.fillna(method="pad"),name='New cases')

    fig.update_layout(title="SMOOTHED NEW CASE AND NEW CASES",title_font_color="black",template="plotly_white"
    )
    fig.update_yaxes(showgrid=True)
    fig.update_xaxes(showgrid=True)
    a=sys.argv[1]

    if int(a)==1:
        
        fig.write_image("bar.png")
    else:
        fig.show()
        
if __name__ =='__main__':
    do()
