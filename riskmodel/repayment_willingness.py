# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import MySQLdb
import math
import numpy as np
import pandas as pd
import logging


class RepaymentWillingnessModel(object):
    """ 还款意愿模型
    """
    features = [
        'member_name',
        # 个人信息 TODO： 有无配偶，有无子女
        'sex', 'age', 'education', 'health',
        # 工作能力
        'work_ability', 'work_status', 'work_time',
        # TODO 家庭背景
        # TODO 贷款记录

        'card_number', 'member_card_number'
    ]

    def run(self):
        """ 使用还款能力模型，计算得分，并保存到csv """
        df = self._fetch_data()
        df['score'] = 0.0
        # 依次计算每一行的得分
        for idx, row in df.iterrows():
            print 's:', self.get_score(row)
            df.set_value(idx, 'score', self.get_score(row))
        # 打印，并存储得分
        print df
        return df.to_csv('data/repayment_willingness.csv', encoding='utf-8')

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
            def _age_func(age):
                if age < 16:
                    return 0
                elif age < 30:
                    return 20
                elif age < 50:
                    return 30
                else:
                    return 10

            self.__score_func = {
                # 个人信息
                'sex': lambda x: {'男': 0, '女': 20}.get(x, 0),
                'age': _age_func,
                'education': lambda x: {'文盲或半文盲': 0, '小学': 5, '初中': 10, '高中': 15, '大专及以上': 20}.get(x, 0),
                'health': lambda x: {'健康': 5, '长期慢性病': -10, '患有大病': -20, '残疾': -20, }.get(x, 0),

                # 工作能力
                'work_ability': lambda x: {'无劳动力': 0, '丧失劳动力': 0, '普通劳动力': 30, '技能劳动力': 40, }.get(x, 0),
                'work_status': lambda x: {'省外务工': 30, '县外省内务工': 30, '乡(镇)外县内务工': 20, '乡(镇)内务工': 20, }.get(x, 0),
                'work_time': lambda x: int(x) if x else 0,
            }
        return self.__score_func


if __name__ == '__main__':
    m = RepaymentWillingnessModel()
    m.run()
