#!env python
#%reset -f 
import pandas as pd
import numpy as np
import requests
import json
import folium
covid19_json = requests.get("https://dashboards-dev.sprinklr.com/data/9043/global-covid19-who-gis.json").content
covid19_json = json.loads(covid19_json)
colname = pd.DataFrame(covid19_json['dimensions'])["name"].append(pd.DataFrame(covid19_json['metrics'])["name"]).to_list()
covid19_dataframe = pd.DataFrame(covid19_json["rows"],columns=colname)
url = "https://www.bobobk.com/wp-content/uploads/2020/05/world-countries.json"
#github 无法连接的话可使用https://www.bobobk.com/wp-content/uploads/2020/05/world-countries.json

df_abb = pd.read_csv("https://www.bobobk.com/wp-content/uploads/2020/05/country_codes.csv",header = None)
dic_abb = {df_abb.iloc[i,1]:df_abb.iloc[i,2] for i in range(np.shape(df_abb)[0])}
covid19_dataframe['fullname'] = covid19_dataframe['Country'].map(dic_abb)

today = covid19_dataframe.day.unique().max()
covid19_dataframe = covid19_dataframe[covid19_dataframe.day == today]
covid19_dataframe['fullname'] = covid19_dataframe['Country'].map(dic_abb)
covid19_dataframe = covid19_dataframe[["Country","fullname","Cumulative Confirmed","Confirmed"]]
#covid19_dataframe.head()

covid19_dataframe["log_total_confirm"] = np.log(covid19_dataframe["Cumulative Confirmed"]+1)
covid19_dataframe["log_new_confirm"] = np.log(covid19_dataframe["Confirmed"]+1)

###raw
m = folium.Map()
folium.Choropleth(geo_data=url,name = "covid-19 total confirm map",data = covid19_dataframe,\
                  columns=["fullname","Cumulative Confirmed"],key_on = "feature.id",
                  fill_color='PuRd',nan_fill_color='white').add_to(m)
m.save("total_confirm.html")
#"feature.properties.ID"

m = folium.Map()
folium.Choropleth(geo_data=url,name = "covid-19 new confirm map",data = covid19_dataframe,\
                  columns=["fullname","Confirmed"],key_on = "feature.id",\
                  fill_color='PuRd',nan_fill_color='white').add_to(m)
m.save("new_confirm.html")


## log
m = folium.Map()
folium.Choropleth(geo_data=url,name = "covid-19 log total confirm map",data = covid19_dataframe,\
                  columns=["fullname","log_total_confirm"],key_on = "feature.id",
                  fill_color='PuRd',nan_fill_color='white').add_to(m)
m.save("log_total_confirm.html")


m = folium.Map()
folium.Choropleth(geo_data=url,name = "covid-19 log new confirm map",data = covid19_dataframe,\
                  columns=["fullname","log_new_confirm"],key_on = "feature.id",\
                  fill_color='PuRd',nan_fill_color='white').add_to(m)
m.save("log_new_confirm.html")

##直接打开当前目录下生成的html就可以了，由于网页需要载入国外站点的地图信息，如果网络连接不快的话请耐心等待

