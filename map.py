import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import sys



df=pd.read_csv('owid-covid-data.csv')
df_copy=df
df_europe=df_copy[(df_copy.continent=='Europe')][['new_cases','new_deaths','location','date','new_cases_per_million','total_cases_per_million']].fillna(0)



df_europe=df_europe[(df_europe.location!='Guernsey') & (df_europe.location!='Jersey') & (df_europe.location!='Isle of Man')]

df_europe.new_cases_per_million=round(df_europe.new_cases_per_million,0)
df_europe.total_cases_per_million=round(df_europe.total_cases_per_million,0)

df_europe.new_cases_per_million=df_europe.new_cases_per_million.astype(int)
df_europe.total_cases_per_million=df_europe.total_cases_per_million.astype(int)

df_europe=df_europe[df_europe.date > '2020-05-01']


df_europe=df_europe.reset_index().drop(columns="index")

df_europe.date=pd.to_datetime(df_europe.date)

df_europe["day"]=df_europe.date.dt.day

df_europe.date=df_europe.date.astype("str")

df_copy=df_europe

df_copy1=df_copy[(df_copy.day==5) | (df_copy.day==10) |  (df_copy.day==15)  | (df_copy.day==20) | (df_copy.day==25) ]

print(df_copy1)

fig = px.choropleth(df_copy1,

                              locations="location",
                              locationmode = "country names",
                              color="total_cases_per_million",
                              labels={'total_cases_per_million':'Total cases per million'},
                          

                              range_color=(0,110000),
                              scope="europe",
                              animation_frame="date",
                              animation_group="location",

                       
                          )
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 4
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 4
fig.update_layout(title_text = "Map of number of total covid cases per million   in Europe.")
fig.update_geos(projection_type="equirectangular", visible=True, resolution=110)
fig.add_trace(go.Scattergeo(lat=[56.26],lon=[9.50],marker={"color":["Black"],"line":{"width":1},"size":5},
                mode="markers+text",
                text=["Denmark"],textfont={"color":["Black"],"size":[15]},textposition=["top left"]))
fig.write_html("map.html")

