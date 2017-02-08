# -*- coding: utf-8 -*-
import hashlib
import pandas as pd
import MySQLdb


PROVINCE = '云南省'
CITY = '大理白族自治州'
COUNTY = '宾川县'

res = set()

mysql_cn = MySQLdb.connect(host='localhost', port=3306,user='root', passwd='123456', db='data_fupin', charset="utf8")
df1 = pd.read_sql("select `member_card_number` from `yunnan_all_pinkunjiating_2014` where province='%s' and city='%s' and county='%s';" % (PROVINCE, CITY, COUNTY), con=mysql_cn)
df2 = pd.read_sql("select `member_card_number` from `yunnan_all_pinkunjiating_2015` where province='%s' and city='%s' and county='%s';" % (PROVINCE, CITY, COUNTY), con=mysql_cn)
df3 = pd.read_sql("select `member_card_number` from `yunnan_all_pinkunjiating_2016` where province='%s' and city='%s' and county='%s';" % (PROVINCE, CITY, COUNTY), con=mysql_cn)

res = set(df1.member_card_number.values.tolist()) | set(df2.member_card_number.values.tolist()) | set(df3.member_card_number.values.tolist())

df = pd.DataFrame(list(res), columns=['member_card_number'])
df.to_csv('data/binchuan.csv')


def sec(v):
    return hashlib.md5(v).hexdigest()


df['md5'] = df['member_card_number'].apply(sec)
print df.shape
df.to_csv('data/binchuan_md5.csv', columns=['md5'], header=False, index=False)
