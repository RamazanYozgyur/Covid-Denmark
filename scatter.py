import pandas as pd
import plotly.express as px
import sys

def do():
   df=pd.read_csv("owid-covid-data.csv")
   df.loc[df[df.location=="Denmark"].index,"color"]="Denmark"

   df_new=df[(df.location=="Niger") | (df.location=="Gambia") | (df.location=="Iraq") | (df.location=="Guatemala") |
   (df.location=="Jordan") | (df.location=="Paraguay") | (df.location=="South Africa") | (df.location=="Dominican Republic")
   | (df.location=="Bangladesh") | (df.location=="Panama") | (df.location=="Malaysia") | (df.location=="Turkey") | (df.location=="Brazil")
   | (df.location=="Moldova") | (df.location=="Australia") | (df.location=="United States") | (df.location=="North Macedonia")
   | (df.location=="UKraine") | (df.location=="Belgium") | (df.location=="Denmark") | (df.location=="Finland")
   | (df.location=="Czechia") | (df.location=="Greece") | (df.location=="Germany") | (df.location=="Italy") | (df.location=="Japan")]

   df1=df_new[["total_deaths_per_million","aged_65_older","location","median_age"]]

   df2=df1.groupby(["location"])[["total_deaths_per_million","median_age","aged_65_older"]].max()

   df2["location"]=df2.index

   df2["color"]="Other countries"

   df2.loc["Denmark","color"]="Denmark"

   df2["total_deaths_per_million"]=round(df2["total_deaths_per_million"])
   df2["median_age"]=round(df2["median_age"])
   df2["aged_65_older"]=round(df2["aged_65_older"])
   x=df2.location


   fig = px.scatter(df2, x='median_age', y='total_deaths_per_million',hover_data={ "color":False},hover_name="location",size="aged_65_older",color="color",
                title="Median age of country and final total deaths where size of bubble imply number of people older than 65",
                labels=dict(median_age="Median age of country",color="Color",
                location="Location", aged_65_older="Percentage of people over 65 in country",total_deaths_per_million="Fİnal total deaths per million"))


   fig.update_layout(legend=dict(
       yanchor="top",
       y=0.99,
       xanchor="left",
       x=0.01,
       traceorder="reversed",
       font=dict(
            family="Courier",
            size=12,
            color="black"
        ),
       bordercolor="White",
       borderwidth=2,

       ) 
    )

   a=sys.argv[1]
   if int(a)==1:
       fig.write_html("scatter.html")
   else:
       fig.show()

if __name__=='__main__':
    do()
