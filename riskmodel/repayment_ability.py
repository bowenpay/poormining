# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import MySQLdb
import math
import numpy as np
import pandas as pd


class RepaymentAbilityModel(object):
    """ 还款能力模型 """
    features = [
        'name',
        'person_year_total_income', 'year_total_income', 'debt_total',

        'tv', 'washing_machine', 'fridge', 'call_number', 'is_danger_house',

        'card_number'

    ]

    def run(self, year):
        """ 使用还款能力模型，计算得分，并保存到csv """
        df = self._fetch_data(year)
        df['score'] = 0.0
        # 依次计算每一行的得分
        for idx, row in df.iterrows():
            df.set_value(idx, 'score', self.get_score(row))
        # 打印，并存储得分
        print df
        return df.to_csv('data/repayment_ability_%s.csv' % year, encoding='utf-8')

    def get_score(self, row):
        """ 计算每一个用户的得分 """
        # 固定资产
        score = 0
        func = self._score_func()
        # 计算用户所有属性的得分，并累加
        for feature in self.features:
            # 获取属性值及对应函数，计算单个属性的得分
            feature_func = func.get(feature)
            feature_value = row[feature]
            # 如果该属性没有对应计算函数，则得分忽略。有则使用函数计算得分
            if feature_func:
                #print feature
                feature_score = feature_func(feature_value)
                if math.isnan(feature_score):
                    feature_score = 0
                score += feature_score

        return score

    def _fetch_data(self, year):
        """ 获取数据 """
        mysql_cn = MySQLdb.connect(host='localhost', port=3306,user='root', passwd='123456', db='binchuan_data', charset="utf8")
        sql = "select %s from yunnan_all_pinkunhu_%s;" % (", ".join(self.features), year)
        df = pd.read_sql(sql, con=mysql_cn)
        return df

    def _score_func(self):
        """ 计算每个字段贡献分值的函数 """
        return {
            # 收入
            'person_year_total_income': lambda x: x / 100.0,
            'year_total_income': lambda x: x / 400.0,
            'debt_total': lambda x: -x / 400.0,
            # 固定资产
            'tv': lambda x: 5 if x else 0,
            'washing_machine': lambda x: 5 if x else 0,
            'fridge': lambda x: 5 if x else 0,
            'call_number': lambda x: 5 if x else 0,
            'is_danger_house': lambda x: -10 if x == '是' else 0,
        }

if __name__ == '__main__':
    m = RepaymentAbilityModel()
    m.run(2016)
