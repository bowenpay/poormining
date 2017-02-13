# -*- coding: utf-8 -*-
import math
import numpy as np
import pandas as pd
from riskmodel.repayment_ability import RepaymentAbilityModel
from riskmodel.repayment_willingness import RepaymentWillingnessModel
from riskmodel.stability import StabilityModel


class RiskModel(object):
    def run(self, year):
        self._fetch_data(year)

    def _fetch_data(self, year):
        files = ['data/repayment_ability_%s.csv' % year, 'data/repayment_willingness_%s.csv' % year, 'data/stability_%s.csv' % year]
        df1 = pd.read_csv(files[0], usecols=['card_number', 'score', 'name','person_year_total_income', 'year_total_income'])
        df2 = pd.read_csv(files[1], usecols=['card_number', 'member_card_number', 'score',
                                             'sex', 'age', 'member_name', 'education', 'health',
                                             'work_ability', 'work_status', 'work_time',])
        df3 = pd.read_csv(files[2], usecols=['card_number', 'member_card_number', 'score'])
        df1 = df1.rename(index=str, columns={"score": "ability_score"})
        df2 = df2.rename(index=str, columns={"score": "willingness_score"})
        df3 = df3.rename(index=str, columns={"score": "stability_score"})
        # print df1.head()
        # print df2.head()
        # print df3.head()
        print df1.shape, df2.shape, df3.shape
        df = pd.merge(df2, df3, how='inner', on=['card_number', 'member_card_number'])
        df = pd.merge(df, df1, how='left', on=['card_number'])
        print df.shape, df
        df.to_csv('data/main_%s.csv' % year, encoding='utf-8', columns=['name', 'member_name', 'member_card_number',
                                                              'ability_score', 'willingness_score', 'stability_score',
                                                              'person_year_total_income', 'year_total_income',
                                                              'sex', 'age', 'education', 'health',
                                                              'work_ability', 'work_status', 'work_time'])


def main():
    # 生成3年的得分数据
    for year in [2016, 2015, 2014]:
        RepaymentAbilityModel().run(year)
        RepaymentWillingnessModel().run(year)
        StabilityModel().run(year)
        RiskModel().run(year)

    merge_all()


def merge_all():
    # 将3年的得分数据合并
    df1 = pd.read_csv('data/main_2014.csv')
    df2 = pd.read_csv('data/main_2015.csv')
    df3 = pd.read_csv('data/main_2016.csv')
    df = pd.concat([df1, df2, df3])
    df = df.drop_duplicates(subset='member_card_number', keep='last')

    # 正太分布
    # df['ability_score'] -= df['ability_score'].mean()
    # df['ability_score'] /= (df['ability_score'].std())
    #
    # df['willingness_score'] -= df['willingness_score'].mean()
    # df['willingness_score'] /= (df['willingness_score'].std())
    #
    # df['stability_score'] -= df['stability_score'].mean()
    # df['stability_score'] /= (df['stability_score'].std())

    # 归一化
    df['ability_score'] -= df['ability_score'].min()
    df['ability_score'] /= (df['ability_score'].max() - df['ability_score'].min()) / 100

    df['willingness_score'] -= df['willingness_score'].min()
    df['willingness_score'] /= (df['willingness_score'].max() - df['willingness_score'].min()) / 100

    df['stability_score'] -= df['stability_score'].min()
    df['stability_score'] /= (df['stability_score'].max() - df['stability_score'].min()) / 100

    #
    def f(v):
        v = math.sqrt(v) * 10
        v = math.sqrt(v) * 10
        return v

    df['ability_score'] = df['ability_score'].apply(f)

    # 互相叠加10%的影响
    ability_score = df['ability_score'].copy()
    willingness_score = df['willingness_score'].copy()
    stability_score = df['stability_score'].copy()
    df['ability_score'] += (willingness_score * 0.10 + stability_score * 0.10)
    df['willingness_score'] += ability_score * 0.10
    df['stability_score'] += (ability_score * 0.30 + willingness_score * 0.10)


    # 再次归一化
    df['ability_score'] -= df['ability_score'].min()
    df['ability_score'] /= (df['ability_score'].max() - df['ability_score'].min()) / 100

    df['willingness_score'] -= df['willingness_score'].min()
    df['willingness_score'] /= (df['willingness_score'].max() - df['willingness_score'].min()) / 100

    df['stability_score'] -= df['stability_score'].min()
    df['stability_score'] /= (df['stability_score'].max() - df['stability_score'].min()) / 100


    # 排序输出
    df = df.sort_values(['ability_score', 'willingness_score', 'stability_score'], ascending=[0, 0, 0])
    print df.shape
    df.to_csv('data/main.csv', encoding='utf-8')
    # 绘制图形
    from matplotlib import pyplot as plt
    df['ability_score'].hist(bins=100)
    df['willingness_score'].hist(bins=100)
    df['stability_score'].hist(bins=100)
    plt.show()


if __name__ == '__main__':
    # main()
    merge_all()