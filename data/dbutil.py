# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from data.db import get_db_session, ZhenxiongPinkunhu2015, ZhenxiongPinkunhu2016

def update_zhengxiong_2015():
    """ 更新镇雄2015的下一年是否脱贫以及下一年收入增长数据 """
    session = get_db_session()
    # 2016数据
    mappings = {}
    objs = session.query(ZhenxiongPinkunhu2016).all()
    for item in objs:
        mappings[item.card_number] = True
        mappings[item.card_number+'year_total_income'] = item.year_total_income
        mappings[item.card_number+'person_year_total_income'] = item.person_year_total_income

    # 2015数据
    objs = session.query(ZhenxiongPinkunhu2015).all()
    for item in objs:
        if mappings.get(item.card_number):
            item.ny_is_poor = 1
            item.ny_increase_income = (mappings[item.card_number+'year_total_income'] or 0) - (item.year_total_income or 0)
            item.ny_increase_person_income = (mappings[item.card_number+'person_year_total_income'] or 0) - (item.person_year_total_income or 0)
        else:
            print item.id, '不存在'
    session.flush()
    session.commit()




if __name__ == "__main__":
    # get_data()
    # update_zhengxiong_2015()
    pass