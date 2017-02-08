# -*- coding: utf-8 -*-
import hashlib
import MySQLdb
import csv

PROVINCE = '云南省'
CITY = '大理白族自治州'
COUNTY = '宾川县'

def sec(v):
    if not v:
        return ''
    return hashlib.md5(v).hexdigest()

db = MySQLdb.connect(host='localhost', port=3306,user='root', passwd='123456', db='data_fupin', charset="utf8")
cursor = db.cursor()
# # 公务员手机号md5
set1 = set()
sql_format = "select DISTINCT(`call_number`) from `yunnan_all_bangfuren_%s`";
for year in ['2014', '2015', '2016']:
    sql = sql_format % year
    cursor.execute(sql)
    res = cursor.fetchall()
    res_set = {item[0] for item in res}
    print len(res_set)
    set1.update(res_set)

print len(set1)
set1 = set(map(sec, set1))
# 贫困户手机号md5
set2 = set()
sql_format = "select `call_number` from `yunnan_all_pinkunhu_%s`";
for year in ['2014', '2015', '2016']:
    sql = sql_format % year
    cursor.execute(sql)
    res = cursor.fetchall()
    res_set = {item[0] for item in res}
    print len(res_set)
    set2.update(res_set)

print len(set2)
set2 = set(map(sec, set2))

# 掌众用户手机号md5
set3 = set()
with open('zhangzhong_mobile.csv', 'rU') as csvfile:
    spamreader = csv.reader(csvfile)
    spamreader = csv.reader(csvfile, dialect=csv.excel_tab)
    set3 = {row[0] for row in spamreader}

print len(set3)

# 统计重合率
## 在公务员中的重合率
ins1 = set1 & set3
print len(ins1), len(ins1) * 100.0 / len(set3)
## 在贫困户中的重合率
ins2 = set2 & set3
print len(ins2), len(ins2) * 100.0 / len(set3)
# 保存
with open('data/zhangzhong_gongwuyuan.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for item in ins1:
        spamwriter.writerow([item])

with open('data/zhangzhong_pinkunhu.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for item in ins2:
        spamwriter.writerow([item])

exit()
