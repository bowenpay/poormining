# -*- coding: utf-8 -*-
import pandas as pd


class RiskModel(object):
    def run(self):
        self._fetch_data()

    def _fetch_data(self):
        files = ['data/repayment_ability.csv', 'data/repayment_willingness.csv', 'data/stability.csv']
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
        df.to_csv('data/main.csv', encoding='utf-8', columns=['name', 'member_name', 'member_card_number',
                                                              'ability_score', 'willingness_score', 'stability_score',
                                                              'person_year_total_income', 'year_total_income',
                                                              'sex', 'age', 'education', 'health',
                                                              'work_ability', 'work_status', 'work_time'])


if __name__ == '__main__':
    m = RiskModel()
    m.run()
