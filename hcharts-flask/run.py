# coding = utf-8
"""
@author: zhou
@time:2020/3/2 10:49
@File: run.py
"""

import requests
from flask import Flask, render_template,jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bar/')
def bar_chart():
    return render_template('bar.html')


@app.route('/get_data/')
def get_data():
    total_list = []
    today_list = []
    ncov_data = {}
    headers = {
        'user-agent': '',
        'accept': ''
    }
    url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'
    res = requests.get(url, headers=headers)
    data = res.json()['data']['chinaDayList']
    for i in data:
        date = i['date']
        today = i['today']['confirm']
        total = i['total']['confirm']
        today_list.append({'name': date, 'y': today})
        total_list.append({'name': date, 'y': total})
    ncov_data['today'] = today_list
    ncov_data['total'] = total_list
    return jsonify(ncov_data)


if __name__ == '__main__':
    app.run(debug=True)
