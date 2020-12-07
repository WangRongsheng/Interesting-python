import requests
import csv
import json
headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
url = 'http://219.136.133.163:8000/Pages/Commonpage/AsyGetData.asmx/GetParkList'
s=requests.session()
s.get(url, headers=headers)
for i in range(1,318):
    data = {
            'cp': str(i),
            'ps': '10',
            'kw': '',
            'lon': 'undefined',
            'lat': 'undefined',
            'type': 'undefined'
        }
    url = 'http://219.136.133.163:8000/Pages/Commonpage/AsyGetData.asmx/GetParkList'
    res = s.post(url, data=data, headers=headers)
    res.encoding = 'utf-8'
    result=json.loads(res.text)['Result']
    for j in result:
        ParkName=j['ParkName']
        Lon=j['Longitude']
        Lat=j['Latitude']
        with open('tingchechang.csv','a+', newline='', encoding='gb18030') as f:
            f_csv = csv.writer(f)
            f_csv.writerow([ParkName,Lon,Lat])
