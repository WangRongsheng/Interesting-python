from pyecharts.charts import Map
from api import api
from pyecharts import options as opts
from time import strftime,localtime
geo=Map()
api=api()
data=api.guonei()
data2=api.data()
updatetime=strftime("%Y-%m-%d %H:%M:%S",localtime(data2['modifyTime']/1000))
zhongdata=[]
for a in range(len(data)):
    tempdata=[]
    tempdata.append(data[a]['provinceShortName'])
    tempdata.append(data[a]['currentConfirmedCount'])
    zhongdata.append(tempdata)
pingjun=data2['currentConfirmedCount']/len(data)
geo.set_global_opts(title_opts=opts.TitleOpts(title="国内疫情地图",subtitle="目前共确诊"+str(data2['currentConfirmedCount'])+"例，数据来自丁香园，截止时间："+updatetime),visualmap_opts=opts.VisualMapOpts(max_=pingjun),legend_opts=opts.LegendOpts(is_show=False))
geo.add("确诊",zhongdata, maptype="china")
geo.render('index.html')