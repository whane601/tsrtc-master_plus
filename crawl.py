# -*- coding: utf-8 -*-

import os
import json
import csv
import time

from datetime import date
from multiprocessing import Pool


import requests


def Crawler(targets):
    '''Request to Market Information System'''
    # def __init__(self, targets,timestamp):
    try:
        timestamp = int(time.time() * 1000 + 1000000)
        endpoint = 'http://mis.twse.com.tw/stock/api/getStockInfo.jsp'
        channels = 'tse_{}.tw'.format(targets)
        s = '{}?ex_ch={}&json=1&delay=0&_={}'.format(endpoint, channels, timestamp)

        req = requests.session()
        req.get('http://mis.twse.com.tw/stock/index.jsp',
                headers={'Accept-Language': 'zh-TW'})

        response = req.get(s)
        content = json.loads(response.text)
    except Exception as err:
        print(err)
        data = []
    else:
        data = content['msgArray']
    return data

def Recorder(data):
    '''Record data to csv'''

    folder_path = '{}/{}'.format('data', date.today().strftime('%Y%m%d'))

    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)


    for row in data:
        try:
            file_path = '{}/{}.csv'.format(folder_path, row['c'])
            with open(file_path, 'a') as output_file:
                writer = csv.writer(output_file, delimiter=',')
                writer.writerow([
                    row['t'],  # 資料時間
                    row['c'],  # 最近成交價
                    row['tv'],  # 當盤成交量
                    row['v'],  # 當日累計成交量
                    row['a'],  # 最佳五檔賣出價格
                    row['f'],  # 最價五檔賣出數量
                    row['b'],  # 最佳五檔買入價格
                    row['g']  # 最佳五檔買入數量

                ])

        except Exception as err:
            print(err)
            print("@@")


if __name__ == '__main__':
    target = [_.strip() for _ in open('stocknumber.csv', 'r')]
    with Pool(processes=50) as pool:
        contents = pool.map(Crawler, target)
        pool.map(Recorder, contents)
        #print(contents)