# -*- coding: utf-8 -*-
__author__ = 'yijingping'

import pandas as pd
import MySQLdb


mysql_cn = MySQLdb.connect(host='localhost', port=3306,user='root', passwd='123456', db='data_fupin', charset="utf8")
df1 = pd.read_sql('select `province`, `city`, `county`, `sid` from `yunnan_all_pinkunhu_2016`;', con=mysql_cn)
# print df1
# exit()

data = {}
for idx, row in df1.iterrows():
    print idx
    data[row['sid']] = '%s-%s-%s' % (row['province'], row['city'], row['county'])


df = pd.read_sql('select `province`, `city`, `county`, `call_number`, `sid` from `yunnan_all_bangfuren_2016`;', con=mysql_cn)
mysql_cn.close()

df2 = df.drop_duplicates(subset='call_number', keep="first")

for idx, row in df2.iterrows():
    addr = data.get(row['sid'])
    print idx
    if addr:
        row['province'], row['city'], row['county'] = addr.split('-')

df2.groupby(['province', 'city', 'county']).size().to_csv('data/out.igt', encoding='utf-8', header=True)

