# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import MySQLdb
import math
import pandas as pd
import logging


class StabilityModel(object):
    """ 稳定性模型
    """
    features = [
        'member_name',
        # 个人信息
        'health', 'work_ability',

        'card_number', 'member_card_number'
    ]

    def run(self):
        """ 使用稳定性模型，计算得分，并保存到csv """
        df = self._fetch_data()
        df['score'] = 0.0
        # 依次计算每一行的得分
        for idx, row in df.iterrows():
            print 's:', self.get_score(row)
            df.set_value(idx, 'score', self.get_score(row))
        # 打印，并存储得分
        print df
        return df.to_csv('data/stability.csv', encoding='utf-8')

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
                logging.error(feature)
                feature_score = feature_func(feature_value)
                logging.error(type(feature_score))
                if math.isnan(feature_score):
                    feature_score = 0
                score += feature_score

        return score

    def _fetch_data(self):
        """ 获取数据 """
        mysql_cn = MySQLdb.connect(host='localhost', port=3306,user='root', passwd='123456', db='binchuan_data', charset="utf8")
        sql = "select %s from %s;" % (", ".join(self.features), 'yunnan_all_pinkunjiating_2016')
        df = pd.read_sql(sql, con=mysql_cn)
        return df

    def _score_func(self):
        """ 计算每个字段贡献分值的函数 """
        if not hasattr(self, '__score_func_value'):
            self.__score_func = {
                # 个人信息
                'health': lambda x: {'健康': 15, '长期慢性病': 0, '患有大病': -10, '残疾': 0, }.get(x, 0),
                # 工作能力
                'work_ability': lambda x: {'无劳动力': 0, '丧失劳动力': 0, '普通劳动力': 10, '技能劳动力': 20, }.get(x, 0),
            }
        return self.__score_func


if __name__ == '__main__':
    m = StabilityModel()
    m.run()
