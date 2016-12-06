# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Text, Float
import pandas as pd
from settings import DATABASE

Base = declarative_base()
DB_SESSION = None
# 数据库表

class Pinkunhu(Base):

    __tablename__ = 'yunnan_all_pinkunhu_2015'

    id = Column(String(20), primary_key=True)
    # 住址
    province = Column(String(36 ))
    city = Column(String(36 ))
    county = Column(String(36 ))
    town = Column(String(36 ))
    village = Column(String(36 ))
    group = Column(String(36 ))
    # 基本情况
    name = Column(String(36 ))
    card_number = Column(String(36 ))
    call_number = Column(String(36 ))

    member_count = Column(Integer())
    bank_name = Column(String(36 ))
    bank_number = Column(String(36 ))
    standard = Column(String(36 ))
    reason = Column(String(36 ))
    other_reason = Column(String(36 ))
    is_back_poor = Column(String(36 ))
    poor_status = Column(String(36 ))
    # 生产生活条件
    arable_land = Column(Float())
    wood_land = Column(Float())
    living_space = Column(Float())
    is_danger_house = Column(String(50 ))
    is_debt = Column(String(50 ))
    debt_total = Column(Float())
    year_total_income = Column(Float())
    person_year_total_income = Column(Float())
    subsidy_total = Column(Float())
    xin_nong_he_total = Column(Float())
    xin_yang_lao_total = Column(Float())
    # 帮扶计划
    help_plan = Column(Text())
    # 五查无看
    tv = Column(String(50 ))
    washing_machine = Column(String(50))
    fridge = Column(String(50))


class ZhenxiongPinkunhu2015(Base):

    __tablename__ = 'zhenxiong_2015'

    id = Column(String(20), primary_key=True)
    # 住址
    province = Column(String(36 ))
    city = Column(String(36 ))
    county = Column(String(36 ))
    town = Column(String(36 ))
    village = Column(String(36 ))
    group = Column(String(36 ))
    # 基本情况
    name = Column(String(36 ))
    card_number = Column(String(36 ))
    call_number = Column(String(36 ))

    member_count = Column(Integer())
    bank_name = Column(String(36 ))
    bank_number = Column(String(36 ))
    standard = Column(String(36 ))
    reason = Column(String(36 ))
    other_reason = Column(String(36 ))
    is_back_poor = Column(String(36 ))
    poor_status = Column(String(36 ))
    # 生产生活条件
    arable_land = Column(Float())
    wood_land = Column(Float())
    living_space = Column(Float())
    is_danger_house = Column(String(50 ))
    is_debt = Column(String(50 ))
    debt_total = Column(Float())
    year_total_income = Column(Float())
    person_year_total_income = Column(Float())
    subsidy_total = Column(Float())
    xin_nong_he_total = Column(Float())
    xin_yang_lao_total = Column(Float())
    # 帮扶计划
    help_plan = Column(Text())
    # 五查无看
    tv = Column(String(50 ))
    washing_machine = Column(String(50))
    fridge = Column(String(50))

    # ny_is_poor = Column(Integer())
    # ny_increase_income = Column(Float())
    # ny_increase_person_income = Column(Float())



class ZhenxiongPinkunhu2016(Base):

    __tablename__ = 'zhenxiong_2016'

    id = Column(String(20), primary_key=True)
    # 住址
    province = Column(String(36 ))
    city = Column(String(36 ))
    county = Column(String(36 ))
    town = Column(String(36 ))
    village = Column(String(36 ))
    group = Column(String(36 ))
    # 基本情况
    name = Column(String(36 ))
    card_number = Column(String(36 ))
    call_number = Column(String(36 ))

    member_count = Column(Integer())
    bank_name = Column(String(36 ))
    bank_number = Column(String(36 ))
    standard = Column(String(36 ))
    reason = Column(String(36 ))
    other_reason = Column(String(36 ))
    is_back_poor = Column(String(36 ))
    poor_status = Column(String(36 ))
    # 生产生活条件
    arable_land = Column(Float())
    wood_land = Column(Float())
    living_space = Column(Float())
    is_danger_house = Column(String(50 ))
    is_debt = Column(String(50 ))
    debt_total = Column(Float())
    year_total_income = Column(Float())
    person_year_total_income = Column(Float())
    subsidy_total = Column(Float())
    xin_nong_he_total = Column(Float())
    xin_yang_lao_total = Column(Float())
    # 帮扶计划
    help_plan = Column(Text())
    # 五查无看
    tv = Column(String(50 ))
    washing_machine = Column(String(50))
    fridge = Column(String(50))

    # ny_is_poor = Column(Integer())
    # ny_increase_income = Column(Float())
    # ny_increase_person_income = Column(Float())


def get_db_session():
    global DB_SESSION
    if not DB_SESSION:
        # 初始化数据库连接:
        engine = create_engine('mysql+mysqlconnector://%s:%s@%s:%s/%s' % (
            DATABASE.get('USER'), DATABASE.get('PASSWORD'), DATABASE.get('HOST'),
            DATABASE.get('PORT', 3306), DATABASE.get('NAME'))
        )
        # 创建DBSession类型:
        DB_SESSION = sessionmaker(bind=engine)()
    return DB_SESSION


def clean_data(data):
    for k, v in enumerate(data):
        if isinstance(v, list):
            data[k] = clean_data(v)
        else:
            if v is None:
                data[k] = ''
    return data


def get_data():
    from sklearn.preprocessing import OneHotEncoder
    enc = OneHotEncoder()
    X = [[1,0, '中文'], [1,0,'NO'], [0,0,'YES']]
    enc.fit()
    df = pd.DataFrame(X, ['a', 'b', 'c'])
    df['c'] = pd.Categorical(df['c'])
    Y = [1, 1, 0]
    print df.head()
    return X, Y
    session = get_db_session()
    objs = session.query(ZhenxiongPinkunhu2015).all()[:10]
    for item in objs:
        X.append([
            item.province, item.city, item.county, item.town, item.village, item.group,
            item.name[:1], '有银行卡' if item.bank_name else '无银行卡', '有电话' if item.call_number else '无电话',
            str(item.member_count), item.standard, item.reason, item.other_reason])
        Y.append(item.poor_status)
    clean_data(X)
    clean_data(Y)
    print X, Y
    return X, Y


def update_zhengxiong_2015():
    ''' 更新镇雄2015的下一年是否脱贫以及下一年收入增长数据 '''
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
    get_data()
    #update_zhengxiong_2015()




